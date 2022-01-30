from fastapi import APIRouter, HTTPException, Depends
from db.table import supplier
from supplier import model
from utils import util
from configs.connection import database
import uuid, datetime
from fastapi_pagination import Page, paginate
router = APIRouter()




# All suppliers
@router.get("/all_supplier", response_model=Page[model.SupplierList])
async def find_all_suppliers(currentUser: model.SupplierList = Depends(util.get_current_active_user)):
    query = supplier.select()
    res = await database.fetch_all(query)
    return paginate(res)

# Find supplier with names
@router.get("/likesupplier/{names}", response_model=Page[model.SupplierList])
async def find_like_supplier(names: str, currentUser: model.SupplierList = Depends(util.get_current_active_user)):

    query = "select * from supplier where name like '%{}%'".format(names)
    res= await database.fetch_all(query=query, values={})
    return paginate(res)


#Find one supplier by TIN Number
@router.get("/supplier_tin/{tin_number}", response_model=model.SupplierList)
async def find_supplier_by_tin_number(tin_number: str, currentUser: model.SupplierList = Depends(util.get_current_active_user)):
    query = supplier.select().where(supplier.c.tin_number == tin_number)
    return await database.fetch_one(query)

#Find one supplier by ID
@router.get("/supplier/{id}", response_model=model.SupplierList)
async def find_supplier_by_ID(id: str, currentUser: model.SupplierList = Depends(util.get_current_active_user)):
    query = supplier.select().where(supplier.c.id == id)
    return await database.fetch_one(query)


#Find suppliers by USER ID
@router.get("/supplier_userEntry/{id}", response_model=model.SupplierList)
async def find_supplier_by_userID(id: str, currentUser: model.SupplierList = Depends(util.get_current_active_user)):
    query = supplier.select().where(supplier.c.user_id == id)
    res = await database.fetch_all(query)
    return paginate(res)


#Find suppliers by province
@router.get("/supplier_province/{province}", response_model=model.SupplierList)
async def find_supplier_by_province(province: str, currentUser: model.SupplierList = Depends(util.get_current_active_user)):
    query = supplier.select().where(supplier.c.province == province)
    res = await database.fetch_all(query)
    return paginate(res)


#Find suppliers by district
@router.get("/supplier_district/{district}", response_model=model.SupplierList)
async def find_supplier_by_district(district: str, currentUser: model.SupplierList = Depends(util.get_current_active_user)):
    query = supplier.select().where(supplier.c.district == district)
    res = await database.fetch_all(query)
    return paginate(res)


# Find supplier with Phone Number

@router.get("/supplier_by_phone_number/{phone}", response_model=Page[model.SupplierList])
async def find_customer_by_phone_number(phone: str, currentUser: model.SupplierList = Depends(util.get_current_active_user)):
    query = supplier.select().where(supplier.c.phone1 == phone) or supplier.select().where(supplier.c.phone2 == phone)
    res = await database.fetch_one(query)
    return paginate(res)

#Find one supplier by Email
@router.get("/supplier_email/{email}", response_model=model.SupplierList)
async def find_supplier_by_email(email: str, currentUser: model.SupplierList = Depends(util.get_current_active_user)):
    query = supplier.select().where(supplier.c.email == email)
    return await database.fetch_one(query)

#Find suppliers by status
@router.get("/supplier_status/{status}", response_model=model.SupplierList)
async def find_supplier_by_status(status: str, currentUser: model.SupplierList = Depends(util.get_current_active_user)):
    query = supplier.select().where(supplier.c.status == status)
    res = await database.fetch_all(query)
    return paginate(res)

# add new supplier
@router.post("/addsupplier", response_model=model.SupplierList)
async def registersupplier(sup: model.SupplierCreate, currentUser: model.SupplierList = Depends(util.get_current_active_user)):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())
    query = supplier.insert().values(
        id = gid,
        user_id=sup.user_id,
        institution_id=sup.institution_id,
        names=sup.names,
        description=sup.description,
        tin_number =sup.tin_number,
        address1= sup.address1 ,
        address2= sup.address2 ,
        province= sup.province ,
        district= sup.district ,
        phone1=sup.phone1 ,
        phone2=sup.phone2,
        email=sup.email,
        created_at = gdate,
        last_update_at=gdate,
        status = "1"
        
    )

    await database.execute(query)
    return {
        **sup.dict(),
        "id": gid,
        "created_at": gdate,
        "status": "1"
    }

#Update supplier
@router.put("/supplier_update", response_model=model.SupplierList)
async def update_supplier(sup: model.SupplierUpdate, currentUser: model.SupplierList = Depends(util.get_current_active_user)):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())

    Query = supplier.update().where(supplier.c.id == sup.id).values(
        id = gid,
        user_id=sup.user_id,
        institution_id=sup.institution_id,
        names=sup.names,
        description=sup.description,
        tin_number =sup.tin_number,
        address1= sup.address1 ,
        address2= sup.address2 ,
        province= sup.province ,
        district= sup.district ,
        phone1=sup.phone1 ,
        phone2=sup.phone2,
        email=sup.email,
        last_update_at=gdate,
        status = "1"
    )

    await database.execute(Query)
    return await find_supplier_by_ID(sup.id)


#Delete supplier
@router.delete("/Delete_supplier/{supplier_id}", response_model=model.SupplierList)
async def Delete_by_supplier_id(supplier_id: str, currentUser: model.SupplierList = Depends(util.get_current_active_user)):
    query = supplier.delete().where(supplier.c.id == supplier_id)
    return await database.execute(query)