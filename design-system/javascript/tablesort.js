/* =========================================================================
   Sortable reference tables
   =========================================================================

   Makes long reference tables (configuration.md, api.md) sortable by
   clicking a header. Opt in per table by wrapping it in a container with
   the `wt-reference` class, or by adding `wt-sortable` to the table.

   Self-contained on purpose: no CDN, no dependency, so a site keeps
   working when the network does not.

   `navigation.instant` swaps page content without a reload, so the setup
   runs on Material's `document$` observable when it exists and falls back
   to a plain DOM-ready listener when it does not.
   ========================================================================= */

(function () {
  "use strict";

  var COLLATOR = new Intl.Collator(undefined, {
    numeric: true,
    sensitivity: "base"
  });

  /**
   * Extract the comparable value of a cell.
   * A `data-sort` attribute wins, so a column can sort on something other
   * than what it displays (a raw timestamp behind a friendly date).
   */
  function cellValue(row, index) {
    var cell = row.cells[index];
    if (!cell) return "";
    return (cell.getAttribute("data-sort") || cell.textContent || "").trim();
  }

  function sortByColumn(table, index, direction) {
    var body = table.tBodies[0];
    if (!body) return;

    var rows = Array.prototype.slice.call(body.rows);
    var factor = direction === "desc" ? -1 : 1;

    rows.sort(function (a, b) {
      return COLLATOR.compare(cellValue(a, index), cellValue(b, index)) * factor;
    });

    // Re-appending in order is enough; the browser moves rather than clones.
    rows.forEach(function (row) {
      body.appendChild(row);
    });
  }

  function activate(table) {
    var head = table.tHead;
    if (!head || !head.rows.length || table.dataset.wtSortReady) return;
    table.dataset.wtSortReady = "true";

    var headers = Array.prototype.slice.call(head.rows[0].cells);

    headers.forEach(function (header, index) {
      header.setAttribute("data-wt-sortable", "");
      header.setAttribute("role", "button");
      header.setAttribute("tabindex", "0");

      function toggle() {
        var current = header.getAttribute("data-wt-sort");
        var next = current === "asc" ? "desc" : "asc";

        headers.forEach(function (other) {
          other.removeAttribute("data-wt-sort");
          other.removeAttribute("aria-sort");
        });

        header.setAttribute("data-wt-sort", next);
        header.setAttribute(
          "aria-sort",
          next === "asc" ? "ascending" : "descending"
        );

        sortByColumn(table, index, next);
      }

      header.addEventListener("click", toggle);
      header.addEventListener("keydown", function (event) {
        if (event.key === "Enter" || event.key === " ") {
          event.preventDefault();
          toggle();
        }
      });
    });
  }

  function setup() {
    var selector = ".wt-reference table, table.wt-sortable";
    document.querySelectorAll(selector).forEach(activate);
  }

  if (typeof window.document$ !== "undefined" && window.document$.subscribe) {
    window.document$.subscribe(setup);
  } else if (document.readyState !== "loading") {
    setup();
  } else {
    document.addEventListener("DOMContentLoaded", setup);
  }
})();
