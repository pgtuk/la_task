
import asyncio
import os

from starlette.applications import Starlette
from starlette.templating import Jinja2Templates
import uvicorn

import processor
from video import Video


app = Starlette()
templates = Jinja2Templates(directory='src/templates')
VIDEOS_DIR = 'videos'


@app.route('/')
def homepage(request):

    return templates.TemplateResponse(
        'index.html',
        {
            'request': request,
            'videos': os.listdir(VIDEOS_DIR)
        }
    )


@app.websocket_route("/ws")
async def video_stream(ws):
    await ws.accept()

    video_name = await ws.receive_text()
    if video_name not in os.listdir(VIDEOS_DIR):
        await ws.close()
        return 

    with Video(f'{VIDEOS_DIR}/{video_name}') as video:
        f_count = 1
        for frame in video.frames():
            r_count = processor.rectangles_count()

            processed_frame = processor.add_rectangles(frame, r_count)
            jpeg = processor.to_jpeg(processed_frame)
            
            await ws.send_bytes(jpeg.tobytes())
            await ws.send_json({
                'f_count': f_count,
                'r_count': r_count,
            })
            await asyncio.sleep(1/video.fps)

            f_count += 1

    await ws.close()

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
