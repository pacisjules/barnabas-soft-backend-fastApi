from fastapi import APIRouter, HTTPException, Depends
from db.table import quotation_detail
from quotation_detail import model
from utils import util
from configs.connection import database
import uuid, datetime
from fastapi_pagination import Page, paginate
router = APIRouter()


# All quotation details
@router.get("/all_quotation_detail", response_model=Page[model.Quotation_DetailList])
async def find_all_quotation_details(currentUser: model.Quotation_DetailList = Depends(util.get_current_active_user)):
    query = quotation_detail.select()
    res = await database.fetch_all(query)
    return paginate(res)


# Find quotation_detail with item name of quotation_detail
@router.get("/likequotation_detail/{name}", response_model=Page[model.Quotation_DetailList])
async def find_like_quotation_detail(name: str, currentUser: model.Quotation_DetailList = Depends(util.get_current_active_user)):

    query = "select * from quotation_detail where item like '%{}%'".format(name)
    res= await database.fetch_all(query=query, values={})
    return paginate(res)



#Find one quotation_detail by ID
@router.get("/quotation_detail/{id}", response_model=model.Quotation_DetailList)
async def find_quotation_detail_by_ID(id: str, currentUser: model.Quotation_DetailList = Depends(util.get_current_active_user)):
    query = quotation_detail.select().where(quotation_detail.c.id == id)
    return await database.fetch_one(query)


#Find quotation_details by USER ID
@router.get("/quotation_detail_userEntry/{id}", response_model=model.Quotation_DetailList)
async def find_quotation_detail_by_userID(id: str, currentUser: model.Quotation_DetailList = Depends(util.get_current_active_user)):
    query = quotation_detail.select().where(quotation_detail.c.user_id == id)
    res = await database.fetch_all(query)
    return paginate(res)

#Find quotation_details by Institution ID
@router.get("/quotation_detail_InstituEntry/{id}", response_model=model.Quotation_DetailList)
async def find_quotation_detail_by_InstituID(id: str, currentUser: model.Quotation_DetailList = Depends(util.get_current_active_user)):
    query = quotation_detail.select().where(quotation_detail.c.institution_id == id)
    res = await database.fetch_all(query)
    return paginate(res)


#Find quotation_details by quotation id
@router.get("/quotation_detail_EmpEntry/{id}", response_model=model.Quotation_DetailList)
async def find_quotation_detail_by_QuotationID(id: str, currentUser: model.Quotation_DetailList = Depends(util.get_current_active_user)):
    query = quotation_detail.select().where(quotation_detail.c.quotation_id == id)
    res = await database.fetch_all(query)
    return paginate(res)





#Find quotation_details by status
@router.get("/quotation_detail_status/{status}", response_model=model.Quotation_DetailList)
async def find_quotation_detail_by_status(status: str, currentUser: model.Quotation_DetailList = Depends(util.get_current_active_user)):
    query = quotation_detail.select().where(quotation_detail.c.status == status)
    res = await database.fetch_all(query)
    return paginate(res)


# add new quotation_detail
@router.post("/addquotation_detail", response_model=model.Quotation_DetailList)
async def registerquotation_detail(QuotDet: model.quotation_detailCreate, currentUser: model.Quotation_DetailList = Depends(util.get_current_active_user)):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())
    query = quotation_detail.insert().values(
        id = gid,

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

#Update quotation_detail
@router.put("/quotation_detail_update", response_model=model.Quotation_DetailList)
async def update_quotation_detail(Quot: model.quotation_detailUpdate, currentUser: model.Quotation_DetailList = Depends(util.get_current_active_user)):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())

    Query = quotation_detail.update().where(quotation_detail.c.id == Quot.id).values(
        id = gid,
        user_i=Quot.user_id,
        institution_id=Quot.institution_id,
        employee_id=Quot.employee_id,
        document=Quot.document,
        quotation_detail_from=Quot.quotation_detail_from,
        tin_number=Quot.tin_number,
        total_amount=Quot.total_amount,
        last_update_at=gdate,
        status = "1"
    )

    await database.execute(Query)
    return await find_quotation_detail_by_ID(Quot.id)


#Delete quotation_detail
@router.delete("/Delete_quotation_detail/{quotation_detail_id}", response_model=model.Quotation_DetailList)
async def Delete_by_quotation_detail_id(quotation_detail_id: str, currentUser: model.Quotation_DetailList = Depends(util.get_current_active_user)):
    query = quotation_detail.delete().where(quotation_detail.c.id == quotation_detail_id)
    return await database.execute(query)