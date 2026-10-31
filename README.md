
# 👻 Ghost Terminal (Shell Auto-Possessor)

### **What I Built**

Ghost Terminal is an offline CLI wrapper that runs locally on your machine, "possessing" standard shell sessions. Whenever a command is executed—whether a successful file check, a failed build, or a force push—a lightweight, locally served open-weight model receives the exit status and command string and injects eerie, contextual terminal commentary into standard output.

---

### **How It Works**

1. **Local Model Runtime:** Powered by `ollama` running the open-weight 3B-parameter coding model `qwen2.5-coder:3b`.
2. **Execution Hook:** A lightweight Python execution wrapper traps terminal commands, preserves standard output streams, and passes execution metrics into local IPC inference.
3. **Ghost Ingestion Engine:** The local LLM processes the shell action in real time and streams a single-line, spooky commentary styled with terminal escape sequences without touching external networks.


---

### **Why Open Innovation & Open Weights Matter**

* **Offline & Low Latency:** Running an open-weight model directly via `ollama`/`llama.cpp` removes API latency and network dependencies. It can operate with internet access disabled after the model is downloaded.
* **Complete Data & System Privacy:** Shell history contains internal directory paths, repo structure, environment parameters, and sensitive flags. Transmitting shell execution logs to cloud-hosted proprietary endpoints is a major security risk. Open-source models keep system telemetry strictly on local hardware.
* **No Usage Fees:** Using open weights avoids per-token costs and provider rate limits, though local inference still uses system resources and electricity.
* **No Service Lock-in:** Open models ensure the tool remains functional indefinitely on local hardware without depending on third-party SaaS availability or API deprecations.

---

### **Tech Stack**

* **LLM Engine:** Ollama / `Qwen2.5-Coder-3B` (Open-Weight)
* **Core Logic:** Python 3 (Standard Library / Zero Heavy Dependencies)
* **Shell Integration:** Bash / Zsh alias hooks

---

### **Quickstart / How to Run**

1. Install [Ollama](https://ollama.com), then pull the model locally:
```bash
ollama run qwen2.5-coder:3b
```

2. Clone the repository:
```bash
git clone https://github.com/sumeet57/ghostterminal
```

3. Add the alias to your `.bashrc` or `.zshrc` (adjust the path as needed):
```bash
alias g="python3 /ghostterminal/ghost.py"
```


