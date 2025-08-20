# Wordle Clone

A Python-based implementation of the popular word guessing game Wordle with a web frontend.

## Project Structure

```
wordle-clone/
├── frontend/          # HTML/CSS/JS frontend
├── backend/           # Python backend API
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites
- Python
- Web browser

### Installation
1. Clone this repository
2. Set up the backend:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
3. Open `frontend/index.html` in your browser

## Game Rules
- Guess the 5-letter word in 6 attempts
- Green: Letter is correct and in the right position
- Yellow: Letter is in the word but wrong position
- Gray: Letter is not in the word

## Development
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask/FastAPI)
- **API**: RESTful endpoints for game logic