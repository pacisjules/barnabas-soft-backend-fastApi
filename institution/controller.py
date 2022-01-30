from fastapi import APIRouter, HTTPException, Depends
from db.table import institution
from institution import model
from utils import util
from configs.connection import database
import uuid, datetime
from fastapi_pagination import Page, paginate
router = APIRouter()




# All institutions
@router.get("/all_institution", response_model=Page[model.InstitutionList])
async def find_all_institutions(currentUser: model.InstitutionList = Depends(util.get_current_active_user)):
    query = institution.select()
    res = await database.fetch_all(query)
    return paginate(res)

# Find institution with names
@router.get("/likeinstitution/{names}", response_model=Page[model.InstitutionList])
async def find_like_institution(names: str, currentUser: model.InstitutionList = Depends(util.get_current_active_user)):

    query = "select * from institution where institution_name like '%{}%'".format(names)
    res= await database.fetch_all(query=query, values={})
    return paginate(res)



#Find one institution by TIN Number
@router.get("/institution_ID/{tin_number}", response_model=model.InstitutionList)
async def find_institution_by_tin_number(tin_number: str, currentUser: model.InstitutionList = Depends(util.get_current_active_user)):
    query = institution.select().where(institution.c.tin_number == tin_number)
    return await database.fetch_one(query)

#Find one institution by ID
@router.get("/institution/{id}", response_model=model.InstitutionList)
async def find_institution_by_ID(id: str, currentUser: model.InstitutionList = Depends(util.get_current_active_user)):
    query = institution.select().where(institution.c.id == id)
    return await database.fetch_one(query)


#Find institutions by USER ID
@router.get("/institution_userEntry/{id}", response_model=model.InstitutionList)
async def find_institution_by_userID(id: str, currentUser: model.InstitutionList = Depends(util.get_current_active_user)):
    query = institution.select().where(institution.c.user_id == id)
    res = await database.fetch_all(query)
    return paginate(res)


#Find institutions by province
@router.get("/institution_province/{province}", response_model=model.InstitutionList)
async def find_institution_by_province(province: str, currentUser: model.InstitutionList = Depends(util.get_current_active_user)):
    query = institution.select().where(institution.c.province == province)
    res = await database.fetch_all(query)
    return paginate(res)


#Find institutions by district
@router.get("/institution_district/{district}", response_model=model.InstitutionList)
async def find_institution_by_district(district: str, currentUser: model.InstitutionList = Depends(util.get_current_active_user)):
    query = institution.select().where(institution.c.district == district)
    res = await database.fetch_all(query)
    return paginate(res)


# Find institution with Phone Number

@router.get("/institution_by_phone_number/{phone}", response_model=Page[model.InstitutionList])
async def find_customer_by_phone_number(phone: str, currentUser: model.InstitutionList = Depends(util.get_current_active_user)):
    query = institution.select().where(institution.c.phone1 == phone) or institution.select().where(institution.c.phone2 == phone)
    res = await database.fetch_one(query)
    return paginate(res)

#Find one institution by Email
@router.get("/institution_email/{email}", response_model=model.InstitutionList)
async def find_institution_by_email(email: str, currentUser: model.InstitutionList = Depends(util.get_current_active_user)):
    query = institution.select().where(institution.c.email == email)
    return await database.fetch_one(query)

#Find institutions by status
@router.get("/institution_status/{status}", response_model=model.InstitutionList)
async def find_institution_by_status(status: str, currentUser: model.InstitutionList = Depends(util.get_current_active_user)):
    query = institution.select().where(institution.c.status == status)
    res = await database.fetch_all(query)
    return paginate(res)

# add new institution
@router.post("/addinstitution", response_model=model.InstitutionList)
async def registerinstitution(inst: model.InstitutionCreate, currentUser: model.InstitutionList = Depends(util.get_current_active_user)):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())
    query = institution.insert().values(
        id = gid,
        user_id=inst.user_id,
        institution_name=inst.institution_name,
        tin_number =inst.tin_number,
        address1= inst.address1 ,
        address2= inst.address2 ,
        province= inst.province ,
        district= inst.district ,
        phone1=inst.phone1 ,
        phone2=inst.phone2,
        email=inst.email,
        created_at = gdate,
        last_update_at=gdate,
        status = "1"
        
    )

    await database.execute(query)
    return {
        **inst.dict(),
        "id": gid,
        "created_at": gdate,
        "status": "1"
    }

#Update institution
@router.put("/institution_update", response_model=model.InstitutionList)
async def update_institution(inst: model.InstitutionUpdate, currentUser: model.InstitutionList = Depends(util.get_current_active_user)):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())

    Query = institution.update().where(institution.c.id == inst.id).values(
        id = gid,
        user_id=inst.user_id,
        institution_name=inst.institution_name,
        tin_number =inst.tin_number,
        address1= inst.address1 ,
        address2= inst.address2 ,
        province= inst.province ,
        district= inst.district ,
        phone1=inst.phone1 ,
        phone2=inst.phone2,
        email=inst.email,
        last_update_at=gdate,
        status = "1"
    )

    await database.execute(Query)
    return await find_institution_by_ID(inst.id)


#Delete institution
@router.delete("/Delete_institution/{institution_id}", response_model=model.InstitutionList)
async def Delete_by_institution_id(institution_id: str, currentUser: model.InstitutionList = Depends(util.get_current_active_user)):
    query = institution.delete().where(institution.c.id == institution_id)
    return await database.execute(query)