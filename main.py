from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from fastapi.responses import FileResponse

import  login, mydashboard, reg_connect

app = FastAPI()

# Serve static files only from /static
app.mount("/static", StaticFiles(directory="static"), name="static")

# Root should load index.html
@app.get("/")
async def root():
    return FileResponse("static/index.html")

# Include routers
# app.include_router(details.routers)
app.include_router(login.routers)
app.include_router(mydashboard.routers)
app.include_router(reg_connect.routers)
