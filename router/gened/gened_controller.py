from fastapi import APIRouter, Header
from router.gened.gened_service import genedService
from router.gened.GenEdResponseDto import GenEdResponseDto

router = APIRouter(prefix="/gened", tags=["gened"])


@router.get("/")
async def gened(
    stdid: str, x_access_token: str | None = Header("x-access-token")
) -> GenEdResponseDto:
    return genedService(stdid, x_access_token)
