# Use an official Python runtime as a parent image
FROM python:3.12-slim-bookworm

# The installer requires curl (and certificates) to download the release archive
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"

# Set the working directory
WORKDIR /code

# Copy the pyproject.toml and uv.lock files
COPY pyproject.toml uv.lock /code/

# Install the pipeline
COPY app/pipelines/en_core_web_lg-3.8.0-py3-none-any.whl /tmp/
RUN pip install /tmp/en_core_web_lg-3.8.0-py3-none-any.whl

# Install dependencies using uv
RUN uv sync --frozen || true

# Copy the HTML template
COPY ./app/templates /code/templates

# Copy the application code
COPY ./app /code/app

# Command to run the application
CMD ["uv", "run", "fastapi", "run", "app/Assignment_1.py", "--port", "80"]