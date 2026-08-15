<!-- Logo -->
<h1 align="center">
  Docs Template
</h1>

<!-- Copy -->
<h4 align="center">Shared MkDocs configuration, design system, and GitHub Actions for every repository.</h4>

<!-- Badges -->
<div align="center">
  <img alt="Docs State" src="https://github.com/willtheorangeguy/mkdocs/actions/workflows/docs.yml/badge.svg">
  <img alt="Lint State" src="https://github.com/willtheorangeguy/mkdocs/actions/workflows/lint.yml/badge.svg">
  <img alt="Documentation" src="https://img.shields.io/badge/docs-online-c33207">
</div>

<!-- Navigation -->
<p align="center">
  <a href="#what-this-is">What This Is</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#repository-layout">Repository Layout</a> •
  <a href="#contributing">Contributing</a>
</p>

**Documentation: [willtheorangeguy.github.io/mkdocs](https://willtheorangeguy.github.io/mkdocs/)**

## What This Is

Every repository gets a `docs/` folder following the same structured Markdown
pattern, published as a [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
site on GitHub Pages. Project repos carry documentation content and a name.
Everything else — theme, plugins, build logic, writing conventions — lives
here.

The point is scale. Across 130+ repositories, a build fix, a dependency bump,
or a restyle should be one commit, not 130.

* **One reusable workflow** builds and deploys every site.
* **Config inheritance** via `INHERIT:` — one theme and plugin set, everywhere.
* **A shared design system** of CSS tokens and components.
* **Coexists with existing sites** — repos already serving an app on Pages keep
  their root URL and get docs at `/docs/`.
* **Root files by reference** — `CHANGELOG.md` and friends are included, never
  copied, so they cannot drift.
* **A written standard** for voice and structure, so AI-generated pages read
  consistently across projects.

## How To Use

To add a documentation site to a repository, follow
**[ROLLOUT.md](ROLLOUT.md)**. Before writing any page, read
**[docs.instructions.md](docs.instructions.md)**.

To preview a site locally, from the root of the repository you are documenting:

```bash
# Clone this repository alongside yours
git clone https://github.com/willtheorangeguy/mkdocs

# Serve, staging the design system exactly as CI does
../mkdocs/scripts/docs-serve.sh        # or scripts\docs-serve.ps1 on Windows
```

To verify a repository is ready to publish:

```bash
mkdocs build --strict
```

The build must exit clean with zero warnings.

## Repository Layout

```text
├── shared/               Config inherited by every repo
│   ├── mkdocs.base.yml   Theme, extensions, plugins, validation
│   ├── requirements-docs.txt
│   ├── macros.py         Jinja variables and helpers
│   └── lint/             markdownlint and lychee configuration
├── design-system/        Staged into every repo at build time
│   ├── stylesheets/      Tokens and components
│   ├── javascript/       Table sorting
│   ├── icons/            Custom SVGs
│   └── overrides/        Material theme partials
├── template/             Copied into a project repo verbatim
├── scripts/              Local preview
├── .github/workflows/    Reusable build and lint workflows
├── docs/                 This repository's own site
├── docs.instructions.md  Writing standard
└── ROLLOUT.md            Per-repository procedure
```

## Contributing

Changes here reach every documentation site on its next build. Two rules:

1. **Never hardcode a colour** in the design system. Every colour is a token
   defined for both light and dark. A hardcoded value produces an unreadable
   page for half the readers.
2. **Never declare `plugins:` or `markdown_extensions:` in a project repo.**
   MkDocs replaces lists rather than merging them, so it silently discards the
   entire shared set.

Run `scripts/docs-serve.ps1 -Build` before opening a pull request.

If support is required, please open a
**[GitHub Discussion](https://github.com/willtheorangeguy/mkdocs/discussions)**.
