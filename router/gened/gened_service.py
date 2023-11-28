import requests
import json
import re

maximumCredits = {
    "Wellness": 6,
    "Entrepreneurship": 3,
    "Thai_Citizen_and_Global_Citizen": 5,
    "Language_and_Communication": 13,
    "Aesthetics": 3,
    "Others": 6,
}


def count_credits(transcript):
    genEdCreditsCount = {
        "Wellness": 0,
        "Entrepreneurship": 0,
        "Thai_Citizen_and_Global_Citizen": 0,
        "Language_and_Communication": 0,
        "Aesthetics": 0,
        "Others": 0,
    }
    for i in transcript["results"]:
        for j in i["grade"]:
            if j["grade"] == "P":
                continue
            type_and_credits = findCreditsAndType(j["subject_code"])
            if type_and_credits == None:
                continue
            if (
                genEdCreditsCount[type_and_credits["type"]]
                < maximumCredits[type_and_credits["type"]]
            ):
                genEdCreditsCount[type_and_credits["type"]] += type_and_credits[
                    "credits"
                ]
            else:
                genEdCreditsCount["Others"] += type_and_credits["credits"]
    return genEdCreditsCount


def get_transcript(stdid, token):
    transcript = requests.get(
        url=f"https://myapi.ku.th/std-profile/checkGrades?idcode={stdid}",
        headers={
            "App-Key": "txCR5732xYYWDGdd49M3R19o1OVwdRFc",
            "X-Access-Token": token,
        },
    ).json()
    return transcript


with open("GenEdList.json", encoding="utf-8") as fp:
    GenEdList = json.load(fp)[0]["result"]["data"]["json"]


def SubjectTypeMap(thName: str):
    th_to_en = {
        "กลุ่มสาระอยู่ดีมีสุข": "Wellness",
        "กลุ่มสาระศาสตร์แห่งผู้ประกอบการ": "Entrepreneurship",
        "กลุ่มสาระภาษากับการสื่อสาร": "Language_and_Communication",
        "กลุ่มสาระพลเมืองไทยและพลเมืองโลก": "Thai_Citizen_and_Global_Citizen",
        "กลุ่มสาระสุนทรียศาสตร์": "Aesthetics",
    }
    if thName in th_to_en.keys():
        return th_to_en[thName]
    else:
        return "NOT_GENED"


def findCreditsAndType(stdid: str):
    for subject in GenEdList:
        if stdid == subject["subjectCode"]:
            return {
                "type": SubjectTypeMap(subject["subjectGroup"]),
                "credits": int(
                    re.match(r"^[0-9]*", subject["subjectCredits"]).group(0)
                ),
            }
    return None


def genedService(stdid, token):
    transcript = get_transcript(stdid, token)
    genEdCreditsCount = count_credits(transcript)
    return genEdCreditsCount
