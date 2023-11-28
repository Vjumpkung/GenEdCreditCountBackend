from fastapi import APIRouter
from router.login.LoginBodyDto import LoginBodyDto
from router.login.login_service import loginService
from router.login.LoginResponseDto import LoginResponseDto

router = APIRouter(prefix="/login", tags=["login"])


@router.post("/")
async def login(loginBodyDto: LoginBodyDto) -> LoginResponseDto:
    return await loginService(loginBodyDto)
