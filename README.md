# Hybrid_RAG_Complete

Hybrid RAG web application with a simple browser UI for:

- Uploading PDF documents
- Asking questions in chat
- Returning generated answers from a backend RAG pipeline
- Showing live UTC time
- Switching UI theme

---

## Overview

This project provides a minimal frontend for a **Hybrid Retrieval-Augmented Generation (RAG)** workflow.  
The UI sends:

1. PDF files to an upload endpoint (`/upload`) for ingestion
2. User questions to a chat endpoint (`/chat`) for answer generation

The backend is expected to index uploaded documents and use retrieval + generation to respond to user prompts.

---

## Current Frontend Capabilities

From `static/script.js`, the frontend supports:

- **Theme switching**
  - `setTheme(theme)` sets `document.body.className = theme`
- **Live UTC clock**
  - `updateClock()` updates an element with id `utcClock` every second
- **PDF upload**
  - `uploadPDF()` reads selected files from input id `pdfFile`
  - Sends files as `FormData` to `POST /upload`
  - Displays response in element id `uploadStatus`
- **Chat messaging**
  - `sendMessage()` sends user text from input id `userInput` to `POST /chat`
  - Appends user + bot messages into `chatBox`

---

## Project Structure

```text
Hybrid_RAG_Complete/
├── static/
│   └── script.js      # Frontend behavior (clock, upload, chat, theme)
├── README.md
└── ...                # Backend files (app/server/routes/indexing logic)
```

> Add your backend file structure here (for example: `app.py`, `main.py`, `routes/`, `services/`, etc.).

---

## API Contract (Expected by Frontend)

### 1) Upload PDFs

- **Endpoint:** `POST /upload`
- **Request type:** `multipart/form-data`
- **Field name:** `file` (can be repeated for multiple files)

**Success response (example):**
```json
{
  "message": "Uploaded and indexed successfully."
}
```

**Error response (example):**
```json
{
  "error": "Upload failed."
}
```

---

### 2) Chat Query

- **Endpoint:** `POST /chat`
- **Request type:** `application/json`

**Request body:**
```json
{
  "query": "What does the uploaded document say about X?"
}
```

**Success response (example):**
```json
{
  "answer": "Based on the uploaded PDFs, ..."
}
```

**Error response (example):**
```json
{
  "error": "Unable to generate answer."
}
```

---

## Required HTML Element IDs

The frontend script expects these IDs to exist in your page:

- `utcClock`
- `pdfFile`
- `uploadStatus`
- `userInput`
- `chatBox`

If any are missing, some features will fail at runtime.

---

## How It Works (Flow)

1. User uploads one or more PDFs.
2. Backend stores and indexes document chunks.
3. User submits a question in chat.
4. Backend retrieves relevant chunks and generates an answer.
5. Frontend displays response in the chat panel.

---

## Setup (Generic)

> Use the setup matching your backend stack (Flask/FastAPI/Node/etc.).  
> Example generic steps:

1. Clone repository
2. Create virtual environment (if Python backend)
3. Install dependencies
4. Start backend server
5. Open app in browser

### Windows example commands (Python backend)

```powershell
git clone <repo-url>
cd Hybrid_RAG_Complete
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

---

## Development Notes

- Frontend currently appends chat messages using `innerHTML`.
  - Consider escaping user input to reduce XSS risk.
- Add error handling around `fetch(...)` for network/server failures.
- Disable submit buttons while requests are pending for better UX.
- Add loading states for upload/chat calls.

---

## Suggested Enhancements

- File upload progress indicator
- Chat streaming responses
- Source citations in bot answers
- Session-based chat history persistence
- Auth + per-user document collections
- Better theme system with saved preference

---

## Troubleshooting

### Upload does nothing
- Verify backend route `POST /upload` exists.
- Confirm `pdfFile` input is present and has selected files.
- Check browser dev tools → Network tab for request errors.

### Chat returns empty/undefined
- Verify backend returns JSON with `answer`.
- Check server logs for retrieval/generation failures.
- Confirm request body uses key `query`.

### Clock not visible
- Ensure an element with id `utcClock` exists in HTML.

---

## Contribution

1. Create a feature branch
2. Make changes
3. Test upload + chat flows
4. Open a pull request with a clear summary

---

## License

Add your project license here (MIT, Apache-2.0, etc.).
