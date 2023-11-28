from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
import router.login.login_controller as login
import router.gened.gened_controller as gened

app = FastAPI()
app.include_router(login.router)
app.include_router(gened.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
