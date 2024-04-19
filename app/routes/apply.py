from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from app.schemas.visitors import Visitors
from app.services.visitors import VisitorsService

apply_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')


@apply_router.get('/', response_class=HTMLResponse)
def apply(req: Request):
    return templates.TemplateResponse('apply/apply.html', {'request': req})

@apply_router.post('/apply')
def apply(vmdto: Visitors):
    result = VisitorsService.insert_visitor(vmdto)
    return result.rowcount

@apply_router.get('/apply', response_class=HTMLResponse)
def applyok(req:Request):
    return templates.TemplateResponse('/applyok.html', {'request': req})