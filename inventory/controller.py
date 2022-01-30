from fastapi import APIRouter, HTTPException, Depends
from db.table import inventory
from inventory import model
from utils import util
from configs.connection import database
import uuid, datetime
from fastapi_pagination import Page, paginate
router = APIRouter()




# All inventories
@router.get("/all_inventory", response_model=Page[model.InventoryList])
async def find_all_inventories(currentUser: model.InventoryList = Depends(util.get_current_active_user)):
    query = inventory.select()
    res = await database.fetch_all(query)
    return paginate(res)


# Find inventory with site names
@router.get("/likeinventory/{names}", response_model=Page[model.InventoryList])
async def find_like_inventory(names: str, currentUser: model.InventoryList = Depends(util.get_current_active_user)):

    query = "select * from inventory where site_name like '%{}%'".format(names)
    res= await database.fetch_all(query=query, values={})
    return paginate(res)



#Find one inventory by type
@router.get("/all_inventory_type/{type}", response_model=Page[model.InventoryList])
async def find_all_inventories_type(role: str, currentUser: model.InventoryList = Depends(util.get_current_active_user)):
    query = inventory.select().where(inventory.c.type == role)
    res = await database.fetch_all(query)
    return paginate(res)


#Find one inventory by ID
@router.get("/inventory/{id}", response_model=model.InventoryList)
async def find_inventory_by_ID(id: str, currentUser: model.InventoryList = Depends(util.get_current_active_user)):
    query = inventory.select().where(inventory.c.id == id)
    return await database.fetch_one(query)


#Find inventorys by USER ID
@router.get("/inventory_userEntry/{id}", response_model=model.InventoryList)
async def find_inventory_by_userID(id: str, currentUser: model.InventoryList = Depends(util.get_current_active_user)):
    query = inventory.select().where(inventory.c.user_id == id)
    res = await database.fetch_all(query)
    return paginate(res)

#Find inventories by Institution ID
@router.get("/inventory_InstituEntry/{id}", response_model=model.InventoryList)
async def find_inventory_by_InstituID(id: str, currentUser: model.InventoryList = Depends(util.get_current_active_user)):
    query = inventory.select().where(inventory.c.institution_id == id)
    res = await database.fetch_all(query)
    return paginate(res)


#Find inventories by Inventoyee ID
@router.get("/inventory_EmpEntry/{id}", response_model=model.InventoryList)
async def find_inventory_by_InstituID(id: str, currentUser: model.InventoryList = Depends(util.get_current_active_user)):
    query = inventory.select().where(inventory.c.Inventoyee_id == id)
    res = await database.fetch_all(query)
    return paginate(res)



#Find inventories by province
@router.get("/inventory_province/{province}", response_model=model.InventoryList)
async def find_inventory_by_province(province: str, currentUser: model.InventoryList = Depends(util.get_current_active_user)):
    query = inventory.select().where(inventory.c.province == province)
    res = await database.fetch_all(query)
    return paginate(res)


#Find inventories by district
@router.get("/inventory_district/{district}", response_model=model.InventoryList)
async def find_inventory_by_district(district: str, currentUser: model.InventoryList = Depends(util.get_current_active_user)):
    query = inventory.select().where(inventory.c.district == district)
    res = await database.fetch_all(query)
    return paginate(res)


#Find inventories by status
@router.get("/inventory_status/{status}", response_model=model.InventoryList)
async def find_inventory_by_status(status: str, currentUser: model.InventoryList = Depends(util.get_current_active_user)):
    query = inventory.select().where(inventory.c.status == status)
    res = await database.fetch_all(query)
    return paginate(res)

# add new inventory
@router.post("/addinventory", response_model=model.InventoryList)
async def registerinventory(Invent: model.InventoryCreate, currentUser: model.InventoryList = Depends(util.get_current_active_user)):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())
    query = inventory.insert().values(
        id = gid,
        user_id=Invent.user_id,
        employee_id=Invent.employee_id,
        institution_id=Invent.institution_id,
        site_name=Invent.site_name,
        province= Invent.province ,
        district= Invent.district ,
        type=Invent.type ,
        created_at = gdate,
        last_update_at=gdate,
        status = "1"
    )

    await database.execute(query)
    return {
        **Invent.dict(),
        "id": gid,
        "created_at": gdate,
        "status": "1"
    }

#Update inventory
@router.put("/inventory_update", response_model=model.InventoryList)
async def update_inventory(Invent: model.InventoryUpdate, currentUser: model.InventoryList = Depends(util.get_current_active_user)):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())

    Query = inventory.update().where(inventory.c.id == Invent.id).values(
        id = gid,
        user_id=Invent.user_id,
        employee_id=Invent.employee_id,
        institution_id=Invent.institution_id,
        site_name=Invent.site_name,
        province= Invent.province ,
        district= Invent.district ,
        type=Invent.type ,
        created_at = gdate,
        last_update_at=gdate,
        status = "1"
    )

    await database.execute(Query)
    return await find_inventory_by_ID(Invent.id)


#Delete inventory
@router.delete("/Delete_inventory/{inventory_id}", response_model=model.InventoryList)
async def Delete_by_inventory_id(inventory_id: str, currentUser: model.InventoryList = Depends(util.get_current_active_user)):
    query = inventory.delete().where(inventory.c.id == inventory_id)
    return await database.execute(query)