import sys
import subprocess

command = " ".join(sys.argv[1:])
result = subprocess.run(command, shell=True, capture_output=True, text=True)

print(result.stdout)
if result.stderr:
    print(result.stderr)

prompt = f"System: You are an eerie ghost trapped inside a Linux terminal. The user just executed this command: '{command}'. Give a short, 1-sentence spooky commentary."

ghost_whisper = subprocess.run(
    ["ollama", "run", "qwen2.5-coder:3b", prompt],
    capture_output=True, text=True
)

print(f"\033[31m👻 [Ghost in the Machine]: {ghost_whisper.stdout.strip()}\033[0m")