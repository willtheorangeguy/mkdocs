<!--
  API

  Pick ONE of the three forms below to match the project's actual public
  interface, and delete the other two.

  If the project genuinely exposes no public interface, delete this file and
  its nav entry in mkdocs.yml.
-->

# API

<!--
  One paragraph: what the public surface is and where a reader should start.
  This is the part mkdocstrings cannot generate.
-->

<!-- =====================================================================
     FORM 1 — Python

     Rely on mkdocstrings. Write Google-style docstrings in the SOURCE
     rather than restating signatures here; a hand-copied signature is wrong
     the first time the code changes.

     Replace {{PACKAGE_NAME}} with the importable package name.
     ===================================================================== -->

## Reference

::: {{PACKAGE_NAME}}
    options:
      show_root_heading: true
      members_order: source

<!-- =====================================================================
     FORM 2 — Command line

     One table per command, plus a usage example. Never prose-describe
     flags.
     ===================================================================== -->

<!--
## `<command>`

<What it does, in one sentence.>

<div class="wt-reference" markdown>

| Flag | Type | Default | Description |
|---|---|---|---|
| `--example` | string | `none` | TODO |

</div>

```bash
# TODO: a complete, runnable invocation
```
-->

<!-- =====================================================================
     FORM 3 — HTTP

     For each endpoint: method and path, parameters, request body, response
     body, and the status codes it ACTUALLY returns, error cases included.
     An endpoint reference with only the happy path is half-written.
     ===================================================================== -->

<!--
## `GET /example`

<What it returns.>

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | TODO |

**Response**

```json
{ "TODO": true }
```

| Status | Meaning |
|---|---|
| `200` | TODO |
| `404` | TODO |
-->

{{ support() }}
