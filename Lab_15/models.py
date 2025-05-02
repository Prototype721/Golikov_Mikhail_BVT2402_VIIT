from pydantic import BaseModel, constr
from fastapi import status

class Search_message(BaseModel):
    message: str | None = None 
    my_name: constr(min_length=3, max_length=50)

class Response_message(Search_message, BaseModel):
    result: str | None = None
    status: str = str(status.HTTP_412_PRECONDITION_FAILED)
    