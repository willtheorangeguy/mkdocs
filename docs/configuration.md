# Configuration

What a project repository can set, and what it inherits.

## Precedence

Settings resolve in this order, highest priority first:

1. The project's own `mkdocs.yml`
2. `shared/mkdocs.base.yml`, pulled in by `INHERIT:`
3. MkDocs and Material defaults

MkDocs deep-merges dictionaries and **replaces** lists.

!!! danger "Never declare `plugins:` or `markdown_extensions:` in a project repo"
    Both are lists. Declaring either replaces the shared set instead of adding
    to it, silently removing search, macros, snippets, mkdocstrings, and every
    markdown extension. The symptom is a site that builds fine and renders
    nothing correctly.

## Placeholders

Every token in `template/mkdocs.yml` that must be replaced when stamping the
template into a repository.

The placeholders below are literal text, so this table is wrapped in a raw
block — otherwise the macros plugin evaluates them and fails the build. That
is the same trap described in the [writing guide](writing-guide.md).

{% raw %}

<div class="wt-reference" markdown>

| Placeholder | Example | Description |
|---|---|---|
| `{{SITE_NAME}}` | `LEGO Block Creator` | Human-readable project name |
| `{{SITE_DESCRIPTION}}` | `Design and export LEGO models from the command line.` | One sentence; becomes the meta description |
| `{{OWNER}}` | `willtheorangeguy` | GitHub owner, case-sensitive |
| `{{OWNER_LOWER}}` | `willtheorangeguy` | Owner lowercased, for the `github.io` hostname |
| `{{REPO_NAME}}` | `LEGO-Block-Creator` | Repository name, case-sensitive |
| `{{DEFAULT_BRANCH}}` | `main` | Used by `edit_uri`; `main` or `master` |
| `{{DOCS_SUBPATH}}` | *(empty)* | `docs/` only when an app owns the Pages root |
| `{{PACKAGE_NAME}}` | `lego_block_creator` | In `api.md`, Python repos only |

</div>

{% endraw %}

`site_url` must be exact. Material derives canonical links, the sitemap, and
instant navigation from it, and a wrong value degrades search indexing without
producing a warning.

## Workflow inputs

Accepted by `docs-build.yml`.

<div class="wt-reference" markdown>

| Input | Type | Default | Description |
|---|---|---|---|
| `docs_subpath` | string | *(empty)* | Publish docs under this subpath. Empty means the site root. |
| `app_path` | string | `.` | Directory of the existing site to publish at the root when `docs_subpath` is set. |
| `python-version` | string | `3.12` | Python used to build the docs. |
| `strict` | boolean | `true` | Fail the build on any MkDocs warning. |
| `shared_ref` | string | `main` | Ref of this repository to build against. |

</div>

Accepted by `docs-lint.yml`.

<div class="wt-reference" markdown>

| Input | Type | Default | Description |
|---|---|---|---|
| `check_links` | boolean | `true` | Run the external link checker. |
| `python-version` | string | `3.12` | Python used for the strict build. |
| `shared_ref` | string | `main` | Ref of this repository to build against. |

</div>

### Publishing docs alongside an existing site

```yaml title=".github/workflows/docs.yml"
jobs:
  docs:
    uses: willtheorangeguy/mkdocs/.github/workflows/docs-build.yml@main
    with:
      docs_subpath: docs
```

The repository's original Pages workflow must be deleted at the same time.

## What a repository may override

| Setting | Override? | Notes |
|---|---|---|
| `site_name`, `site_description`, `site_url` | Required | Identity |
| `repo_url`, `repo_name`, `edit_uri` | Required | Links back to source |
| `nav` | Required | Drop entries that do not apply |
| `theme.logo` | Optional | Delete if there is no `docs/images/logo.png` |
| `theme.palette` | Discouraged | Breaks visual consistency across sites |
| `plugins`, `markdown_extensions` | Never | Replaces the shared set |
| `extra_css`, `extra_javascript` | Never | Managed by the design system |

A repository needing a bespoke theme partial commits it to `overrides/` at the
same path as the shared one. Staging is no-clobber, so the local file wins
without forking the design system.

## Invalid values

MkDocs fails the build on an unknown top-level key, so a typo surfaces
immediately. An unknown key *inside* `theme:` is passed to the theme and
usually ignored silently — check spelling against the Material documentation
when an option appears to have no effect.

{{ support() }}
