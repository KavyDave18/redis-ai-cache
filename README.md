# Redis AI Cache

A high-performance Redis-powered caching system built with FastAPI. The project demonstrates how caching can significantly reduce response times by storing expensive AI responses in Redis and serving repeated requests directly from memory.

## Overview

In many AI-powered applications, the same question may be asked multiple times. Calling an AI model repeatedly for identical queries increases latency and computational cost.

This project solves that problem using Redis caching. The first request generates a response and stores it in Redis with a configurable Time-To-Live (TTL). Subsequent requests for the same query are served directly from Redis, reducing response times from seconds to milliseconds.

---

## Features

* Redis-Based Response Caching
* FastAPI Backend
* Configurable Cache TTL
* Cache Hit/Miss Tracking
* Response Time Monitoring
* Cache Invalidation Endpoint
* REST API Architecture
* Modular Project Structure

---

## Tech Stack

### Backend

* Python
* FastAPI
* Uvicorn

### Caching

* Redis

### Development Tools

* Virtual Environment (venv)
* VS Code
* Git
* GitHub

---

## Project Architecture

```text
Client
   │
   ▼
FastAPI API
   │
   ▼
Check Redis Cache
   │
   ├──────── Cache Hit
   │              │
   │              ▼
   │      Return Cached Response
   │
   ▼
Cache Miss
   │
   ▼
Generate Response
   │
   ▼
Store In Redis
   │
   ▼
Return Response
```

---

## API Endpoints

### Ask Question

```http
POST /ask
```

Request:

```json
{
  "question": "What is Redis?"
}
```

Response (Cache Miss):

```json
{
  "cached": false,
  "answer": "AI Response: What is Redis?",
  "response_time_ms": 2002.14
}
```

Response (Cache Hit):

```json
{
  "cached": true,
  "answer": "AI Response: What is Redis?",
  "response_time_ms": 1.32
}
```

---

### Cache Statistics

```http
GET /stats
```

Response:

```json
{
  "total_requests": 10,
  "cache_hits": 6,
  "cache_misses": 4,
  "hit_rate": 60.0
}
```

---

### Delete Cache

```http
DELETE /cache/{question}
```

Response:

```json
{
  "success": true,
  "message": "Cache deleted"
}
```

---

## Performance Comparison

| Scenario   | Response Time |
| ---------- | ------------- |
| Cache Miss | ~2000 ms      |
| Cache Hit  | ~1-5 ms       |

Performance improvement:

```text
~400x to 2000x faster
```

depending on workload and hardware.

---

## Screenshot Section

### API Documentation

### Cache Miss Example

<img width="1061" height="450" alt="image" src="https://github.com/user-attachments/assets/a5bf56f7-438f-4495-a6b0-666e6ebbfcb3" />


```text
docs/screenshots/cache-miss.png
```

Expected:

```json
{
  "cached": false,
  "response_time_ms": 2000
}
```

---

### Cache Hit Example

<img width="1063" height="455" alt="image" src="https://github.com/user-attachments/assets/e1eb066d-14e7-4bca-a28c-c9627d579858" />


```text
docs/screenshots/cache-hit.png
```

Expected:

```json
{
  "cached": true,
  "response_time_ms": 1
}
```

---


### Statistics Endpoint

<img width="1059" height="443" alt="image" src="https://github.com/user-attachments/assets/f4302303-054a-4bd1-9c5a-db36b6842ee3" />


```text
docs/screenshots/stats-endpoint.png
```

---

## Project Structure

```text
redis-ai-cache/
│
├── app/
│   ├── config/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── tests/
│
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start Redis:

```bash
redis-server
```

Run FastAPI:

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

## Learning Outcomes

Through this project I learned:

* Redis Fundamentals
* Caching Strategies
* Cache Hit and Cache Miss Concepts
* Time-To-Live (TTL)
* Cache Invalidation
* FastAPI Development
* API Design
* Backend Performance Optimization
* Response Time Monitoring
* Git and GitHub Workflow

---

## Future Improvements

* Real LLM Integration (OpenAI / Ollama)
* Redis Background Job Queue
* Docker Deployment
* Cache Analytics Dashboard
* Distributed Caching
* Rate Limiting with Redis
* Multi-Level Caching

---

## Author

Kavy Dave

Computer Science Engineering Student | Backend Development | Machine Learning | AI Systems
