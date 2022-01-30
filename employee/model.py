from pydantic import BaseModel, Field



class EmployeeCreate(BaseModel):
    user_id:str =Field (..., example="user id")
    institution_id:str =Field (..., example="institution_id")
    first_name:str =Field (..., example="first_name")
    last_name:str =Field (..., example="last_name")
    role:str =Field (..., example="role")
    credits:str =Field (..., example="credits")


    address:str =Field (..., example="address")
    address_street:str =Field (..., example="address_street")

    province:str =Field (..., example="province")
    district:str =Field (..., example="district")
    phone1:str =Field (..., example="phone 1")
    phone2:str =Field (..., example="phone 2")
    email:str =Field (..., example="e-mail")


class EmployeeList(BaseModel):
    id:str
    user_id:str 
    institution_id:str 
    first_name:str 
    last_name:str
    role:str 
    credits:str 


    address:str
    address_street:str 

    province:str
    district:str
    phone1:str
    phone2:str 
    email:str
    status: str
    created_at:str
    last_update_at: str


class EmployeeUpdate(BaseModel):
    id:str
    user_id:str 
    institution_id:str 
    first_name:str 
    last_name:str
    role:str 
    credits:str 
    address:str
    address_street:str 
    province:str
    district:str
    phone1:str
    phone2:str 
    email:str
    status: str
    created_at:str
    last_update_at: str

