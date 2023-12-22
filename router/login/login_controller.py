from fastapi import APIRouter
from router.login.LoginBodyDto import LoginBodyDto
from router.login.login_service import loginService

router = APIRouter(prefix="/login", tags=["login"])


@router.post("/")
async def login(loginBodyDto: LoginBodyDto):
    return await loginService(loginBodyDto)
