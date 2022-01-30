from numpy import integer
from pydantic import BaseModel, Field


class QuotationCreate(BaseModel):
    user_id:str =Field (..., example="user id")
    institution_id:str =Field (..., example="institution_id")
    employee_id:str =Field (..., example="employee id")

    document:str =Field (..., example="document")
    quotation_from:str =Field (..., example="Quotation_from")
    tin_number:str =Field (..., example="tin_number")
    total_amount:float =Field (..., example="total_amount")

class QuotationList(BaseModel):
    id:str
    user_id:str 
    institution_id:str 
    employee_id:str
    document:str
    quotation_from:str 
    tin_number:str 
    total_amount:float
    status: str
    created_at:str
    last_update_at: str


class QuotationUpdate(BaseModel):
    id:str
    user_id:str 
    institution_id:str 
    employee_id:str
    document:str
    quotation_from:str 
    tin_number:str 
    total_amount:float
    status: str
    created_at:str
    last_update_at: str

