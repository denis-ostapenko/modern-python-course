# Daybook reference application

This is the complete guided project. Read it after building the corresponding checkpoints.
Run commands from the starter root:

```text
uv run python daybook/main.py --data work/demo.json add reading 25
uv run python daybook/main.py --data work/demo.json list
uv run python daybook/main.py --data work/demo.json summary
```

The data option precedes the subcommand. Without it, data is stored in .daybook.json inside your home directory. A missing file starts empty. Invalid JSON, invalid records, and file errors are reported without overwriting the source. Saves replace a temporary file; this prevents a partly written document from becoming the main file. Concurrent writers are not supported. Back up important data before editing it manually.
