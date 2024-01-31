# main.py

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.routers import csv_handler, logging_handler


app = FastAPI()

# Serve the HTML file at the root endpoint
@app.get("/")
def read_root():
    return FileResponse("static/index.html")

# Include your routers
app.include_router(csv_handler.router, prefix="/csv", tags=["csv"])
app.include_router(logging_handler.router, prefix="/logging", tags=["logging"])


# Mount the static files directory to serve HTML
app.mount("/", StaticFiles(directory="static"), name="static")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=2121)
