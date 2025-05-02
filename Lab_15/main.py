from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse

import urllib.parse as parse
import wikipedia 

from models import Search_message, Response_message


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")



@app.post("/post", response_model=Response_message)
async def post_port(content: Search_message):
    try:
        url = wikipedia.page(content.message).url
        status_code = str(status.HTTP_200_OK)
    except:
        url = "Error"
        status_code = str(status.HTTP_412_PRECONDITION_FAILED)
    
    return Response_message(
        message=content.message,
        my_name=content.my_name,
        result=url,
        status=status_code
    )
    


@app.get("/find/{content}", response_class=HTMLResponse)
async def find_page(request: Request, content: str):
    decoded_content = parse.unquote(content)
    try:
        page_summary = wikipedia.summary(decoded_content)
        return templates.TemplateResponse("result_summary.html", {"request": request, "content": page_summary})
    except:
        return RedirectResponse(url="/")


@app.get("/", response_class=HTMLResponse)
async def main(request: Request = None, message: str | None = None, limit: int = 10):
    if message is None:
        return FileResponse("index_main.html")
    else:
        decoded_message = parse.unquote(message)
        list_research = wikipedia.search(decoded_message, results=limit)
        return templates.TemplateResponse("index_search_reasults.html", {"request": request, "content": list_research})












































# @app.exception_handler(HTTPException)
# async def custom_404_handler(exc: HTTPException):
#     if exc.status_code == 404:
#         return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
#     return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)