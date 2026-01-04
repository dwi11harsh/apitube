# ApiTube - FastAPI Server

A FastAPI server for YouTube transcript and analytics API using `uv` as the package manager.

## Setup

This project uses [uv](https://github.com/astral-sh/uv) for fast, reliable Python package management.

### Prerequisites

- Python 3.12+
- uv package manager

### Installation

1. Clone the repository
2. Install dependencies:
```bash
uv sync
```

## Running the Server

### Development Mode

Run the server with auto-reload:

```bash
uv run python main.py
```

Or using uvicorn directly:

```bash
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- Main API: http://localhost:8000
- Interactive API docs: http://localhost:8000/docs
- Alternative API docs: http://localhost:8000/redoc



## Development

### Adding Dependencies

```bash
uv add <package-name>
```

### Adding Dev Dependencies

```bash
uv add --dev <package-name>
```