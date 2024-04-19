from fastapi import APIRouter, Request, status, Form
from fastapi.templating import Jinja2Templates

from app.schemas.visitors import Visitors
from app.services.visitors import VisitorsService

visitors_router = APIRouter()
# jinja2 설정
templates = Jinja2Templates(directory='views/templates')
# jumun_router.mount('/static', StaticFiles(directory='views/static'), name='static')

# 방문객 등록 신청
@visitors_router.post('/visitors/register')
def register(vmdto: Visitors):
    res_url = '/jumun_error'
    result = VisitorsService.insert_visitor(vmdto)
    return result.rowcount

