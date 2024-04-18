from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware


app = FastAPI()

# 세션처리를 미들웨어 설정
app.add_middleware(SessionMiddleware, secret_key='02232024duedate')


# jinja2 설정
templates = Jinja2Templates(directory='views/templates')
app.mount('/static', StaticFiles(directory='views/static'), name='static')


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True)
