from fastapi import APIRouter,HTTPException
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.params import Form
from app.services.visitors import VisitorsService

check_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')


@check_router.get('/', response_class=HTMLResponse)
def check(req: Request):
    return templates.TemplateResponse('check/check.html', {'request': req})

@check_router.get('/checkok', response_class=HTMLResponse)
def checkok(req: Request):
    return templates.TemplateResponse('check/checkok.html', {'request': req})



@check_router.post("/checkok")
async def search_visitor(request: Request, name: str = Form(), phone_number: str = Form()):
    visitor_info = VisitorsService.search_visitor(name, phone_number)
    if not visitor_info:
        raise HTTPException(status_code=404, detail="Visitor not found")

    # visitor_info를 템플릿에 전달하고 템플릿 렌더링
    return templates.TemplateResponse("checkok.html", {"request": request, "visitor_info": visitor_info})
    return JSONResponse(content={"result:"})