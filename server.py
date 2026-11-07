import os
from pathlib import Path
from fastmcp import FastMCP

# Initialize the FastMCP server with a name
# This name identifies your server to any MCP host client (i.e. Claude Desktop)
mcp = FastMCP("Local File Inspector")

# Define a safe root directory (e.g. the current working directory)
# so the LLM can't go through files outside your project boundary
SAFE_ROOT = Path().resolve()

# Anchor it explicitly to the current directory where the script runs:
BASE_DIR = Path(".").resolve()

@mcp.tool()
def list_workspace_files() -> list[str]:
    '''List all text and code files in the workscape directory.'''

    files = []
    for path in BASE_DIR.rglob("*"):
        if path.is_file() and not any(part.startswith('.') for part in path.parts):
            files.append(str(path.relative_to(BASE_DIR)))

    return files

@mcp.tool()
def read_file_content(file_path: str, max_lines: int=100) -> str:
    '''Read the contents of a specific file within the workspace safely.'''
    target_path = (BASE_DIR / file_path).resolve()

    # Security check: Ensure the file stays inside our workspace directory
    if not str(target_path).startswith(str(BASE_DIR)):
        return "Error: Access denied. Path is outside the workspace root."

    if not target_path.exists():
        return f"Error: File '{file_path} does not exist."

    try:
        with open(target_path, "r", encoding="utf-8") as f:
            lines = [f.readline() for _ in range(max_lines)]
            content = "".join(lines)

            if f.readline():
                content += "\n[Note: output truncated at max_lines limit]"
        return content
    except Exception as e:
        return f"Error reading file: {str(e)}"

if __name__ == "__main__":
    # Run the server using standard input/output (stdio) transport
    # This is how local AI desktop clinets communicate with local python scripts securely

    mcp.run(transport="stdio")