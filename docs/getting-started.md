# Getting started

By the end of this page one repository has a documentation site building
locally. Publishing it is [Rollout](rollout.md) step 6.

## Prerequisites

| Requirement | Minimum version | Check with |
|---|---|---|
| Python | 3.9 | `python --version` |
| Git | any | `git --version` |

## Install

Nothing is installed globally. The dependencies are pinned in
`shared/requirements-docs.txt` and installed on demand by the preview script.

## First run

1. Clone this repository beside the one you want to document.

    ```bash
    git clone https://github.com/willtheorangeguy/mkdocs
    ```

2. Copy the template into the target repository.

    ```bash
    cd ../your-repo
    cp    ../mkdocs/template/mkdocs.yml            .
    cp -r ../mkdocs/template/.github/workflows/.   .github/workflows/
    cp -r ../mkdocs/template/docs/.                docs/
    cp -r ../mkdocs/template/overrides/.           overrides/
    cp    ../mkdocs/docs.instructions.md           docs/
    ```

3. Replace the placeholders in `mkdocs.yml`. Every one is listed in
    [Configuration](configuration.md#placeholders).

4. Preview the site.

    === "Windows"

        ```powershell
        ..\mkdocs\scripts\docs-serve.ps1
        ```

    === "macOS / Linux"

        ```bash
        ../mkdocs/scripts/docs-serve.sh
        ```

    ```text
    Serving on http://127.0.0.1:8000 ...
    ```

5. Confirm the build is clean. This is the check CI runs.

    ```bash
    mkdocs build --strict
    ```

    ```text
    INFO - Documentation built in 1.42 seconds
    ```

## What just happened

The preview script cloned this repository into `.mkdocs-shared/` and staged the
design system into `docs/stylesheets/`, `docs/javascript/`, and `overrides/`.
Your `mkdocs.yml` inherits everything else through its `INHERIT:` line, which
resolves against that checkout.

The build workflow does exactly the same thing in CI, which is why a clean
local build predicts a green pipeline.

## Next steps

- [Rollout](rollout.md) — the full per-repository procedure, including
  migrating an existing `docs/` folder
- [Writing guide](writing-guide.md) — read before writing any page
- [Configuration](configuration.md) — what a repository can override

{{ support() }}
