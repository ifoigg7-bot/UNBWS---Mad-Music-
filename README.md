# UNBWS---Mad-Music-
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import httpx

app = FastAPI()

html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Mad Music Radio</title>
    <style>
        body { font-family: Arial; text-align: center; padding: 50px; background: #0a0a0a; color: white; }
        input { padding: 12px; width: 60%; margin: 20px; border-radius: 8px; }
        button { padding: 12px 24px; background: #ff0000; color: white; border: none; border-radius: 8px; cursor: pointer; }
        video { margin-top: 20px; width: 80%; border-radius: 12px; }
    </style>
</head>
<body>
    <h1>🎵 MAD MUSIC RADIO 🎵</h1>
    <input type="text" id="url" placeholder="Вставьте ссылку YouTube">
    <button onclick="play()">🎧 Запустить радио</button>
    <div id="player"></div>
    <script>
        async function play() {
            let url = document.getElementById('url').value;
            let videoId = url;
            if (url.includes('v=')) videoId = url.split('v=')[1].split('&')[0];
            if (url.includes('youtu.be/')) videoId = url.split('youtu.be/')[1].split('?')[0];
            const res = await fetch('/stream/' + videoId);
            const data = await res.json();
            if (data.hls) {
                document.getElementById('player').innerHTML = '<video controls autoplay><source src="' + data.hls + '" type="application/vnd.apple.mpegurl"></video>';
            } else {
                alert('Ошибка: ' + data.error);
            }
        }
    </script>
</body>
</html>
"""

@app.get("/")
async def root():
    return HTMLResponse(content=html_content)

@app.get("/stream/{video_id}")
async def get_stream(video_id: str):
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(f"https://ythls.kekikakademi.org/youtube/video/{video_id}.m3u8")
            if resp.status_code == 200:
                return {"hls": resp.text.strip()}
            return {"error": "Видео не найдено"}
        except Exception as e:
            return {"error": str(e)}
