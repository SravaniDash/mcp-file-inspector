# Local File Inspector MCP Server

A Model Context Protocol (MCP) server built with **FastMCP** that provides safe, read-only file system inspection capabilities to LLMs and MCP clients.

## Features & Tools

This server exposes two core tools decorated for automatic schema generation:

1. **`list_workspace_files`**
   - **Description:** Enumerates all text and code files recursively within the workspace directory, filtering out hidden system files.
   - **Parameters:** None

2. **`read_file_content`**
   - **Description:** Safely reads the contents of a specific file within the workspace boundary up to a line limit.
   - **Parameters:**
     - `file_path` (str): Relative path to the target file.
     - `max_lines` (int, default=100): Maximum number of lines to read.

## Security Boundaries
To ensure safe operation, the server includes a strict directory containment check (`BASE_DIR`). Any attempts to traverse outside the workspace root are automatically blocked.

---

## Getting Started & Usage

### Prerequisites
Make sure you have Python and `uv` installed.

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/SravaniDash/mcp-file-inspector.git](https://github.com/SravaniDash/mcp-file-inspector.git)
   cd mcp-file-inspector