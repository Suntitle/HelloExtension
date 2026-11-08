"""Connect, send Hello periodically, and retry disconnected sessions until stopped.

Each connection waits ten seconds before its first message. Shutdown is terminal;
connection failures defer sending until a new connection succeeds.
"""

import argparse
import asyncio
import logging

import websockets


async def send_hello(server: str) -> None:
    """Send text frames every ten seconds; retry failed connections after five seconds."""
    while True:
        try:
            async with websockets.connect(server) as websocket:
                logging.info("Connected to %s", server)
                while True:
                    await asyncio.sleep(10)
                    await websocket.send("Hello")
                    logging.info("Sent Hello")
        except (OSError, websockets.exceptions.WebSocketException) as error:
            logging.warning("Connection failed: %s; retrying in five seconds", error)
            await asyncio.sleep(5)


def main() -> None:
    """Read the relay endpoint and run until interrupted by the host or user."""
    parser = argparse.ArgumentParser(description="Send Hello every ten seconds.")
    parser.add_argument("--server", default="ws://localhost:3030/translate")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    try:
        asyncio.run(send_hello(args.server))
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
