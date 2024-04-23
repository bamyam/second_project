from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from starlette import status
from starlette.responses import RedirectResponse

from app.services.admin import AdminService
from app.services.mail import MailService

admin_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')


@admin_router.get('/', response_class=HTMLResponse)
def admin(req: Request):
    info = AdminService.select_visit()
    return templates.TemplateResponse('admin/admin.html', {'request': req,
        'info': info})


@admin_router.post('/accept')
def accept(data: dict):
    number = data['number']

    result = AdminService.accept_visit(number)

    res_url = '/error'
    if result.rowcount > 0:
        res_url = '/admin'
        visitor_name, visitor_email, time = MailService.find_data(number)
        MailService.mail_accepted(visitor_name, visitor_email, time)

    return RedirectResponse(res_url, status_code=status.HTTP_302_FOUND)

@admin_router.post('/reject')
def reject(data: dict):
    number = data['number']
    reason = data['reason']

    result = AdminService.reject_visit(number)

    res_url = '/error'
    if result.rowcount > 0:
        res_url = '/admin'
        visitor_name, visitor_email, time = MailService.find_data(number)
        MailService.mail_regected(visitor_name, visitor_email, time, reason)

    return RedirectResponse(res_url, status_code=status.HTTP_302_FOUND)
