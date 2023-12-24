import pymyku
from router.login.LoginBodyDto import LoginBodyDto


def loginService(loginBodyDto: LoginBodyDto):
    client = pymyku.Client(
        username=loginBodyDto.username, password=loginBodyDto.password
    )
    return client.login().json()
