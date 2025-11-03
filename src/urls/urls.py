from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()


@router.get("/", response_class=FileResponse)
async def home():
    return "src/templates/index.html"
