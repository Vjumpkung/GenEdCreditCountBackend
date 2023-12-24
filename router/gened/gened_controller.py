from fastapi import APIRouter, Header
from router.gened.gened_service import creditsService, subjectlistService
from router.gened.GenEdResponseDto import GenEdResponseDto
from router.gened.SubjectListResponseDto import SubjectListResponseDto

router = APIRouter(prefix="/gened", tags=["gened"])


@router.get("/")
def getGenEdCredit(
    stdid: str, x_access_token: str | None = Header("X-Access-Token")
) -> GenEdResponseDto:
    return creditsService(stdid, x_access_token)

@router.get("/subjectlist")
def subjectlist(
    stdid: str, x_access_token: str | None = Header("X-Access-Token")
) -> SubjectListResponseDto:
    return subjectlistService(stdid, x_access_token)
