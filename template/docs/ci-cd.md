<!--
  CI/CD  (extended page)

  Include only when the repo has workflows. Delete the file and its nav
  entry otherwise.

  Source of truth: .github/workflows/. Document what is there — do not
  describe workflows the repo does not have.
-->

# CI/CD

<!-- One sentence: what runs automatically and when. -->

## Workflows

<div class="wt-reference" markdown>

| Workflow | Trigger | Purpose |
|---|---|---|
| `docs.yml` | Push to the default branch | Builds and publishes this site |
| `docs-lint.yml` | Pull request | Markdown style, strict build, link check |
| <!-- TODO --> | <!-- TODO --> | <!-- TODO --> |

</div>

## Documentation

This site is built by a reusable workflow in
[willtheorangeguy/mkdocs](https://github.com/willtheorangeguy/mkdocs). The
workflow in this repository only calls it and grants the Pages permissions,
so build changes are made once, centrally, rather than in every repository.

<!-- One H2 per remaining workflow below. For each: what triggers it, what it
     does, and what a failure means for a contributor. -->

## <!-- TODO: workflow name -->

## Release process

<!--
  The actual steps that produce a release: tag format, what is published and
  where, whether it is automatic. Delete this section if there is no release
  process.
-->

{{ support() }}
