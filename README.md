# Study Assistant ChatBot
A simple FastAPI-based chatbot designed to answer study-related questions using natural language processing (NLP) and vector similarity search with FAISS. The chatbot retrieves answers from a predefined educational content file based on user queries.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Contributing](#contributing)

## Features
- Accepts text questions via a web form or API endpoint.
- Uses Sentence Transformers for text embeddings and FAISS for efficient similarity search.
- Returns structured JSON responses with questions, answers, and source passages.
- Includes a simple HTML interface for user interaction.

## Prerequisites
- Python 3.11 or higher
- Git (for version control)

## Installation
1. **Clone the Repository**:
```bash
git clone https://github.com/leonardo0231/study-assistant.git
cd study-assistant
```
2. **Set Up a Virtual Environment**:
```bash
python -m venv env
source env/bin/activate
```
3. **Install Dependencies**:
```bash
pip install -r requirements.txt
```

## Configuration
create a `.env` file in te project root(`study-assistant/`) to store configuration variables:
```plaintext
# .env
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
CONTENT_FILE_PATH=data/sample_content.txt
```
- `EMBEDDING_MODEL`: The Sentence Transformers model for generating embeddings
- `CONTENT_FILE_PATH`: Path to the text file containing educational content


## Usage
1. Run the Application:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
2. Access the API Documentation:
- Visit http://localhost:8000/docs to explore the interactive Swagger UI.
- Test the /ask endpoint with a JSON payload:
```json
{
  "question": "سلول گیاهی چیست؟"
}
```
- Expected response:
```json
{
  "question": "سلول گیاهی چیست؟",
  "answer": "سلول‌های گیاهی دارای دیواره سلولی و کلروپلاست هستند و در فتوسنتز نقش دارند.",
  "source_passage": "سلول‌های گیاهی دارای دیواره سلولی و کلروپلاست هستند و در فتوسنتز نقش دارند."
}
```

## API Documentation
- GET /: Serves a simple HTML form to submit questions.
- POST /ask: Accepts a question and returns a response.
- - Request (Form): Submit via the web form with question as a text input.
- - Request (JSON):
```json
{
  "question": "string"
}
```
- - Response:
```json
{
  "question": "string",
  "answer": "string",
  "source_passage": "string"
}
```
- - Status Codes:
- - - `200 OK`: Successful response.
- - - `422 Unprocessable Entity`: Invalid request data.

## Testing
1. Run Tests:
```bash
pytest tests/
```
- The tests/test_api.py file contains unit tests for the /ask endpoint.
2. Add Test Data:
- Ensure the data/sample_content.txt file is populated for tests to work.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make changes and commit (`git commit -m "Add your message"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.
