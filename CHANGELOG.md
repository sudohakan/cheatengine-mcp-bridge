# Changelog

All notable changes documented here. Format: [Keep a Changelog](https://keepachangelog.com).

## [1.0.0] - 2026-03-22

### Added

- `ce_mcp_bridge.lua` — Cheat Engine Lua bridge v11.4.0 with Named Pipe server (pipe: `CE_MCP_Bridge_v99`)
- `mcp_cheatengine.py` — Python MCP server exposing 40+ reverse engineering tools via FastMCP
- `test_mcp.py` — Test suite with 36/37 passing tests covering all tool categories
- Full 32-bit and 64-bit target process support — all operations auto-adapt via `getArchInfo()` and `readPointer()`
- **Process & Modules**: `get_process_info`, `enum_modules`, `get_thread_list`, `get_symbol_address`, `get_address_info`, `get_rtti_classname`
- **Memory Read**: `read_memory`, `read_integer`, `read_string`, `read_pointer`, `read_pointer_chain`, `checksum_memory`
- **Memory Write**: `write_integer`, `write_memory`, `write_string`
- **Pattern Scanning**: `aob_scan`, `scan_all`, `next_scan`, `get_scan_results`, `search_string`, `generate_signature`
- **Memory Regions**: `get_memory_regions`, `enum_memory_regions_full`
- **Disassembly & Analysis**: `disassemble`, `get_instruction_info`, `find_function_boundaries`, `analyze_function`, `find_references`, `find_call_references`, `dissect_structure`
- **Hardware Breakpoints**: `set_breakpoint`, `set_data_breakpoint`, `get_breakpoint_hits`, `remove_breakpoint`, `list_breakpoints`, `clear_all_breakpoints`
- **DBVM Hypervisor (Ring -1)**: `get_physical_address`, `start_dbvm_watch`, `poll_dbvm_watch`, `stop_dbvm_watch`
- **Scripting**: `evaluate_lua`, `auto_assemble`, `ping`
- Windows CRLF fix — monkey-patches MCP SDK's `stdio_server` to use `newline='\n'` on Win32, preventing `"invalid trailing data"` errors
- Auto-reconnect on Named Pipe failure with configurable retry count
- Zombie resource cleanup on Lua script reload — prevents orphaned hardware breakpoints and DBVM watches from surviving CE restarts
- `AI_Context/AI_Guide_MCP_Server_Implementation.md` — architecture guide and best practices for AI agents
- `AI_Context/MCP_Bridge_Command_Reference.md` — full command reference with parameters, return shapes, and workflow examples
- `AI_Context/CE_LUA_Documentation.md` — Cheat Engine Lua API reference for development
