# MCP stdio Client

This is a Python client that connects to an MCP (Mud Communication Protocol) server using standard input/output (stdio) as the transport layer.


# Create and activate the Python virtual environment

````shell
python3 -m venv .venv
source .venv/bin/activate
````

# Install Dependencies

````shell
pip install -r requirements.txt
````

# Run the client
- The client sends a hello message and waits for the server response.

````shell
python main.py
````

# Others
- [A Go implementation of the Model Context Protocol (MCP), enabling seamless integration between LLM applications and external data sources and tools](https://github.com/mark3labs/mcp-go)
