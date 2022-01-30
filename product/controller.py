from fastapi import APIRouter, HTTPException, Depends
from db.table import product
from product import model
from utils import util
from configs.connection import database
import uuid, datetime
from fastapi_pagination import Page, paginate
router = APIRouter()




# All products
@router.get("/all_product", response_model=Page[model.ProductList])
async def find_all_products(currentUser: model.ProductList = Depends(util.get_current_active_user)):
    query = product.select()
    res = await database.fetch_all(query)
    return paginate(res)


# Find product with name
@router.get("/likeproduct/{name}", response_model=Page[model.ProductList])
async def find_like_product(name: str, currentUser: model.ProductList = Depends(util.get_current_active_user)):

    query = "select * from product where product_name like '%{}%'".format(name)
    res= await database.fetch_all(query=query, values={})
    return paginate(res)



#Find one product by ID
@router.get("/product/{id}", response_model=model.ProductList)
async def find_product_by_ID(id: str, currentUser: model.ProductList = Depends(util.get_current_active_user)):
    query = product.select().where(product.c.id == id)
    return await database.fetch_one(query)


#Find products by USER ID
@router.get("/product_userEntry/{id}", response_model=model.ProductList)
async def find_product_by_userID(id: str, currentUser: model.ProductList = Depends(util.get_current_active_user)):
    query = product.select().where(product.c.user_id == id)
    res = await database.fetch_all(query)
    return paginate(res)

#Find products by Institution ID
@router.get("/product_InstituEntry/{id}", response_model=model.ProductList)
async def find_product_by_InstituID(id: str, currentUser: model.ProductList = Depends(util.get_current_active_user)):
    query = product.select().where(product.c.institution_id == id)
    res = await database.fetch_all(query)
    return paginate(res)


#Find products by Prodory ID
@router.get("/product_EmpEntry/{id}", response_model=model.ProductList)
async def find_product_by_ProdoryID(id: str, currentUser: model.ProductList = Depends(util.get_current_active_user)):
    query = product.select().where(product.c.Prodory_id == id)
    res = await database.fetch_all(query)
    return paginate(res)


#Find products by Supplier ID
@router.get("/product_EmpEntry/{id}", response_model=model.ProductList)
async def find_product_by_SupplierID(id: str, currentUser: model.ProductList = Depends(util.get_current_active_user)):
    query = product.select().where(product.c.supplier_id == id)
    res = await database.fetch_all(query)
    return paginate(res)


#Find products by status
@router.get("/product_status/{status}", response_model=model.ProductList)
async def find_product_by_status(status: str, currentUser: model.ProductList = Depends(util.get_current_active_user)):
    query = product.select().where(product.c.status == status)
    res = await database.fetch_all(query)
    return paginate(res)

# add new product
@router.post("/addproduct", response_model=model.ProductList)
async def registerproduct(Prod: model.ProductCreate, currentUser: model.ProductList = Depends(util.get_current_active_user)):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())
    query = product.insert().values(
        id = gid,
        user_i=Prod.user_id,
        institution_id=Prod.institution_id,
        supplier_id=Prod.supplier_id,
        inventory_id=Prod.inventory_id, 
        product_name=Prod.product_name, 
        description=Prod.description,
        supplier_price=Prod.supplier_price,
        price=Prod.price,
        quantity=Prod.quantity, 
        imported_at=Prod.imported_at,
        expire_at=Prod.expire_at, 
        created_at = gdate,
        last_update_at=gdate,
        status = "1"
    )

    await database.execute(query)
    return {
        **Prod.dict(),
        "id": gid,
        "created_at": gdate,
        "status": "1"
    }

#Update product
@router.put("/product_update", response_model=model.ProductList)
async def update_product(Prod: model.ProductUpdate, currentUser: model.ProductList = Depends(util.get_current_active_user)):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())

    Query = product.update().where(product.c.id == Prod.id).values(
        id = gid,
        user_i=Prod.user_id,
        institution_id=Prod.institution_id,
        supplier_id=Prod.supplier_id,
        inventory_id=Prod.inventory_id, 
        product_name=Prod.product_name, 
        description=Prod.description,
        supplier_price=Prod.supplier_price,
        price=Prod.price,
        quantity=Prod.quantity, 
        imported_at=Prod.imported_at,
        expire_at=Prod.expire_at, 
        created_at = gdate,
        last_update_at=gdate,
        status = "1"
    )

    await database.execute(Query)
    return await find_product_by_ID(Prod.id)


#Delete product
@router.delete("/Delete_product/{product_id}", response_model=model.ProductList)
async def Delete_by_product_id(product_id: str, currentUser: model.ProductList = Depends(util.get_current_active_user)):
    query = product.delete().where(product.c.id == product_id)
    return await database.execute(query)