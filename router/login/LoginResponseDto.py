from pydantic import BaseModel


class LoginResponseDto(BaseModel):
    code: str
    message: str
    accesstoken: str
    renewtoken: str
    user: dict
    cache: bool
