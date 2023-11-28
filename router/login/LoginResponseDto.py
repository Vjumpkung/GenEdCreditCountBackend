from pydantic import BaseModel

"""
{
  "code": "success",
  "message": "",
  "accesstoken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImI2NDEwNTA0MDQ3IiwidXNlcnR5cGUiOiIxIiwiaWRjb2RlIjoiNjQxMDUwNDA0NyIsInN0ZGlkIjoiMjEzNzc4IiwiZmlyc3ROYW1lRW4iOiJDaGFucmljaCIsImZpcnN0TmFtZVRoIjoi4LiK4Liy4LiN4Lik4LiX4LiY4Li04LmMIiwibGFzdE5hbWVFbiI6IlBJU0lUSklORyIsImxhc3ROYW1lVGgiOiLguJ7guLTguKjguLTguKnguJDguYzguIjguKPguLTguIciLCJ0aXRsZVRoIjoi4LiZ4Liy4LiiIiwicm9sZUlkIjpudWxsLCJzdGRTdGF0dXNDb2RlIjoiMjcxMDEiLCJpYXQiOjE3MDExODI5MDgsImV4cCI6MTcwMTE4NDcwOH0.BOz8_7RIqcyeso4G4ACNOdynmoJT6TcHkO8TO4VkPdU",
  "renewtoken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImI2NDEwNTA0MDQ3IiwidXNlcnR5cGUiOiIxIiwiaWRjb2RlIjoiNjQxMDUwNDA0NyIsInN0ZGlkIjoiMjEzNzc4IiwiZmlyc3ROYW1lRW4iOiJDaGFucmljaCIsImZpcnN0TmFtZVRoIjoi4LiK4Liy4LiN4Lik4LiX4LiY4Li04LmMIiwibGFzdE5hbWVFbiI6IlBJU0lUSklORyIsImxhc3ROYW1lVGgiOiLguJ7guLTguKjguLTguKnguJDguYzguIjguKPguLTguIciLCJ0aXRsZVRoIjoi4LiZ4Liy4LiiIiwicm9sZUlkIjpudWxsLCJzdGRTdGF0dXNDb2RlIjoiMjcxMDEiLCJpYXQiOjE3MDExODI5MDgsImV4cCI6MTcwMTE4NjUwOH0.0Kq0DJc9exQPTOjRVno5LKfyoT_qMTTN6_OB9GLYAWM",
  "user": {
    "loginName": "b6410504047",
    "userType": "1",
    "idCode": "6410504047",
    "titleTh": "นาย",
    "titleEn": "Mr.",
    "firstNameTh": "ชาญฤทธิ์",
    "firstNameEn": "Chanrich",
    "middleNameTh": null,
    "middleNameEn": null,
    "lastNameTh": "พิศิษฐ์จริง",
    "lastNameEn": "PISITJING",
    "avatar": " ",
    "gender": "18701",
    "student": {
      "loginName": "b6410504047",
      "stdId": "213778",
      "stdCode": "6410504047",
      "titleTh": "นาย",
      "titleEn": "Mr.",
      "firstNameTh": "ชาญฤทธิ์",
      "middleNameTh": null,
      "lastNameTh": "พิศิษฐ์จริง",
      "firstNameEn": "Chanrich",
      "middleNameEn": null,
      "lastNameEn": "PISITJING",
      "copenId": "5480",
      "copenNameTh": "ปริญญาตรี หลักสูตรวิศวกรรมศาสตรบัณฑิต สาขาวิชาวิศวกรรมคอมพิวเตอร์ แผนการศึกษาสำหรับนิสิตที่ไม่เรียนสหกิจศึกษา",
      "copenNameEn": "ปริญญาตรี หลักสูตรวิศวกรรมศาสตรบัณฑิต สาขาวิชาวิศวกรรมคอมพิวเตอร์ แผนการศึกษาสำหรับนิสิตที่ไม่เรียนสหกิจศึกษา",
      "campusCode": "B",
      "campusNameTh": "บางเขน",
      "campusNameEn": "Bangkhen",
      "facultyCode": "E",
      "facultyNameTh": "วิศวกรรมศาสตร์",
      "facultyNameEn": "Engineering",
      "departmentCode": "B",
      "departmentNameTh": "วิศวกรรมคอมพิวเตอร์",
      "departmentNameEn": "Computer Engineering",
      "majorCode": "E09",
      "majorNameTh": "วิศวกรรมคอมพิวเตอร์",
      "majorNameEn": "Computer Engineering",
      "nationCode": "TH",
      "nationalityNameTh": "ประเทศไทย",
      "nationalityNameEn": "THAILAND",
      "studentStatusCode": "17001",
      "studentStatusNameTh": "ปกติ",
      "studentStatusNameEn": "Regular",
      "studentTypeCode": "27101",
      "studentTypeNameTh": "นิสิตปัจจุบัน",
      "studentTypeNameEn": "นิสิตปัจจุบัน",
      "edulevelCode": "0",
      "edulevelNameTh": "ปริญญาตรี",
      "edulevelNameEn": "Bachelor Degree",
      "studentYear": "3",
      "advisorId": "E9018",
      "advisorNameTh": "อัครพงศ์ พัชรรุ่งเรือง",
      "advisorNameEn": "Akrapong Patchararoungruang",
      "positionTh": "ผู้ช่วยศาสตราจารย์",
      "email": " ",
      "mobileNo": " "
    },
    "roleMenus": [
      {
        "menuId": 9081,
        "menuNameTh": "ทำงาน",
        "menuUrl": null,
        "menuIcon": null,
        "parentMenuId": 9080,
        "menuType": 2
      },
      {
        "menuId": 9082,
        "menuNameTh": "ข่าวสารนิสิต",
        "menuUrl": "/std/announcement",
        "menuIcon": "fas fa-calendar-alt",
        "parentMenuId": 9081,
        "menuType": 3
      },
      {
        "menuId": 9084,
        "menuNameTh": "ตารางเรียน/ตารางสอบ",
        "menuUrl": "/std/classroom",
        "menuIcon": "fas fa-book-reader",
        "parentMenuId": 9081,
        "menuType": 3
      },
      {
        "menuId": 9085,
        "menuNameTh": "วิชาที่เปิดให้ลงทะเบียน",
        "menuUrl": "/std/subject",
        "menuIcon": "ion ion-md-apps",
        "parentMenuId": 9081,
        "menuType": 3
      },
      {
        "menuId": 9086,
        "menuNameTh": "เลือกรูปแบบ/การเงิน",
        "menuUrl": "/std/financeStudent",
        "menuIcon": "fas fa-dollar-sign",
        "parentMenuId": 9081,
        "menuType": 3
      },
      {
        "menuId": 9087,
        "menuNameTh": "ลงทะเบียน/เพิ่ม-ถอน",
        "menuUrl": "/std/enroll",
        "menuIcon": "fas fa-th-list",
        "parentMenuId": 9081,
        "menuType": 3
      },
      {
        "menuId": 9088,
        "menuNameTh": "ผลการลงทะเบียน",
        "menuUrl": "/std/enrollresult",
        "menuIcon": "fas fa-list-ul",
        "parentMenuId": 9081,
        "menuType": 3
      },
      {
        "menuId": 9089,
        "menuNameTh": "ตรวจสอบผลการเรียน",
        "menuUrl": "/std/grade",
        "menuIcon": "zmdi zmdi-graduation-cap",
        "parentMenuId": 9081,
        "menuType": 3
      },
      {
        "menuId": 9090,
        "menuNameTh": "ประวัติการลงทะเบียน",
        "menuUrl": "/std/enrollhistory",
        "menuIcon": "fas fa-scroll",
        "parentMenuId": 9081,
        "menuType": 3
      },
      {
        "menuId": 9091,
        "menuNameTh": "สถิติ",
        "menuUrl": "/std/dashboard",
        "menuIcon": "zmdi zmdi-apps",
        "parentMenuId": 9081,
        "menuType": 3
      },
      {
        "menuId": 9095,
        "menuNameTh": "ประวัตินิสิต",
        "menuUrl": "/std/profile",
        "menuIcon": "zmdi zmdi-account-box",
        "parentMenuId": 9081,
        "menuType": 3
      }
    ]
  },
  "cache": false
}
"""


class LoginResponseDto(BaseModel):
    code: str
    message: str
    accesstoken: str
    renewtoken: str
    user: dict
    cache: bool
