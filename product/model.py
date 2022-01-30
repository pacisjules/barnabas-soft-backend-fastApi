from numpy import integer
from pydantic import BaseModel, Field



class ProductCreate(BaseModel):
    user_id:str =Field (..., example="user id")
    institution_id:str =Field (..., example="institution_id")
    supplier_id:str =Field (..., example="supplier_id")
    inventory_id:str =Field (..., example="inventory_id")
    product_name:str =Field (..., example="product_name")
    description:str =Field (..., example="description")
    supplier_price:float =Field (..., example="supplier_price")
    price:float =Field (..., example="price")
    quantity:int =Field (..., example="quantity")
    imported_at:str =Field (..., example="imported at")
    expire_at:str =Field (..., example="expire at")


class ProductList(BaseModel):
    id:str
    user_id:str
    institution_id:str
    supplier_id:str
    inventory_id:str 
    product_name:str 
    description:str
    supplier_price:float
    price:float
    quantity:int
    imported_at:str
    expire_at:str 
    status: str
    created_at:str
    last_update_at: str




class ProductUpdate(BaseModel):
    id:str
    user_id:str
    institution_id:str
    supplier_id:str
    inventory_id:str 
    product_name:str 
    description:str
    supplier_price:float
    price:float
    quantity:int
    imported_at:str
    expire_at:str 
    status: str
    created_at:str
    last_update_at: str

