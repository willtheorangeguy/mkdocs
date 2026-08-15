<!--
  INSTALLATION

  Every method the project ACTUALLY supports gets a tab. Delete the tabs for
  methods that do not exist — a documented install path that does not work is
  worse than an undocumented one that does.

  Source of truth for which methods exist: the README, pyproject.toml /
  package.json, Dockerfile, and the release workflows.
-->

# Installation

<!-- One sentence naming the available methods. -->

## Requirements

| Requirement | Version | Notes |
|---|---|---|
| <!-- TODO --> | <!-- TODO --> | <!-- TODO --> |

## Install

=== "Package manager"

    <!-- Delete this tab if the project is not published to a registry. -->

    ```bash
    # TODO: pip install / npm install / etc.
    ```

=== "Executable"

    <!-- Delete this tab if there are no released binaries. -->

    1. Download the latest release from the [releases page]({{ releases_url }}).
    2. Extract the archive.
    3. Run the executable.

=== "Docker"

    <!-- Delete this tab if there is no Dockerfile or published image. -->

    ```bash
    # TODO: docker pull ...
    # TODO: docker run ...
    ```

=== "From source"

    ```bash
    git clone {{ config.repo_url }}.git
    cd {{ repo_name }}
    # TODO: build / install command
    ```

## Verify the installation

<!--
  A command and its output, proving the install worked. This section is what
  turns "I ran the installer" into "it is installed".
-->

```bash
# TODO: version or health-check command
```

```text
TODO: expected output
```

## Upgrading

```bash
# TODO: upgrade command
```

## Uninstalling

```bash
# TODO: uninstall command
```

{{ support() }}
