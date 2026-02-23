 # REAL AI Research Assistant 🧠🔍

A powerful, multi‑agent research assistant that autonomously investigates any topic, analyzes data, generates comprehensive reports, and adds proper citations — all through an intuitive Streamlit dashboard. Built with **CrewAI**, **Hugging Face Transformers**, and a suite of real‑world tools.

![Dashboard Preview](https://via.placeholder.com/800x400.png?text=Dashboard+Screenshot+Coming+Soon)

---

## ✨ Features

- **Multi‑agent orchestration** – Five specialized AI agents work in sequence:
  1. **Research Agent** – Searches the web and ArXiv for the latest information.
  2. **Data Analyst** – Extracts numbers, performs statistical analysis, and creates charts.
  3. **Content Synthesizer** – Writes a polished report tailored to your audience.
  4. **Citation Manager** – Formats all sources in APA style with in‑text citations.
  5. **Reviewer Agent** – Quality‑checks the final output.

- **Real‑world tools** – Agents use DuckDuckGo, ArXiv, and custom data‑viz tools to gather and present authentic information.

- **Local LLMs** – Leverages Hugging Face models (e.g., `gpt2-medium`) – no API keys required for many open models.

- **Live progress updates** – The Streamlit dashboard shows each agent’s status in real time.

- **Fully customizable** – Change models, add new tools, or adjust agent prompts to suit your needs.

---

## 🛠️ Tech Stack

- **Python 3.9** (compatible with CrewAI 0.5.0)
- [CrewAI](https://github.com/joaomdmoura/crewai) – Agent orchestration (version 0.5.0)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index) – Local language models
- [Streamlit](https://streamlit.io/) – Web interface
- **Search & tools**: `duckduckgo-search`, `arxiv`, `matplotlib`, `plotly`, `pandas`, `numpy`
- **Environment management**: `python-dotenv`

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 ([download](https://www.python.org/downloads/release/python-3913/))
- Git (optional, for cloning)

### Installation

1. **Clone the repository** (or download the source)
   ```bash
   git clone https://github.com/yourusername/ai-research-assistant.git
   cd ai-research-assistant