from pydantic import BaseModel
from typing import List

class SubjectDto(BaseModel):
    subject_code: str
    subject_name_en: str
    subject_name_th: str
    credits: int

class SubjectListResponseDto(BaseModel):
    Wellness: List[SubjectDto]
    Entrepreneurship: List[SubjectDto]
    Thai_Citizen_and_Global_Citizen: List[SubjectDto]
    Language_and_Communication: List[SubjectDto]
    Aesthetics: List[SubjectDto]
    Others: List[SubjectDto]