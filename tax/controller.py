from fastapi import APIRouter, HTTPException, Depends
from db.table import tax
from tax import model
from utils import util
from configs.connection import database
import uuid, datetime
from fastapi_pagination import Page, paginate
router = APIRouter()




# All taxies
@router.get("/all_taxies", response_model=Page[model.TaxList])
async def find_all_taxs(currentUser: model.TaxList = Depends(util.get_current_active_user)):
    query = tax.select()
    res = await database.fetch_all(query)
    return paginate(res)


# Find tax with name
@router.get("/liketax/{name}", response_model=Page[model.TaxList])
async def find_like_tax(name: str, currentUser: model.TaxList = Depends(util.get_current_active_user)):

    query = "select * from tax where tax_name like '%{}%'".format(name)
    res= await database.fetch_all(query=query, values={})
    return paginate(res)


#Find one tax by ID
@router.get("/tax/{id}", response_model=model.TaxList)
async def find_tax_by_ID(id: str, currentUser: model.TaxList = Depends(util.get_current_active_user)):
    query = tax.select().where(tax.c.id == id)
    return await database.fetch_one(query)


#Find taxies by USER ID
@router.get("/tax_userEntry/{id}", response_model=model.TaxList)
async def find_tax_by_userID(id: str, currentUser: model.TaxList = Depends(util.get_current_active_user)):
    query = tax.select().where(tax.c.user_id == id)
    res = await database.fetch_all(query)
    return paginate(res)

#Find taxies by Institution ID
@router.get("/tax_InstituEntry/{id}", response_model=model.TaxList)
async def find_tax_by_InstituID(id: str, currentUser: model.TaxList = Depends(util.get_current_active_user)):
    query = tax.select().where(tax.c.institution_id == id)
    res = await database.fetch_all(query)
    return paginate(res)


#Find taxies by ProdUCT ID
@router.get("/tax_EmpEntry/{id}", response_model=model.TaxList)
async def find_tax_by_ProdoryID(id: str, currentUser: model.TaxList = Depends(util.get_current_active_user)):
    query = tax.select().where(tax.c.Product_id == id)
    res = await database.fetch_all(query)
    return paginate(res)


#Find taxies by status
@router.get("/tax_status/{status}", response_model=model.TaxList)
async def find_tax_by_status(status: str, currentUser: model.TaxList = Depends(util.get_current_active_user)):
    query = tax.select().where(tax.c.status == status)
    res = await database.fetch_all(query)
    return paginate(res)

# add new tax
@router.post("/addtax", response_model=model.TaxList)
async def registertax(TaxIn: model.TaxCreate, currentUser: model.TaxList = Depends(util.get_current_active_user)):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())
    query = tax.insert().values(
        id = gid,
        user_id=TaxIn.user_id,
        institution_id=TaxIn.institution_id, 
        supplier_id=TaxIn.supplier_id,
        product_id=TaxIn.product_id, 
        Tax_name=TaxIn.Tax_name, 
        tax_percentage=TaxIn.tax_percentage,
        created_at = gdate,
        last_update_at=gdate,
        status = "1"
    )

    await database.execute(query)
    return {
        **TaxIn.dict(),
        "id": gid,
        "created_at": gdate,
        "status": "1"
    }

#Update tax
@router.put("/tax_update", response_model=model.TaxList)
async def update_tax(TaxIn: model.TaxUpdate, currentUser: model.TaxList = Depends(util.get_current_active_user)):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())

    Query = tax.update().where(tax.c.id == TaxIn.id).values(
        id = gid,
        user_id=TaxIn.user_id,
        institution_id=TaxIn.institution_id, 
        supplier_id=TaxIn.supplier_id,
        product_id=TaxIn.product_id, 
        Tax_name=TaxIn.Tax_name, 
        tax_percentage=TaxIn.tax_percentage,
        last_update_at=gdate,
        status = "1"
    )

    await database.execute(Query)
    return await find_tax_by_ID(TaxIn.id)


#Delete tax
@router.delete("/Delete_tax/{tax_id}", response_model=model.TaxList)
async def Delete_by_tax_id(tax_id: str, currentUser: model.TaxList = Depends(util.get_current_active_user)):
    query = tax.delete().where(tax.c.id == tax_id)
    return await database.execute(query)