# Rollout instructions

How to add the documentation site to one repository. This file is the
mechanical procedure: which files to create, what to check first, how to
migrate an existing `docs/` folder.

**How to write the pages is a separate document.** Read
[`docs.instructions.md`](https://github.com/willtheorangeguy/mkdocs/blob/main/docs.instructions.md) before writing any prose. This
file tells you *what* to build; that one tells you *how it should read*.

Work one repository at a time. Finish and verify each before starting the next.

---

## Target end state

```text
<repo>/
├── .github/workflows/
│   ├── docs.yml              caller — builds and deploys
│   └── docs-lint.yml         caller — PR checks
├── docs/
│   ├── index.md
│   ├── getting-started.md
│   ├── installation.md
│   ├── configuration.md
│   ├── architecture.md
│   ├── api.md
│   ├── testing.md            extended
│   ├── ci-cd.md              extended
│   ├── faq.md                extended
│   ├── contributing.md       include
│   ├── changelog.md          include
│   ├── code-of-conduct.md    include
│   ├── security.md           include
│   ├── license.md            include
│   ├── docs.instructions.md  writing standard (excluded from the built site)
│   └── images/
├── overrides/                Material custom_dir, usually empty
├── mkdocs.yml
└── README.md                 UNCHANGED
```

The site publishes to `https://<pages-host>/<repo>/`, or
`https://<pages-host>/<repo>/docs/` when an application already owns the
Pages root. The host is not always `<owner>.github.io` — see
[Pages hosts](#pages-hosts).

---

## Step 1 — Triage

Answer all of these before creating a single file. Each one changes what you
build.

### Default branch

```bash
git symbolic-ref refs/remotes/origin/HEAD --short
```

Sets `{{DEFAULT_BRANCH}}` in `mkdocs.yml` (used for `edit_uri`). The workflow
itself triggers on both `main` and `master`, so no workflow edit is needed.

### Project type — decides `api.md`

| Signal | `api.md` becomes |
|---|---|
| `pyproject.toml` / `setup.py` | mkdocstrings form; set `{{PACKAGE_NAME}}` to the importable package |
| CLI entry point, no library surface | Command/flag reference tables |
| Serves HTTP | Endpoint reference |
| No public interface at all | **Delete `api.md` and its nav entry** |

### Does it already publish to GitHub Pages?

```bash
grep -rl "deploy-pages\|gh-pages\|pages-build-deployment" .github/workflows/ 2>/dev/null
ls index.html 2>/dev/null
```

If either hits:

1. Uncomment `docs_subpath: docs` in `.github/workflows/docs.yml`.
2. Set `{{DOCS_SUBPATH}}` to `docs/` in `site_url`.
3. **Delete the repository's existing Pages workflow.**

!!! danger "The most likely way this breaks"
    Two workflows deploying to Pages will fight over the deployment and one
    will fail, intermittently. The old workflow must be removed, not disabled
    by renaming. The new workflow republishes the app at the root — that job
    is now its responsibility.

Known repos in this category: `Snoopy-Landing-Page`, `Chrome-File-Directory`,
`Apache-File-Directory`, `Nginx-File-Directory`, `stacktower-docker`,
`git-rewrite-commits`, `CSUS-Code`, `Homework-Dump`, and the `CPSC-*-Code`
repos using `jekyll-gh-pages.yml`. Verify rather than trusting this list.

### Health files are org-level — link, don't include

`CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md` are being
consolidated into [willtheorangeguy/.github](https://github.com/willtheorangeguy/.github)
and **deleted from individual repos**. As of August 2026 an open
`docs/standardize` pull request does exactly that in each repo.

So the template links to the org copies from the nav instead of including
them. Do not add snippet pages for these three, even when the local files are
still present — the site would build today and break the moment that pull
request merges.

Check whether the repo is in that wave before deciding:

```bash
gh pr list --search "head:docs/standardize" --json number,title
```

The two that stay per-repo and *are* included as pages:

- `CHANGELOG.md` — genuinely repo-specific
- `LICENSE.md` — normalised by that wave, not deleted

A repo that deliberately keeps its own local health files can still use the
snippet pages; the templates remain in `template/docs/`.

### Which root files exist?

```bash
ls CHANGELOG.md CONTRIBUTING.md CODE_OF_CONDUCT.md SECURITY.md LICENSE.md 2>/dev/null
```

**Delete the snippet page AND its nav entry for every file that does not
exist.** `check_paths: true` turns a missing include into a build failure, not
an empty page. Note that some repos use `LICENSE` with no extension — either
correct the path in `license.md` or drop the page.

### Fix cross-references inside the included root files

`CONTRIBUTING.md` and `SECURITY.md` typically link to each other and to
`README.md` with **relative** paths. Those work on GitHub but not once the file
is included into a docs page, because the target is not a page in the site:

```text
WARNING - Doc file 'security.md' contains a link 'CONTRIBUTING.md', but the
          target is not found among documentation files.
```

Rewrite them as absolute GitHub URLs, which are correct in both contexts:

```markdown
[`CONTRIBUTING`](https://github.com/OWNER/REPO/blob/HEAD/CONTRIBUTING.md)
```

Use `/blob/HEAD/`, not `/blob/main/`. Roughly half these repos default to
`master`, and a hardcoded `main` produces a 404 — several already have this bug.

Check for the same problem in reverse: an in-page anchor such as `[below](#style)`
pointing at a heading that does not exist is broken on GitHub too, and the
strict build is often the first thing to notice.

This is editing root files, which is allowed — the standing rule is only that
you do not restructure `README.md`.

### Deleting a page means deleting three things

Every time triage removes a page, remove all of:

1. The file in `docs/`
2. Its entry in the `nav:` block of `mkdocs.yml`
3. **Every inbound link to it** — the card grid in `index.md` and the "Next
   steps" list in `getting-started.md` both link to `api.md` by default

Missing the third is the most common first build failure:

```text
WARNING - Doc file 'index.md' contains a link 'api.md', but the target is
          not found among documentation files.
```

### Which extended pages apply?

- `testing.md` — only if there is a test suite
- `ci-cd.md` — only if there are workflows beyond the two you are adding
- `faq.md` — **always**. Do not wait for real questions to accumulate; the
  repos with no recorded questions are the ones where a reader has nowhere
  else to turn. Predict the questions from what the source, tests, and
  workflows told you, and answer every one from verified behaviour. See
  "Writing an FAQ" in `docs.instructions.md`.

### Does `docs/` already exist?

If yes, go to [Step 3](#step-3-migrate-an-existing-docs-folder) after copying
the template.

---

## Step 2 — Stamp the template

Copy from `willtheorangeguy/mkdocs`:

| From | To |
|---|---|
| `template/mkdocs.yml` | `mkdocs.yml` |
| `template/.github/workflows/docs.yml` | `.github/workflows/docs.yml` |
| `template/.github/workflows/docs-lint.yml` | `.github/workflows/docs-lint.yml` |
| `template/docs/*` | `docs/` (do not overwrite existing files) |
| `template/overrides/.gitkeep` | `overrides/.gitkeep` |
| `docs.instructions.md` | `docs/docs.instructions.md` |

Then replace every placeholder in `mkdocs.yml`:

| Placeholder | Value |
|---|---|
| `{{SITE_NAME}}` | Human-readable project name, e.g. `LEGO Block Creator` |
| `{{SITE_DESCRIPTION}}` | One sentence — reuse the README's description line |
| `{{OWNER}}` | `willtheorangeguy`, `Dog-Face-Development`, … |
| `{{PAGES_HOST}}` | Pages host for this owner — see [Pages hosts](#pages-hosts) |
| `{{REPO_NAME}}` | Repository name |
| `{{DEFAULT_BRANCH}}` | `main` or `master` |
| `{{DOCS_SUBPATH}}` | Empty, or `docs/` for an app-serving repo |
| `{{PACKAGE_NAME}}` | In `api.md`, for Python repos only |

### Pages hosts

Two of the three accounts serve Pages from a custom domain, so `site_url` is
**not** `<owner>.github.io` for most repos.

| Owner | Pages host | Example site URL |
|---|---|---|
| `willtheorangeguy` | `williamvdg.me` | `https://williamvdg.me/LEGO-Block-Creator/` |
| `Dog-Face-Development` | `dog-face-development.github.io` | `https://dog-face-development.github.io/Bars/` |
| `Daniela-and-Will-Travel` | `danielaandwilltravel.ca` | `https://danielaandwilltravel.ca/littlelink/` |

Confirm rather than trusting the table — the host is whatever the account's
`*.github.io` repo has as its CNAME:

```bash
gh api repos/OWNER/OWNER.github.io/pages --jq '.cname // "OWNER.github.io"'
```

Append `template/gitignore-additions.txt` to the repo's `.gitignore`. Those
paths are generated at build time; a committed copy starts overriding the
shared version and the site drifts.

Delete `theme.logo` from `mkdocs.yml` if the repo has no `docs/images/logo.png`
— the shared config falls back to an icon.

---

## Step 3 — Migrate an existing `docs/` folder

About 26 repos already have one, using UPPERCASE filenames.

### Renames

| Existing | Becomes |
|---|---|
| `docs/README.md` | `docs/index.md`, rewritten as a real landing page |
| `docs/USAGE.md` | Split: setup steps → `getting-started.md`, options → `configuration.md` |
| `docs/TESTING.md` | `docs/testing.md` |
| `docs/CI-CD.md` | `docs/ci-cd.md` |
| `docs/OPTIONS.md` | `docs/configuration.md` |
| Anything else | Lowercase it, keep the content, add a nav entry |

Use `git mv` so history follows the file.

!!! warning "Case-only renames on Windows"
    The filesystem is case-insensitive, so `git mv USAGE.md usage.md` is a
    no-op. Rename via a temporary name:

    ```bash
    git mv USAGE.md usage.tmp && git mv usage.tmp usage.md
    ```

### Rules

- **Never discard content.** A file that maps to no standard page becomes its
  own lowercase page with a nav entry. `Craft-Clash/docs/GAMEPLAY.md` is a real
  example — it becomes `gameplay.md`, not deleted.
- **Do not move `docs/images/`.** Root READMEs reference those files by
  absolute `raw.githubusercontent.com` URL. Moving or renaming them breaks the
  GitHub landing page silently.
- **Drop the old index scaffolding.** The `Documentation Structure` and
  `Available Documentation` sections in existing `docs/README.md` files are
  replaced by the site nav. Delete them and write `index.md` per the contract
  in `docs.instructions.md`.
- **Fix inbound links** to every renamed file, in the root `README.md` and in
  other docs pages.

---

## Step 4 — Write the content

Read [`docs.instructions.md`](https://github.com/willtheorangeguy/mkdocs/blob/main/docs.instructions.md) first.

Source material, in order of authority: the source code, the tests, the
workflows, then the README. Where they disagree, the code wins and the README
is out of date.

- **Reorganize, don't rewrite.** Existing README prose that already reads well
  moves across as-is. This is not a licence to restyle working text.
- **Never invent** features, flags, install methods, or return values.
- **Leave `<!-- TODO: ... -->`** where information genuinely is not available.
  A TODO is honest; a plausible guess is a bug that ships.
- **Do not modify the root `README.md`**, except to fix links broken by
  renames.
- Watch for the two build-breaking syntaxes: a literal `{{` or `{%` in a code
  sample needs a raw wrapper, and a literal include marker at the start of a
  line needs a leading semicolon to escape it.

---

## Step 5 — Verify

Locally, from the repository root:

```bash
git clone --depth 1 https://github.com/willtheorangeguy/mkdocs .mkdocs-shared
pip install -r .mkdocs-shared/shared/requirements-docs.txt
mkdir -p docs/stylesheets docs/javascript overrides/.icons
cp -r .mkdocs-shared/design-system/stylesheets/. docs/stylesheets/
cp -r .mkdocs-shared/design-system/javascript/. docs/javascript/
cp -rn .mkdocs-shared/design-system/overrides/. overrides/
cp -rn .mkdocs-shared/design-system/icons/. overrides/.icons/
mkdocs build --strict
```

`scripts/docs-serve.ps1` and `scripts/docs-serve.sh` in the template repo do
all of the above plus `mkdocs serve`.

**The build must exit clean with zero warnings.** `--strict` catches broken
internal links, orphaned files, bad anchors, missing snippet targets, and macro
errors. Do not consider a repository done until it passes.

Common failures:

| Message | Cause |
|---|---|
| `Snippet ... could not be found` | A snippet page whose root file does not exist. Delete the page and its nav entry. |
| `Config value 'nav': ... not found` | A nav entry pointing at a file you deleted. |
| `Error reading page ...: unexpected '{'` | A literal `{{` or `{%` in a code sample. Wrap it in a raw block. |
| `Cannot load module` (mkdocstrings) | Wrong `{{PACKAGE_NAME}}`, or the package is not importable from the repo root. |

---

## Step 6 — Enable Pages

Not automatic. Once per repository, after the first successful build:

```bash
# First time
gh api -X POST repos/OWNER/REPO/pages -f build_type=workflow

# Already enabled with a different source
gh api -X PUT repos/OWNER/REPO/pages -f build_type=workflow

# Point the repo's About section at the site
gh repo edit OWNER/REPO --homepage https://PAGES_HOST/REPO/
```

---

## Step 7 — Optional README link

Default is to change nothing. If you want the site discoverable from the
GitHub landing page, add one badge to the existing badge block:

```html
<!-- Documentation -->
<a href="https://PAGES_HOST/REPO/">
  <img alt="Documentation" src="https://img.shields.io/badge/docs-online-c33207">
</a>
```

---

## Per-repository checklist

- [ ] Triage answered: branch, project type, Pages conflict, root files, extended pages
- [ ] Template stamped, all placeholders replaced
- [ ] Old Pages workflow deleted, if there was one
- [ ] Snippet pages deleted for every missing root file
- [ ] Existing `docs/` migrated, no content discarded, `docs/images/` untouched
- [ ] Inbound links fixed in the root README
- [ ] `.gitignore` updated
- [ ] `mkdocs build --strict` passes with zero warnings
- [ ] Pushed, workflow green, site loads
- [ ] For app-serving repos: the app still loads at the root **and** docs load at `/docs/`
