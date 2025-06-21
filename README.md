# CCCC CSAI Chatbot

A ChatGPT-like clone built with Streamlit and OpenAI's API, using UV for fast Python package management.

## Features

- 🤖 **OpenAI Integration**: Powered by GPT-4o-mini for intelligent conversations
- 💬 **Chat Interface**: Clean, intuitive Streamlit-based chat UI
- 🔄 **Streaming Responses**: Real-time response streaming for better user experience
- 💾 **Session Memory**: Maintains conversation history within the session
- ⚡ **Fast Setup**: Uses UV for lightning-fast dependency management

## Prerequisites

- Python 3.13+ OR Docker
- [UV](https://docs.astral.sh/uv/) package manager (for local development)
- OpenAI API key

## Installation

### Option 1: Local Development with UV

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

### Option 2: Docker Deployment

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd cccc-csai-chatbot
   ```

2. **Set up your OpenAI API key**
   
   Create a `.streamlit/secrets.toml` file:

   ```toml
   OPENAI_API_KEY = "your-openai-api-key-here"
   ```

3. **Run with Docker Compose**

   ```bash
   docker-compose -f docker-compose.dev.yml up --build
   ```

## Usage

### Local Development

1. **Start the application**

   ```bash
   uv run streamlit run app.py
   ```

2. **Open your browser**
   
   Navigate to `http://localhost:8501`

### Docker Deployment

1. **Application should already be running** (if you used docker-compose)
   
   Navigate to `http://localhost:8501`

2. **Or run manually with Docker**

   ```bash
   docker build -t cccc-csai-chatbot .
   docker run -p 8501:8501 -v $(pwd)/.streamlit:/app/.streamlit cccc-csai-chatbot
   ```

3. **Start chatting!**
   
   Type your message in the chat input and press Enter to start a conversation with the AI.

## Project Structure

```text
cccc-csai-chatbot/
├── app.py                    # Main Streamlit application
├── pyproject.toml            # Project dependencies and metadata
├── uv.lock                   # Locked dependency versions
├── Dockerfile                # Docker container configuration
├── docker-compose.dev.yml    # Docker Compose for development
├── .streamlit/
│   └── secrets.toml          # OpenAI API key (not tracked)
├── .gitignore                # Git ignore rules
└── README.md                 # This file
```

## Configuration

The chatbot uses GPT-4o-mini by default. You can modify the model in `app.py` by changing the `openai_model` session state variable.

## Dependencies

- **streamlit**: Web framework for the chat interface
- **openai**: Official OpenAI Python client for API integration

## Docker

This project includes Docker support for easy deployment:

- **Dockerfile**: Uses the official UV Python 3.13 Alpine image for lightweight containers
- **docker-compose.dev.yml**: Development configuration with volume mounting for secrets
- **Volume Mounting**: The `.streamlit` directory is mounted to persist configuration

### Docker Benefits

- 🐳 **Containerized Deployment**: Consistent environment across different systems
- ⚡ **Fast Builds**: Leverages UV for rapid dependency installation
- 🔧 **Development Mode**: Volume mounting for easy configuration updates
- 🚀 **Production Ready**: Alpine-based image for minimal footprint

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
