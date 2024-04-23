from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

admin_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')


@admin_router.get('/', response_class=HTMLResponse)
def admin(req: Request):
    return templates.TemplateResponse('admin/admin.html', {'request': req})

# @admin_router.post('/accept')
# def accept():
#     result =

# @admin_router.post('/reject')
# def reject():
#     result =