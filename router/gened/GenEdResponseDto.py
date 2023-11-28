from pydantic import BaseModel


class GenEdResponseDto(BaseModel):
    Wellness: int
    Entrepreneurship: int
    Thai_Citizen_and_Global_Citizen: int
    Language_and_Communication: int
    Aesthetics: int
    Others: int
