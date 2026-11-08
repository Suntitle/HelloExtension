# Hello extension

Suntitle Python extension that sends the text `Hello` every 10 seconds over
WebSocket. The first message arrives 10 seconds after connection. Failed
connections retry after 5 seconds. Stop the process to stop sending.

The default `/translate` route forwards the messages to connected displays.
Incoming text is not used.

## Run directly

```sh
python3 -m venv .venv
.venv/bin/pip install 'websockets>=12,<16'
.venv/bin/python hello.py --server ws://localhost:3030/translate
```

## Register with Suntitle

Register this directory as a Local extension source. The controller MUST be able
to read the directory. For Compose, mount its parent directory through
`LOCAL_EXTENSIONS_DIR` and register `/opt/suntitle/extensions/HelloExtension`.
Alternatively, publish this repository and register its HTTP(S) Git URL.

Create an enabled node using the **Hello** extension on a Diamant host. Diamant
installs the dependencies from `pyproject.toml` and supplies the relay URL.
The `endpoint` setting defaults to `translate`; use `transcribe` to send the
messages through a translator before display.
