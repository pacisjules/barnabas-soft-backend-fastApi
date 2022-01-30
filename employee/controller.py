from fastapi import APIRouter, HTTPException, Depends
from db.table import employee
from employee import model
from utils import util
from configs.connection import database
import uuid, datetime
from fastapi_pagination import Page, paginate
router = APIRouter()




# All employees
@router.get("/all_employee", response_model=Page[model.EmployeeList])
async def find_all_employees(currentUser: model.EmployeeList = Depends(util.get_current_active_user)):
    query = employee.select()
    res = await database.fetch_all(query)
    return paginate(res)

# Find employee with names
@router.get("/likeemployee/{names}", response_model=Page[model.EmployeeList])
async def find_like_employee(names: str, currentUser: model.EmployeeList = Depends(util.get_current_active_user)):

    query = "select * from employee where first_name like '%{}%'".format(names)
    res= await database.fetch_all(query=query, values={})
    return paginate(res)



#Find one employee by role
@router.get("/all_employee_role/{role}", response_model=Page[model.EmployeeList])
async def find_all_employees(role: str, currentUser: model.EmployeeList = Depends(util.get_current_active_user)):
    query = employee.select().where(employee.c.role == role)
    res = await database.fetch_all(query)
    return paginate(res)


#Find one employee by ID
@router.get("/employee/{id}", response_model=model.EmployeeList)
async def find_employee_by_ID(id: str, currentUser: model.EmployeeList = Depends(util.get_current_active_user)):
    query = employee.select().where(employee.c.id == id)
    return await database.fetch_one(query)


#Find employees by USER ID
@router.get("/employee_userEntry/{id}", response_model=model.EmployeeList)
async def find_employee_by_userID(id: str, currentUser: model.EmployeeList = Depends(util.get_current_active_user)):
    query = employee.select().where(employee.c.user_id == id)
    res = await database.fetch_all(query)
    return paginate(res)


#Find employees by province
@router.get("/employee_province/{province}", response_model=model.EmployeeList)
async def find_employee_by_province(province: str, currentUser: model.EmployeeList = Depends(util.get_current_active_user)):
    query = employee.select().where(employee.c.province == province)
    res = await database.fetch_all(query)
    return paginate(res)


#Find employees by district
@router.get("/employee_district/{district}", response_model=model.EmployeeList)
async def find_employee_by_district(district: str, currentUser: model.EmployeeList = Depends(util.get_current_active_user)):
    query = employee.select().where(employee.c.district == district)
    res = await database.fetch_all(query)
    return paginate(res)


# Find employee with Phone Number
@router.get("/employee_by_phone_number/{phone}", response_model=Page[model.EmployeeList])
async def find_customer_by_phone_number(phone: str, currentUser: model.EmployeeList = Depends(util.get_current_active_user)):
    query = employee.select().where(employee.c.phone1 == phone) or employee.select().where(employee.c.phone2 == phone)
    res = await database.fetch_one(query)
    return paginate(res)


#Find one employee by Email
@router.get("/employee_email/{email}", response_model=model.EmployeeList)
async def find_employee_by_email(email: str, currentUser: model.EmployeeList = Depends(util.get_current_active_user)):
    query = employee.select().where(employee.c.email == email)
    return await database.fetch_one(query)

#Find employees by status
@router.get("/employee_status/{status}", response_model=model.EmployeeList)
async def find_employee_by_status(status: str, currentUser: model.EmployeeList = Depends(util.get_current_active_user)):
    query = employee.select().where(employee.c.status == status)
    res = await database.fetch_all(query)
    return paginate(res)

# add new employee
@router.post("/addemployee", response_model=model.EmployeeList)
async def registeremployee(Empl: model.EmployeeCreate, currentUser: model.EmployeeList = Depends(util.get_current_active_user)):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())
    query = employee.insert().values(
        id = gid,
        user_id=Empl.user_id,
        institution_id=Empl.institution_id,
        first_name=Empl.first_name,
        last_name =Empl.last_name,
        role= Empl.role,
        credits= Empl.credits,
        province= Empl.province ,
        district= Empl.district ,
        phone1=Empl.phone1 ,
        phone2=Empl.phone2,
        email=Empl.email,
        created_at = gdate,
        last_update_at=gdate,
        status = "1"
    )

    await database.execute(query)
    return {
        **Empl.dict(),
        "id": gid,
        "created_at": gdate,
        "status": "1"
    }

#Update employee
@router.put("/employee_update", response_model=model.EmployeeList)
async def update_employee(Empl: model.EmployeeUpdate, currentUser: model.EmployeeList = Depends(util.get_current_active_user)):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())

    Query = employee.update().where(employee.c.id == Empl.id).values(
        id = gid,
        user_id=Empl.user_id,
        institution_id=Empl.institution_id,
        first_name=Empl.first_name,
        last_name =Empl.last_name,
        role= Empl.role,
        credits= Empl.credits,
        province= Empl.province ,
        district= Empl.district ,
        phone1=Empl.phone1 ,
        phone2=Empl.phone2,
        email=Empl.email,
        last_update_at=gdate,
        status = "1"
    )

    await database.execute(Query)
    return await find_employee_by_ID(Empl.id)


#Delete employee
@router.delete("/Delete_employee/{employee_id}", response_model=model.EmployeeList)
async def Delete_by_employee_id(employee_id: str, currentUser: model.EmployeeList = Depends(util.get_current_active_user)):
    query = employee.delete().where(employee.c.id == employee_id)
    return await database.execute(query)