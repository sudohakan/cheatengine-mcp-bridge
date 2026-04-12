# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.0.x   | Yes       |

---

## Responsible Use — Process Memory Access

This tool directly reads from and writes to the memory of running processes using Cheat Engine's kernel-level APIs. This capability carries significant responsibility:

**You are responsible for ensuring that:**

- You only use this tool on processes you own or have explicit written permission to analyze.
- You do not use this tool to gain unfair advantages in online multiplayer games where such activity violates the game's Terms of Service.
- You do not use this tool to extract, tamper with, or misuse proprietary data, trade secrets, or personal information from third-party software.
- You comply with all applicable laws in your jurisdiction, including the Computer Fraud and Abuse Act (CFAA) in the US and equivalent laws elsewhere.

**Legitimate use cases this tool is designed for:**

- Offline game modding and research on games you own.
- Reverse engineering your own software for debugging.
- Security research on software you have authorization to test.
- Educational purposes in controlled environments.

The authors provide this tool as-is for legitimate reverse engineering and educational use. Misuse is solely the responsibility of the user.

---

## DBVM / Hypervisor Tools

The DBVM features (`start_dbvm_watch`, `get_physical_address`) operate at the hypervisor level (Ring -1) and interact with physical memory directly. Improper use can cause system instability. These tools require the Cheat Engine DBVM kernel driver to be loaded.

---

## Anti-Cheat Software

This bridge uses hardware debug registers (not software Int3 breakpoints) to reduce detectability, but **no tool can guarantee invisibility to all anti-cheat systems**. Using this tool against games with kernel-level anti-cheat (e.g., Vanguard, EasyAntiCheat kernel mode) may result in bans and could trigger system-level security responses.

Do not use this tool against online games with active anti-cheat protection unless you are conducting authorized security research.

---

## Reporting a Vulnerability

If you discover a security vulnerability in this project (e.g., a way the Python MCP server or Lua bridge could be exploited to execute arbitrary code on a connecting AI agent's host, or a privilege escalation in the Named Pipe implementation), please report it responsibly:

1. **Do not open a public GitHub issue.**
2. Email the maintainer directly or open a [GitHub Security Advisory](https://github.com/sudohakan/cheatengine-mcp-bridge/security/advisories/new).
3. Include: description, reproduction steps, potential impact.
4. Allow reasonable time for a fix before any public disclosure.

---

## Named Pipe Security

The Named Pipe (`\\.\pipe\CE_MCP_Bridge_v99`) is created with default Windows ACLs, meaning any process running as the same user can connect to it. On a shared or multi-user system, be aware that any local process could issue commands to Cheat Engine through this pipe while the bridge is running.

Mitigations:
- Run the bridge only when actively using it. Stop the Lua script when not in use.
- Restrict pipe access via custom DACL if deploying in a sensitive environment (modify `ce_mcp_bridge.lua`).
