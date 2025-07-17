# 🌍 Language Detection API

A simple and containerized FastAPI microservice to detect the language of a given text using `langdetect`.

---

## 📦 Features

- 🔍 Detects language of input text using [`langdetect`](https://pypi.org/project/langdetect/)
- 🚀 Built with FastAPI
- 🐳 Dockerized with dev & prod profiles
- 🔄 Live-reload support in development
- 📄 Interactive API docs with Swagger

---

## 🔧 Getting Started

### 1. 📁 Clone the Repository

```bash
git clone https://github.com/your-username/language-detect-api.git
cd language-detect-api
```

---

### 2. ⚙️ Local Development with Docker

#### ✅ Dev Mode (Auto Reload)

```bash
./run.sh dev
```

This mounts your code and enables hot reload via `uvicorn --reload`. Accessible at [http://localhost:8000/docs](http://localhost:8000/docs)

#### 🚀 Prod Mode

```bash
./run.sh prod
```

Runs the production build without auto-reload.

---

### 3. 🐳 Manual Docker Commands

#### Build the image

```bash
docker build -t language-detect-api .
```

#### Run the container

```bash
docker run -p 8000:8000 language-detect-api
```

---

## 📂 API Endpoints

- **`POST /detect`** – Detect language from text
- **`GET /`** – Root endpoint
- **`/docs`** – Swagger UI
- **`/redoc`** – ReDoc documentation

---

## 🧪 Example Request

```bash
curl -X POST http://localhost:8000/detect \
  -H "Content-Type: application/json" \
  -d '{"text": "Bonjour le monde"}'
```

### Response

```json
{
  "language": "fr"
}
```

---

## 🧰 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [langdetect](https://pypi.org/project/langdetect/)
- [Docker](https://www.docker.com/)

---

## 📄 License

MIT

---
