# CCCC CSAI Chatbot

A ChatGPT-like clone built with Streamlit and OpenAI's API, using UV for fast Python package management.

## Features

- 🤖 **OpenAI Integration**: Powered by GPT-4o-mini for intelligent conversations
- 💬 **Chat Interface**: Clean, intuitive Streamlit-based chat UI
- 🔄 **Streaming Responses**: Real-time response streaming for better user experience
- 💾 **Session Memory**: Maintains conversation history within the session
- ⚡ **Fast Setup**: Uses UV for lightning-fast dependency management

## Prerequisites

- Python 3.13+
- [UV](https://docs.astral.sh/uv/) package manager
- OpenAI API key

## Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd cccc-csai-chatbot
   ```

2. **Install dependencies using UV**

   ```bash
   uv sync
   ```

3. **Set up your OpenAI API key**
   
   Create a `.streamlit/secrets.toml` file:

   ```toml
   OPENAI_API_KEY = "your-openai-api-key-here"
   ```

## Usage

1. **Start the application**

   ```bash
   uv run streamlit run app.py
   ```

2. **Open your browser**
   
   Navigate to `http://localhost:8501`

3. **Start chatting!**
   
   Type your message in the chat input and press Enter to start a conversation with the AI.

## Project Structure

```text
cccc-csai-chatbot/
├── app.py                 # Main Streamlit application
├── pyproject.toml         # Project dependencies and metadata
├── uv.lock               # Locked dependency versions
├── .streamlit/
│   └── secrets.toml      # OpenAI API key (not tracked)
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## Configuration

The chatbot uses GPT-4o-mini by default. You can modify the model in `app.py` by changing the `openai_model` session state variable.

## Dependencies

- **streamlit**: Web framework for the chat interface
- **openai**: Official OpenAI Python client for API integration

## Development

This project uses UV for dependency management, which provides:

- ⚡ Fast dependency resolution and installation
- 🔒 Reproducible builds with `uv.lock`
- 🐍 Automatic Python version management

To add new dependencies:

```bash
uv add package-name
```

## License

[Add your license here]

## Contributing

[Add contributing guidelines here]