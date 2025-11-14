# Alpha Board

## Development

### Set development environment

This project uses **pre-commit** to maintain a consistent development environment, enforce formatting standards and ensure high code quality.

To begin working with the repository, activate the virtual environment:

```bash
source scripts/venv.sh
```

### Run the app

Run as a desktop app:

```
uv run flet run
```

Run as a web app:

```
uv run flet run --web
```

### Build the app

#### Android

```
flet build apk -v
```

For more details on building and signing `.apk` or `.aab`, refer to the [Android Packaging Guide](https://flet.dev/docs/publish/android/).

#### iOS

```
flet build ipa -v
```

For more details on building and signing `.ipa`, refer to the [iOS Packaging Guide](https://flet.dev/docs/publish/ios/).

#### macOS

```
flet build macos -v
```

For more details on building macOS package, refer to the [macOS Packaging Guide](https://flet.dev/docs/publish/macos/).

#### Linux

```
flet build linux -v
```

For more details on building Linux package, refer to the [Linux Packaging Guide](https://flet.dev/docs/publish/linux/).

#### Windows

```
flet build windows -v
```

For more details on building Windows package, refer to the [Windows Packaging Guide](https://flet.dev/docs/publish/windows/).

### Commit changes

When your changes are ready, create a commit using **cz**:

```bash
cz commit
```

Then follow the interactive instructions provided by **cz**.