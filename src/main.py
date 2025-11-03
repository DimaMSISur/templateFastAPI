import uvicorn
from fastapi import FastAPI

from urls.urls import router


app = FastAPI()


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
