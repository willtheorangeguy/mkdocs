"""Shared macros for every documentation site.

Registered by ``shared/mkdocs.base.yml`` as::

    plugins:
      - macros:
          module_name: .mkdocs-shared/shared/macros

Everything defined in :func:`define_env` is available inside markdown as a
Jinja expression, so values that would otherwise be copy-pasted into 130
repos live here instead.

.. warning::
   The macros plugin evaluates Jinja in *all* markdown. A literal ``{{`` or
   ``{%`` in a code sample will be parsed as a macro and fail the build with
   ``on_error_fail: true``. Wrap such blocks in a raw tag — see
   ``docs.instructions.md``, "Code blocks".
"""

from __future__ import annotations

import datetime
import urllib.parse

# --------------------------------------------------------------------------
# Organisation-wide constants. Change here, not in any repo.
# --------------------------------------------------------------------------

ORG_NAME = "willtheorangeguy"
ORG_URL = "https://github.com/willtheorangeguy"
DISCORD_INVITE = "https://discord.gg/73azSgcNYt"
PYPI_BASE = "https://pypi.org/project"
GHCR_BASE = "https://ghcr.io"

SHIELDS = "https://img.shields.io"


def _repo_slug(config) -> str:
    """Return ``owner/name`` from the site's ``repo_url``.

    Falls back to an empty string when ``repo_url`` is unset so that a
    missing value degrades to a blank badge rather than a build failure.
    """
    repo_url = (config.get("repo_url") or "").rstrip("/")
    if not repo_url:
        return ""
    parts = urllib.parse.urlparse(repo_url).path.strip("/")
    return parts


def define_env(env) -> None:
    """Register variables and macros with the macros plugin."""
    config = env.conf
    slug = _repo_slug(config)
    owner, _, name = slug.partition("/")

    # ---- Variables -----------------------------------------------------

    env.variables["org"] = ORG_NAME
    env.variables["org_url"] = ORG_URL
    env.variables["discord"] = DISCORD_INVITE
    env.variables["year"] = datetime.date.today().year

    env.variables["repo_slug"] = slug
    env.variables["repo_owner"] = owner
    env.variables["repo_name"] = name
    env.variables["issues_url"] = f"{config.get('repo_url', '')}/issues"
    env.variables["discussions_url"] = f"{config.get('repo_url', '')}/discussions"
    env.variables["releases_url"] = f"{config.get('repo_url', '')}/releases/latest"

    # ---- Macros --------------------------------------------------------

    @env.macro
    def gh(path: str = "", label: str | None = None) -> str:
        """Link to a path inside this repository on GitHub.

        Args:
            path: Repo-relative path, e.g. ``CONTRIBUTING.md``.
            label: Link text. Defaults to ``path``.

        Returns:
            A markdown link.
        """
        base = (config.get("repo_url") or "").rstrip("/")
        url = f"{base}/blob/HEAD/{path.lstrip('/')}" if path else base
        return f"[{label or path or slug}]({url})"

    @env.macro
    def pypi(package: str) -> str:
        """Link to a package on the Python Package Index."""
        return f"[`{package}`]({PYPI_BASE}/{package}/)"

    @env.macro
    def badges(*kinds: str) -> str:
        """Render a row of shields.io badges.

        Args:
            *kinds: Any of ``version``, ``issues``, ``pulls``, ``license``,
                ``downloads``, ``stars``. Unknown names are ignored so a
                typo degrades gracefully instead of failing the build.

        Returns:
            A single line of markdown images.
        """
        if not slug:
            return ""
        available = {
            "version": f"{SHIELDS}/github/v/release/{slug}?include_prereleases",
            "issues": f"{SHIELDS}/github/issues/{slug}",
            "pulls": f"{SHIELDS}/github/issues-pr/{slug}",
            "license": f"{SHIELDS}/github/license/{slug}",
            "downloads": f"{SHIELDS}/github/downloads/{slug}/total",
            "stars": f"{SHIELDS}/github/stars/{slug}",
        }
        out = [
            f"![{kind}]({available[kind]})"
            for kind in (kinds or available)
            if kind in available
        ]
        return " ".join(out)

    @env.macro
    def support() -> str:
        """The standard support block, identical on every site."""
        return (
            f"If you need help, open a "
            f"[GitHub Discussion]({config.get('repo_url', '')}/discussions) "
            f"or join the [Discord]({DISCORD_INVITE})."
        )
