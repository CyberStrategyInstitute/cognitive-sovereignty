# Integration checks

On November 7, 2026, the local adapter passed an actual stdio client/server exchange using the official Python MCP SDK 1.30.0. The check covers tool discovery, read-only annotations, record lookup with original analysis, bounded pagination, CTSS calculation, unknown inputs, rejection of Boolean score inputs, unknown collections, excessive page sizes, and catalog discovery. JSON Schema checks passed for all event, signal, and lens records.

Run `python tests/check_mcp.py` after installing the optional requirements. The ordinary framework checks use Python standard library modules and do not require the MCP package. CI repeats these integration checks on Linux. These checks establish the local adapter contract; they do not establish a remote deployment, client authorization policy, or field protection outcome.
