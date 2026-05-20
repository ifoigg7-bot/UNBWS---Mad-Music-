from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# ТВОЯ ССЫЛКА С ЮТУБА
YOUTUBE_URL = "https://youtu.be/nsr0xhrWrMI?si=KwATIcKw37XujraB"

# Достаём ID видео из ссылки
video_id = YOUTUBE_URL.split("/")[-1].split("?")[0]

html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Mad Music Radio</title>
    <style>
        body {{
            font-family: Arial;
            text-align: center;
            padding: 50px;
            background: #0a0a0a;
            color: white;
        }}
        iframe {{
            width: 80%;
            height: 500px;
            border-radius: 12px;
            margin-top: 20px;
        }}
        h1 {{ color: #ff0000; }}
        p {{ margin-top: 20px; opacity: 0.7; }}
    </style>
</head>
<body>
    <h1>🎵 MAD MUSIC RADIO 24/7 🎵</h1>
    <iframe 
        src="https://www.youtube.com/embed/{video_id}?autoplay=1&loop=1&playlist={video_id}" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen>
    </iframe>
    <p>Радио работает 24/7 — видео повторяется автоматически</p>
</body>
</html>
"""

@app.get("/")
async def root():
    return HTMLResponse(content=html_content)
