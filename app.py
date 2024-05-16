from fastapi import FastAPI
from starlette.responses import FileResponse 
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/ui")
async def read_index():
    return FileResponse('static/index.html')

@app.get("/")
async def root():
    return {"message": "Hello World"}