from numpy import integer
from pydantic import BaseModel, Field


class Quotation_DetailCreate(BaseModel):
    user_id:str =Field (..., example="user id")
    institution_id:str =Field (..., example="institution_id")
    quotation_id:str =Field (..., example="employee id")

    item:str =Field (..., example="item")
    quantity:int =Field (..., example="quantity")
    description:str =Field (..., example="description")
    unit_price:float =Field (..., example="total_amount")

class Quotation_DetailList(BaseModel):
    id:str
    user_id:str
    institution_id:str
    quotation_id:str 
    item:str
    quantity:int 
    description:str 
    unit_price:float 
    status: str
    created_at:str
    last_update_at: str


class Quotation_DetailUpdate(BaseModel):
    id:str
    user_id:str
    institution_id:str
    quotation_id:str 
    item:str
    quantity:int 
    description:str 
    unit_price:float 
    status: str
    created_at:str
    last_update_at: str

