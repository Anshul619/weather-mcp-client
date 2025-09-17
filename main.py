import subprocess, json, threading, shlex, os, time
from dotenv import load_dotenv

load_dotenv()
MCP_SERVER_CMD = os.getenv("MCP_SERVER_CMD")
server_cmd = shlex.split(MCP_SERVER_CMD)

def start_server():
    return subprocess.Popen(
        server_cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )

def read_logs(proc):
    for line in proc.stderr:
        if line.strip():
            print("[SERVER LOG]", line.strip())

def send(proc, msg):
    proc.stdin.write(json.dumps(msg) + "\n")
    proc.stdin.flush()

def recv(proc, timeout=10):
    start = time.time()
    while True:
        if proc.poll() is not None:
            return None
        if time.time() - start > timeout:
            return None
        line = proc.stdout.readline()
        if line:
            try:
                return json.loads(line.strip())
            except:
                continue

def main():
    proc = start_server()
    threading.Thread(target=read_logs, args=(proc,), daemon=True).start()

    # Call get_weather tool
    tool_call = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {"name": "get_weather", "args": {"city": "London"}}
    }

    send(proc, tool_call)
    resp = recv(proc, timeout=15)
    if resp:
        print("[WEATHER RESPONSE]", resp)
    else:
        print("[ERROR] No response received")

    proc.terminate()
    proc.wait()

if __name__ == "__main__":
    main()
