# VCH Dashboard — AI Chat Backend

A lightweight Flask server that proxies requests to the Anthropic API.
The frontend never touches the API key — it stays server-side only.

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Set your API key
```bash
cp .env.example .env
# Open .env and paste your Anthropic API key
```

### 3. Run locally
```bash
ANTHROPIC_API_KEY=your-key python server.py
```
Server starts at `http://localhost:5000`

### 4. Test it
```bash
curl http://localhost:5000/health
# should return: {"status": "ok"}
```

---

## Deploy to Render (free tier — recommended)

1. Push this folder to a GitHub repo (separate from your frontend repo, or a subfolder)
2. Go to [render.com](https://render.com) → New → Web Service
3. Connect your GitHub repo
4. Set:
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `python server.py`
5. Under **Environment Variables**, add:
   - Key: `ANTHROPIC_API_KEY`
   - Value: your key from console.anthropic.com
6. Deploy — Render gives you a public URL like `https://vch-backend.onrender.com`

---

## Update your frontend

Once deployed, open `index.html` and find this line:

```js
const BACKEND_URL = "http://localhost:5000";
```

Change it to your Render URL:

```js
const BACKEND_URL = "https://vch-backend.onrender.com";
```

Commit and push — the AI chat will now work on your public GitHub Pages site.

---

## Security notes

- `.env` is in `.gitignore` — it will never be committed
- The API key only lives on the server, never in the browser
- CORS is enabled so your GitHub Pages frontend can call the backend
