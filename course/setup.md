# Set up your local workspace

Use a desktop or laptop for the local course. Browser lesson 0.1 can run on a phone; a phone is not the supported device for the local editor workflow.

## Choose your system

The release includes macOS, Windows and Linux installation instructions based on official documentation. Local interactive verification was performed on macOS Apple Silicon. The release workflow checks Python code on all three operating systems. An automated job is not evidence that every installer dialog has been observed.

### macOS

1. Download [Visual Studio Code](https://code.visualstudio.com/download), open the archive, and move the application into Applications.
2. Open Terminal. Run `git --version`. If macOS offers Command Line Tools, install them and retry.
3. Install uv using the official installer:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

4. Close and reopen the terminal. Run `uv --version` and `git --version`.

Fallback: obtain the appropriate uv archive from the [official releases](https://github.com/astral-sh/uv/releases), extract it, and put its executable in a folder on your PATH. The official [installation guide](https://docs.astral.sh/uv/getting-started/installation/) explains package-manager options as well. Avoid mixing several installations unless you know which executable your terminal resolves.

### Windows

1. Install [VS Code](https://code.visualstudio.com/download) and [Git for Windows](https://git-scm.com/downloads/win) from their official sites.
2. Open PowerShell and use the official uv command:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

3. Close and reopen PowerShell. Run `uv --version` and `git --version`.

The command's execution-policy setting applies to that installer process. If your organization blocks installation, do not change machine policy: use a pre-provisioned environment or ask the device administrator to install uv. The fallback is the Windows binary from [official uv releases](https://github.com/astral-sh/uv/releases), extracted into a permitted PATH folder.

### Linux

Install VS Code using the [official distribution instructions](https://code.visualstudio.com/docs/setup/linux). Install Git through your distribution's package manager. Install uv with the same shell command shown for macOS, then reopen the terminal and check both versions. If the installer is unavailable, use the architecture-matched binary from [official uv releases](https://github.com/astral-sh/uv/releases).

## Open the prepared folder

Select Get the workspace in the course toolbar and extract the ZIP before opening it. The folder should contain main.py, pyproject.toml, uv.lock, tools and exercises. Do not run inside the archive preview.

In VS Code choose File > Open Folder. Select the extracted learner-workspace folder. In Extensions, install Python by Microsoft and Python Debugger by Microsoft. In Terminal > New Terminal:

```text
uv sync --frozen
uv run python main.py
uv run python tools/start_git.py
uv run python tools/check_environment.py
```

uv downloads the selected Python if needed. The program should print `reading: 25 minutes`. The final diagnostic should report READY. The Git helper creates a local exercise baseline; nothing is sent to GitHub.

From View > Command Palette, choose Python: Select Interpreter and select this project's .venv. See [VS Code's environment guide](https://code.visualstudio.com/docs/python/environments). Use the terminal command shown above throughout this course; another extension's Run button may choose a different interpreter.

## A map of the editor

| Region | Find it | Use it for |
| --- | --- | --- |
| Explorer | Left sidebar, file icon | Open main.py and see the root folder |
| Editor | Center tab labelled main.py | Edit source and save it |
| Terminal | Terminal > New Terminal | Run uv commands and read program output |
| Source Control | Sidebar branch icon | Inspect changed files and diffs |
| Run and Debug | Sidebar play/bug icon | Introduced in lesson 2.1 |
| Testing | Sidebar test icon, after extension discovery | Introduced in lesson 2.3 |

The first three regions are enough to begin. You do not need an agent pane or a cloud account.

## If a step fails

| Observed message | Next useful action |
| --- | --- |
| uv not found | Reopen the terminal after installation; run uv --version outside VS Code too |
| main.py not found | Open the extracted folder, then Terminal > New Terminal |
| no pyproject.toml | Check that the terminal is at the learner-workspace root |
| dependency download fails | Restore network access and retry uv sync --frozen; do not delete your source |
| unsupported Python | Let uv use the supplied .python-version rather than a system Python command |
| no Git baseline | Run tools/start_git.py in the extracted starter, then rerun the diagnostic |
| unexpected first output | Inspect main.py and restore only that file from the 0.2 checkpoint |

Once Python and dependencies have been cached, `uv run --offline python main.py` can run without internet. A first installation cannot promise offline access. The download includes all lesson text for reading without the site.

Continue with [Your real workspace](00-start-here/02-real-workspace.md).
