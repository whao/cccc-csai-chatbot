# Use Python 3.13
FROM ghcr.io/astral-sh/uv:python3.13-alpine
# Set the working directory
WORKDIR /app
# Copy the requirements file into the container
COPY app.py pyproject.toml /app/
# Install the dependencies
RUN uv sync

EXPOSE 8501
# Run the Streamlit app

CMD ["uv", "run", "streamlit", "run", "app.py"]