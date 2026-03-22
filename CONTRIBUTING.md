# Contributing

Thank you for your interest in contributing to Cheat Engine MCP Bridge.

---

## Development Setup

### Prerequisites

- Windows 10/11
- Python 3.12+
- Cheat Engine 7.x
- A target process to test against (any game or application)
- Git

### Python Environment

```bash
cd MCP_Server
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### Running Tests

Ensure Cheat Engine is running with `ce_mcp_bridge.lua` loaded and a process attached, then:

```bash
python MCP_Server/test_mcp.py
```

Expected: 36/37 tests passing. The one skipped test (`generate_signature`) is intentionally skipped because it performs a full memory scan and can block for several minutes.

### Running the MCP Server Manually

```bash
python MCP_Server/mcp_cheatengine.py
```

The server communicates over stdio using the MCP protocol. Use an MCP client (Claude Desktop, Cursor, or the MCP Inspector) to interact with it.

---

## Project Structure

```
MCP_Server/
  mcp_cheatengine.py    # Python MCP server — add new tools here
  ce_mcp_bridge.lua     # Lua bridge — add new command handlers here
  test_mcp.py           # Tests — add test cases here
  requirements.txt

AI_Context/             # Documentation for AI agents — keep in sync with code
```

---

## Adding a New Tool

New tools require changes in two files:

### 1. `ce_mcp_bridge.lua` — Add a command handler

Find the section matching the tool's category and add a handler in the `commandHandlers` table:

```lua
commandHandlers["my_new_tool"] = function(params)
    local address = parseAddress(params.address)
    if not address then return { success = false, error = "Invalid address" } end
    -- ... implementation ...
    return { success = true, result = value }
end
```

### 2. `mcp_cheatengine.py` — Expose it as an MCP tool

```python
@mcp.tool()
def my_new_tool(address: str, param: int = 10) -> str:
    """One-line description shown to AI agents."""
    return format_result(ce_client.send_command("my_new_tool", {
        "address": address,
        "param": param
    }))
```

### 3. `test_mcp.py` — Add a test

Add a test case in the appropriate category block.

### 4. `AI_Context/MCP_Bridge_Command_Reference.md` — Document it

Add a section with: purpose, parameters table, return JSON example, and any usage notes.

---

## Code Standards

- **Python**: Follow PEP 8. Keep tool functions minimal — they are thin wrappers. All logic lives in Lua.
- **Lua**: Use `pcall` for all CE API calls that might fail. Always return `{ success = false, error = "..." }` on error, never nil or unhandled exceptions.
- **Error handling**: Every command handler must return a valid JSON-serializable table. Never let an unhandled error propagate to the pipe.
- **Anti-cheat safety**: Do not add software breakpoints (0xCC / Int3). Hardware debug registers only.
- **Architecture**: Always use `readPointer()` for pointer operations — never hardcode 4 or 8 bytes.

---

## Pull Request Process

1. Fork the repository.
2. Create a branch: `feat/my-tool-name` or `fix/description`.
3. Make your changes following the standards above.
4. Run the test suite and confirm no regressions.
5. Update `CHANGELOG.md` under a new `[Unreleased]` section.
6. Open a PR with a clear description of what the tool does and why it is useful.

---

## Reporting Bugs

Open a GitHub issue with:
- Cheat Engine version
- Target process architecture (32-bit / 64-bit)
- DBVM active or not
- Exact tool call and parameters
- Full error message or unexpected behavior description

For security issues, see [SECURITY.md](SECURITY.md) — do not open a public issue.
