<!--
  CONFIGURATION

  Reference material. Readers arrive here mid-task with one specific
  question, usually "why isn't my setting applying" — which is why the
  precedence section comes first and is not optional.

  Every option needs an example value. A type and a description do not tell
  the reader what a valid value looks like.
-->

# Configuration

<!-- One sentence: what can be configured and from where. -->

## Precedence

Settings are resolved in this order, highest priority first:

1. Command-line flags
2. Environment variables
3. Configuration file
4. Built-in defaults

<!-- Correct this list to match the project's actual behaviour. If the
     project only supports one source, say so and delete the rest. -->

## Configuration file

<!-- Delete this section if the project has no config file. -->

<div class="wt-reference" markdown>

| Option | Type | Default | Description |
|---|---|---|---|
| `<!-- TODO -->` | string | `<!-- TODO -->` | <!-- TODO. Enumerate valid values. --> |

</div>

```yaml title="config.yml"
# TODO: a complete, working example configuration
```

## Environment variables

<!-- Delete this section if the project reads no environment variables. -->

Environment variables are named by uppercasing the option and applying the
`<!-- TODO -->_` prefix.

<div class="wt-reference" markdown>

| Variable | Type | Default | Description |
|---|---|---|---|
| `<!-- TODO -->` | <!-- TODO --> | `<!-- TODO -->` | <!-- TODO --> |

</div>

## Command-line flags

<!-- Delete this section if there is no CLI. -->

<div class="wt-reference" markdown>

| Flag | Type | Default | Description |
|---|---|---|---|
| `<!-- TODO -->` | <!-- TODO --> | `<!-- TODO -->` | <!-- TODO --> |

</div>

## Examples

<!-- At least one complete, working configuration. Not a fragment. -->

### <!-- TODO: a named scenario -->

```yaml title="config.yml"
# TODO
```

## Invalid values

<!--
  State what happens when a value is wrong: ignored with a warning, or
  fatal. Readers debugging configuration need this and it is almost never
  written down.
-->

{{ support() }}
