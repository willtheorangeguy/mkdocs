# Docs template

Shared MkDocs configuration, design system, and GitHub Actions for every
repository. Project repos carry documentation content and a name; everything
else is inherited from here.

The point is scale. Across 130 repositories, a build fix, a dependency bump, or
a restyle should be one commit — not 130.

## Key features

- **One reusable workflow** builds and deploys every site. A project repo's
  workflow is fifteen lines and contains no build logic.
- **Config inheritance** — theme, markdown extensions, plugins, and validation
  live in one file that every repo pulls in.
- **A shared design system** of tokens and components, so 130 sites look like
  one family rather than 130 default installs.
- **Coexists with existing sites.** Repos already serving an app on GitHub
  Pages keep their root URL and get docs at `/docs/`.
- **Root files by reference.** `CHANGELOG.md`, `CONTRIBUTING.md`, and the rest
  are included, never copied, so they cannot drift.
- **A written standard** for voice and structure, so AI-generated pages read
  consistently across projects.

## Quick start

From the root of a repository you want to document:

```bash
git clone --depth 1 https://github.com/willtheorangeguy/mkdocs .mkdocs-shared
.mkdocs-shared/scripts/docs-serve.sh
```

See [Getting started](getting-started.md) for the full path.

## Where to next

<div class="wt-grid" markdown>

[:material-rocket-launch: **Getting started**<br>Add a docs site to one repository](getting-started.md){ .wt-card }

[:material-sitemap: **Architecture**<br>How the pieces fit together](architecture.md){ .wt-card }

[:material-tune: **Configuration**<br>What each repository can set](configuration.md){ .wt-card }

[:material-palette: **Design system**<br>Every component, rendered](design-system.md){ .wt-card }

[:material-fountain-pen-tip: **Writing guide**<br>Voice, structure, and page contracts](writing-guide.md){ .wt-card }

[:material-clipboard-check: **Rollout**<br>The per-repository procedure](rollout.md){ .wt-card }

</div>

## Support

{{ support() }}
