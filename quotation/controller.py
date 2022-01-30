from fastapi import APIRouter, HTTPException, Depends
from db.table import quotation
from quotation import model
from utils import util
from configs.connection import database
import uuid, datetime
from fastapi_pagination import Page, paginate
router = APIRouter()


# All quotations
@router.get("/all_quotation", response_model=Page[model.QuotationList])
async def find_all_quotations(currentUser: model.QuotationList = Depends(util.get_current_active_user)):
    query = quotation.select()
    res = await database.fetch_all(query)
    return paginate(res)


# Find quotation with name of quotation from
@router.get("/likequotation/{name}", response_model=Page[model.QuotationList])
async def find_like_quotation(name: str, currentUser: model.QuotationList = Depends(util.get_current_active_user)):

    query = "select * from quotation where quotation_from like '%{}%'".format(name)
    res= await database.fetch_all(query=query, values={})
    return paginate(res)



#Find one quotation by ID
@router.get("/quotation/{id}", response_model=model.QuotationList)
async def find_quotation_by_ID(id: str, currentUser: model.QuotationList = Depends(util.get_current_active_user)):
    query = quotation.select().where(quotation.c.id == id)
    return await database.fetch_one(query)


#Find quotations by USER ID
@router.get("/quotation_userEntry/{id}", response_model=model.QuotationList)
async def find_quotation_by_userID(id: str, currentUser: model.QuotationList = Depends(util.get_current_active_user)):
    query = quotation.select().where(quotation.c.user_id == id)
    res = await database.fetch_all(query)
    return paginate(res)

#Find quotations by Institution ID
@router.get("/quotation_InstituEntry/{id}", response_model=model.QuotationList)
async def find_quotation_by_InstituID(id: str, currentUser: model.QuotationList = Depends(util.get_current_active_user)):
    query = quotation.select().where(quotation.c.institution_id == id)
    res = await database.fetch_all(query)
    return paginate(res)


#Find quotations by Employee ID
@router.get("/quotation_EmpEntry/{id}", response_model=model.QuotationList)
async def find_quotation_by_QuotoryID(id: str, currentUser: model.QuotationList = Depends(util.get_current_active_user)):
    query = quotation.select().where(quotation.c.employee_id == id)
    res = await database.fetch_all(query)
    return paginate(res)


#Find quotations by tin number ID
@router.get("/quotation_tinNumber/{tin}", response_model=model.QuotationList)
async def find_quotation_by_tin(tin: str, currentUser: model.QuotationList = Depends(util.get_current_active_user)):
    query = quotation.select().where(quotation.c.tin_number == tin)
    res = await database.fetch_all(query)
    return paginate(res)



#Find quotations by status
@router.get("/quotation_status/{status}", response_model=model.QuotationList)
async def find_quotation_by_status(status: str, currentUser: model.QuotationList = Depends(util.get_current_active_user)):
    query = quotation.select().where(quotation.c.status == status)
    res = await database.fetch_all(query)
    return paginate(res)


# add new quotation
@router.post("/addquotation", response_model=model.QuotationList)
async def registerquotation(Quot: model.QuotationCreate, currentUser: model.QuotationList = Depends(util.get_current_active_user)):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())
    query = quotation.insert().values(
        id = gid,
        user_i=Quot.user_id,
        institution_id=Quot.institution_id,
        employee_id=Quot.employee_id,
        document=Quot.document,
        quotation_from=Quot.quotation_from,
        tin_number=Quot.tin_number,
        total_amount=Quot.total_amount,
        created_at = gdate,
        last_update_at=gdate,
        status = "1"
    )

    await database.execute(query)
    return {
        **Quot.dict(),
        "id": gid,
        "created_at": gdate,
        "status": "1"
    }

#Update quotation
@router.put("/quotation_update", response_model=model.QuotationList)
async def update_quotation(Quot: model.QuotationUpdate, currentUser: model.QuotationList = Depends(util.get_current_active_user)):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())

    Query = quotation.update().where(quotation.c.id == Quot.id).values(
        id = gid,
        user_i=Quot.user_id,
        institution_id=Quot.institution_id,
        employee_id=Quot.employee_id,
        document=Quot.document,
        quotation_from=Quot.quotation_from,
        tin_number=Quot.tin_number,
        total_amount=Quot.total_amount,
        last_update_at=gdate,
        status = "1"
    )

    await database.execute(Query)
    return await find_quotation_by_ID(Quot.id)


#Delete quotation
@router.delete("/Delete_quotation/{quotation_id}", response_model=model.QuotationList)
async def Delete_by_quotation_id(quotation_id: str, currentUser: model.QuotationList = Depends(util.get_current_active_user)):
    query = quotation.delete().where(quotation.c.id == quotation_id)
    return await database.execute(query)