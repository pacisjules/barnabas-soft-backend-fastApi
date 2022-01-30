from pydantic import BaseModel, Field



class InstitutionCreate(BaseModel):
    user_id:str =Field (..., example="user id")
    institution_name:str =Field (..., example="institution name")
    tin_number:str =Field (..., example="tin number")
    address1:str =Field (..., example="address1")
    address2:str =Field (..., example="address2")
    province:str =Field (..., example="province")
    district:str =Field (..., example="district")
    phone1:str =Field (..., example="phone 1")
    phone2:str =Field (..., example="phone 2")
    email:str =Field (..., example="e-mail")


class InstitutionList(BaseModel):
    id:str
    user_id:str 
    institution_name:str
    tin_number:str 
    address1:str
    address2:str
    province:str 
    district:str 
    phone1:str 
    phone2:str
    email:str
    status: str
    created_at:str
    last_update_at: str


class InstitutionUpdate(BaseModel):
    id:str
    user_id:str 
    institution_name:str
    tin_number:str 
    address1:str
    address2:str
    province:str 
    district:str 
    phone1:str 
    phone2:str
    email:str
    status: str
    created_at:str
    last_update_at: str

