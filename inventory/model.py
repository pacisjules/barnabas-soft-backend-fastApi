from pydantic import BaseModel, Field



class InventoryCreate(BaseModel):
    user_id:str =Field (..., example="user id")
    employee_id:str =Field (..., example="employee_id")
    institution_id:str =Field (..., example="institution_id")
    site_name:str =Field (..., example="site_name")
    province:str =Field (..., example="province")
    district:str =Field (..., example="district")
    type:str =Field (..., example="type")

class InventoryList(BaseModel):
    id:str
    user_id:str 
    employee_id:str 
    institution_id:str
    site_name:str 
    province:str
    district:str 
    type:str 
    status: str
    created_at:str
    last_update_at: str


class InventoryUpdate(BaseModel):
    id:str
    user_id:str 
    employee_id:str 
    institution_id:str
    site_name:str 
    province:str
    district:str 
    type:str 
    status: str
    created_at:str
    last_update_at: str

