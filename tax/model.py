from numpy import integer
from pydantic import BaseModel, Field



class TaxCreate(BaseModel):
    user_id:str =Field (..., example="user id")
    institution_id:str =Field (..., example="institution_id")
    supplier_id:str =Field (..., example="supplier_id")
    product_id:str =Field (..., example="product_id")

    Tax_name:str =Field (..., example="Tax_name")
    tax_percentage:float =Field (..., example="tax percentage")


class TaxList(BaseModel):
    id:str
    user_id:str
    institution_id:str 
    supplier_id:str
    product_id:str 
    Tax_name:str 
    tax_percentage:float 
    status: str
    created_at:str
    last_update_at: str




class TaxUpdate(BaseModel):
    id:str
    user_id:str
    institution_id:str 
    supplier_id:str
    product_id:str 
    Tax_name:str 
    tax_percentage:float 
    
    status: str
    created_at:str
    last_update_at: str

