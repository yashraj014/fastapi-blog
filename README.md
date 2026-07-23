# FastAPI Blog

A modern, fast, and scalable blogging application built with [FastAPI](https://fastapi.tiangolo.com/), a high-performance Python web framework for building APIs.

## Features

- **Fast Performance**: Built on FastAPI with async support for handling concurrent requests
- **Modern API**: RESTful API design with automatic interactive API documentation
- **Easy to Use**: Simple and intuitive API endpoints for blog management
- **Scalable**: Production-ready architecture suitable for deployment
- **Type Safety**: Full Python type hints for better code quality and IDE support

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Documentation](#api-documentation)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Requirements

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yashraj014/fastapi-blog.git
cd fastapi-blog
```

### 2. Create a Virtual Environment

```bash
# On macOS and Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
# Server Configuration
HOST=127.0.0.1
PORT=8000
DEBUG=True

# Database Configuration
DATABASE_URL=sqlite:///./blog.db

# API Configuration
API_TITLE=FastAPI Blog
API_VERSION=1.0.0
```

## Usage

### Running the Application

```bash
uvicorn main:app --reload
```

The application will be available at `http://127.0.0.1:8000`

### Interactive API Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

### Example API Endpoints

#### Create a Blog Post

```bash
curl -X POST "http://127.0.0.1:8000/api/posts/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My First Blog Post",
    "content": "This is the content of my blog post",
    "author": "Your Name"
  }'
```

#### Get All Posts

```bash
curl "http://127.0.0.1:8000/api/posts/"
```

#### Get a Specific Post

```bash
curl "http://127.0.0.1:8000/api/posts/1"
```

#### Update a Post

```bash
curl -X PUT "http://127.0.0.1:8000/api/posts/1" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Updated Title",
    "content": "Updated content"
  }'
```

#### Delete a Post

```bash
curl -X DELETE "http://127.0.0.1:8000/api/posts/1"
```

## Project Structure

```
fastapi-blog/
├── main.py              # Application entry point
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not in repo)
├── .gitignore           # Git ignore rules
├── README.md            # This file
├── app/
│   ├── __init__.py
│   ├── models.py        # Database models
│   ├── schemas.py       # Pydantic schemas
│   ├── database.py      # Database configuration
│   └── routes/
│       ├── __init__.py
│       └── posts.py     # Post endpoints
└── tests/
    └── test_posts.py    # API tests
```

## API Documentation

### POST /api/posts/
Create a new blog post.

**Request Body:**
```json
{
  "title": "string",
  "content": "string",
  "author": "string"
}
```

**Response:** `201 Created`

### GET /api/posts/
Get all blog posts with pagination support.

**Query Parameters:**
- `skip` (int): Number of items to skip (default: 0)
- `limit` (int): Number of items to return (default: 10)

**Response:** `200 OK`

### GET /api/posts/{post_id}
Get a specific blog post by ID.

**Response:** `200 OK`

### PUT /api/posts/{post_id}
Update a blog post.

**Request Body:**
```json
{
  "title": "string",
  "content": "string"
}
```

**Response:** `200 OK`

### DELETE /api/posts/{post_id}
Delete a blog post.

**Response:** `204 No Content`

## Development

### Install Development Dependencies

```bash
pip install -r requirements-dev.txt
```

### Run Tests

```bash
pytest
```

### Run Tests with Coverage

```bash
pytest --cov=app tests/
```

### Code Formatting

```bash
black .
```

### Linting

```bash
flake8 .
pylint app/
```

## Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork the Repository**: Click the "Fork" button on GitHub
2. **Create a Feature Branch**: 
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make Your Changes**: Implement your feature or bug fix
4. **Write Tests**: Ensure your changes are covered by tests
5. **Commit Your Changes**:
   ```bash
   git commit -m "Add: brief description of changes"
   ```
6. **Push to Your Fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Submit a Pull Request**: Describe your changes in detail

### Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use type hints for all functions
- Write meaningful commit messages
- Add docstrings to functions and classes

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For issues, questions, or suggestions, please [open an issue](https://github.com/yashraj014/fastapi-blog/issues) on GitHub.

## Changelog

### Version 1.0.0
- Initial release
- Basic CRUD operations for blog posts
- Interactive API documentation

---

**Made with ❤️ by [yashraj014](https://github.com/yashraj014)**
