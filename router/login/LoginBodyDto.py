from pydantic import BaseModel


class LoginBodyDto(BaseModel):
    username: str
    password: str
