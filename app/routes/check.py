from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

check_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')


@check_router.get('/', response_class=HTMLResponse)
def check(req: Request):
    return templates.TemplateResponse('check/check.html', {'request': req})

@check_router.get('/checkok', response_class=HTMLResponse)
def checkok(req: Request):
    return templates.TemplateResponse('check/checkok.html', {'request': req})