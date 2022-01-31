import sqlalchemy
from sqlalchemy import ForeignKey
metadata = sqlalchemy.MetaData()

#Start and Configuration


#1 Table
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("username"  , sqlalchemy.String, unique=True),
    sqlalchemy.Column("password"  , sqlalchemy.String),
    sqlalchemy.Column("fullname"  , sqlalchemy.String),
    sqlalchemy.Column("email"     , sqlalchemy.String, unique=True),
    sqlalchemy.Column("type"     , sqlalchemy.String),
    sqlalchemy.Column("role"     , sqlalchemy.String),
    sqlalchemy.Column("company"     , sqlalchemy.String),
    sqlalchemy.Column("phone"     , sqlalchemy.String, unique=True),
    sqlalchemy.Column("living"     , sqlalchemy.String),
    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)


#2 Table
institution  = sqlalchemy.Table(
    "institution",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),

    sqlalchemy.Column("institution_name"  , sqlalchemy.String),
    sqlalchemy.Column("tin_number"  , sqlalchemy.String),
    sqlalchemy.Column("address1"  , sqlalchemy.String),
    sqlalchemy.Column("address2"  , sqlalchemy.String),
    sqlalchemy.Column("province"  , sqlalchemy.String),
    sqlalchemy.Column("district"  , sqlalchemy.String),
    sqlalchemy.Column("phone1"  , sqlalchemy.String),
    sqlalchemy.Column("phone2"  , sqlalchemy.String),
    sqlalchemy.Column("email"     , sqlalchemy.String),
    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)


#3 Table
customer  = sqlalchemy.Table(
    "customer",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("institution_id", sqlalchemy.String, ForeignKey(institution.c.id), nullable=False),
    
    sqlalchemy.Column("company_name"  , sqlalchemy.String),
    sqlalchemy.Column("tin_number"  , sqlalchemy.String),
    sqlalchemy.Column("represent_names"  , sqlalchemy.String),
    sqlalchemy.Column("address1"  , sqlalchemy.String),
    sqlalchemy.Column("address2"  , sqlalchemy.String),
    sqlalchemy.Column("province"  , sqlalchemy.String),
    sqlalchemy.Column("district"  , sqlalchemy.String),
    sqlalchemy.Column("phone1"  , sqlalchemy.String),
    sqlalchemy.Column("phone2"  , sqlalchemy.String),
    sqlalchemy.Column("email"     , sqlalchemy.String),
    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)

#4 Table
supplier  = sqlalchemy.Table(
    "supplier",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("institution_id", sqlalchemy.String, ForeignKey(institution.c.id), nullable=False),
    
    sqlalchemy.Column("name"  , sqlalchemy.String),
    sqlalchemy.Column("description"  , sqlalchemy.String),
    sqlalchemy.Column("tin_number"  , sqlalchemy.String),
    sqlalchemy.Column("address1"  , sqlalchemy.String),
    sqlalchemy.Column("address2"  , sqlalchemy.String),
    sqlalchemy.Column("province"  , sqlalchemy.String),
    sqlalchemy.Column("district"  , sqlalchemy.String),
    sqlalchemy.Column("phone1"  , sqlalchemy.String),
    sqlalchemy.Column("phone2"  , sqlalchemy.String),
    sqlalchemy.Column("email"     , sqlalchemy.String),
    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)

#5 Table
employee  = sqlalchemy.Table(
    "employee",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("institution_id", sqlalchemy.String, ForeignKey(institution.c.id), nullable=False),

    sqlalchemy.Column("first_name"  , sqlalchemy.String),
    sqlalchemy.Column("last_name"  , sqlalchemy.String),
    sqlalchemy.Column("role"  , sqlalchemy.String),
    sqlalchemy.Column("credits"  , sqlalchemy.String),
    sqlalchemy.Column("address"  , sqlalchemy.String),
    sqlalchemy.Column("address_street"  , sqlalchemy.String),
    sqlalchemy.Column("province"  , sqlalchemy.String),
    sqlalchemy.Column("district"  , sqlalchemy.String),
    sqlalchemy.Column("phone1"  , sqlalchemy.String),
    sqlalchemy.Column("phone2"  , sqlalchemy.String),
    sqlalchemy.Column("email"     , sqlalchemy.String),
    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)


#6 Table
inventory  = sqlalchemy.Table(
    "inventory",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("employee_id", sqlalchemy.String, ForeignKey(employee.c.id), nullable=False),
    sqlalchemy.Column("institution_id", sqlalchemy.String, ForeignKey(institution.c.id), nullable=False),
    sqlalchemy.Column("site_name"  , sqlalchemy.String),
    sqlalchemy.Column("province"  , sqlalchemy.String),
    sqlalchemy.Column("district"  , sqlalchemy.String),
    sqlalchemy.Column("type"  , sqlalchemy.String),
    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)


#7 Table
product  = sqlalchemy.Table(
    "product",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("institution_id", sqlalchemy.String, ForeignKey(institution.c.id), nullable=False),
    sqlalchemy.Column("supplier_id", sqlalchemy.String, ForeignKey(supplier.c.id), nullable=False),
    sqlalchemy.Column("inventory_id", sqlalchemy.String, ForeignKey(inventory.c.id), nullable=False),


    sqlalchemy.Column("product_name"  , sqlalchemy.String),
    sqlalchemy.Column("description"  , sqlalchemy.String),
    sqlalchemy.Column("supplier_price"  , sqlalchemy.Float),
    sqlalchemy.Column("price"  , sqlalchemy.Float),
    sqlalchemy.Column("quantity"  , sqlalchemy.Integer),
    sqlalchemy.Column("status"    , sqlalchemy.String),
    
    sqlalchemy.Column("imported_at"  , sqlalchemy.String),
    sqlalchemy.Column("expire_at"  , sqlalchemy.String),

    sqlalchemy.Column("status", sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)


#8 Table
tax= sqlalchemy.Table(
    "tax",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("institution_id", sqlalchemy.String, ForeignKey(institution.c.id), nullable=False),
    sqlalchemy.Column("product_id", sqlalchemy.String, ForeignKey(product.c.id), nullable=False),

    sqlalchemy.Column("tax_name"  , sqlalchemy.String),
    sqlalchemy.Column("tax_percentage", sqlalchemy.Float),
    
    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)


#Sales Dashboard

#9 Table
quotation= sqlalchemy.Table(
    "quotation",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("institution_id", sqlalchemy.String, ForeignKey(institution.c.id), nullable=False),
    sqlalchemy.Column("employee_id", sqlalchemy.String, ForeignKey(employee.c.id), nullable=False),

    sqlalchemy.Column("document"  , sqlalchemy.String),
    sqlalchemy.Column("quotation_from"  , sqlalchemy.String),
    sqlalchemy.Column("tin_number"  , sqlalchemy.String),
    sqlalchemy.Column("total_amount", sqlalchemy.Float),

    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)


#10 Table
quotation_detail= sqlalchemy.Table(
    "quotation_detail",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("institution_id", sqlalchemy.String, ForeignKey(institution.c.id), nullable=False),
    sqlalchemy.Column("quotation_id", sqlalchemy.String, ForeignKey(quotation.c.id), nullable=False),

    sqlalchemy.Column("item"  , sqlalchemy.String),
    sqlalchemy.Column("quantity"  , sqlalchemy.Integer),
    sqlalchemy.Column("description"  , sqlalchemy.String),
    sqlalchemy.Column("unit_price", sqlalchemy.Float),

    sqlalchemy.Column("status" , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)


#11 Table
purchase_order= sqlalchemy.Table(
    "purchase_order",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("institution_id", sqlalchemy.String, ForeignKey(institution.c.id), nullable=False),
    sqlalchemy.Column("quatation_id", sqlalchemy.String, ForeignKey(quotation.c.id), nullable=False),

    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)


#12 Table
invoice= sqlalchemy.Table(
    "invoice",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("institution_id", sqlalchemy.String, ForeignKey(institution.c.id), nullable=False),
    sqlalchemy.Column("quatation_id", sqlalchemy.String, ForeignKey(quotation.c.id), nullable=False),
    sqlalchemy.Column("purchase_order_id", sqlalchemy.String, ForeignKey(purchase_order.c.id), nullable=False),

    sqlalchemy.Column("tin_number"  , sqlalchemy.String),
    sqlalchemy.Column("tax_percentage", sqlalchemy.Float),
    sqlalchemy.Column("cash_total", sqlalchemy.Float),

    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)

#13 Table
payment= sqlalchemy.Table(
    "payment",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("institution_id", sqlalchemy.String, ForeignKey(institution.c.id), nullable=False),
    sqlalchemy.Column("quatation_id", sqlalchemy.String, ForeignKey(quotation.c.id), nullable=False),
    sqlalchemy.Column("purchase_order_id", sqlalchemy.String, ForeignKey(purchase_order.c.id), nullable=False),
    sqlalchemy.Column("invoice_id", sqlalchemy.String, ForeignKey(invoice.c.id), nullable=False),

    sqlalchemy.Column("payment_type", sqlalchemy.String),
    sqlalchemy.Column("cash_total", sqlalchemy.Float),
    sqlalchemy.Column("remain_total", sqlalchemy.Float),
    sqlalchemy.Column("process", sqlalchemy.String),

    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)

#Cost of Sales Dashboard

#14 Table Request
sale_request= sqlalchemy.Table(
    "sale_request",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("institution_id", sqlalchemy.String, ForeignKey(institution.c.id), nullable=False),
    sqlalchemy.Column("employee_id", sqlalchemy.String, ForeignKey(employee.c.id), nullable=False),

    sqlalchemy.Column("description"  , sqlalchemy.String),
    sqlalchemy.Column("event_name"  , sqlalchemy.String),

    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)


#15 Table Request Details
sale_request_detail= sqlalchemy.Table(
    "sale_request_detail",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("institution_id", sqlalchemy.String, ForeignKey(institution.c.id), nullable=False),
    sqlalchemy.Column("employee_id", sqlalchemy.String, ForeignKey(employee.c.id), nullable=False),
    sqlalchemy.Column("sale_request_id", sqlalchemy.String, ForeignKey(sale_request.c.id), nullable=False),

    sqlalchemy.Column("item"  , sqlalchemy.String),
    sqlalchemy.Column("description"  , sqlalchemy.String),
    sqlalchemy.Column("quantity"  , sqlalchemy.Integer),
    sqlalchemy.Column("unit_price", sqlalchemy.Float),


    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)




#16 Table Proforma
sale_proforma= sqlalchemy.Table(
    "sale_proforma",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("institution_id", sqlalchemy.String, ForeignKey(institution.c.id), nullable=False),
    sqlalchemy.Column("employee_id", sqlalchemy.String, ForeignKey(employee.c.id), nullable=False),
    sqlalchemy.Column("sale_request_id", sqlalchemy.String, ForeignKey(sale_request.c.id), nullable=False),

    sqlalchemy.Column("upload"  , sqlalchemy.String),
    sqlalchemy.Column("event_name"  , sqlalchemy.String),


    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)


#17 Table Proforma details
sale_proforma_details= sqlalchemy.Table(
    "sale_proforma_details",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("institution_id", sqlalchemy.String, ForeignKey(institution.c.id), nullable=False),
    sqlalchemy.Column("employee_id", sqlalchemy.String, ForeignKey(employee.c.id), nullable=False),
    sqlalchemy.Column("sale_request_id", sqlalchemy.String, ForeignKey(sale_request.c.id), nullable=False),
    sqlalchemy.Column("sale_proforma_id", sqlalchemy.String, ForeignKey(sale_proforma.c.id), nullable=False),

    sqlalchemy.Column("item"  , sqlalchemy.String),
    sqlalchemy.Column("quantity"  , sqlalchemy.Integer),
    sqlalchemy.Column("description"  , sqlalchemy.String),
    sqlalchemy.Column("unit_price", sqlalchemy.Float),


    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)


#18 Table Request_purchase_order
sales_purchase_order= sqlalchemy.Table(
    "sales_purchase_order",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("institution_id", sqlalchemy.String, ForeignKey(institution.c.id), nullable=False),
    sqlalchemy.Column("employee_id", sqlalchemy.String, ForeignKey(employee.c.id), nullable=False),
    sqlalchemy.Column("sale_request_id", sqlalchemy.String, ForeignKey(sale_request.c.id), nullable=False),
    sqlalchemy.Column("sale_proforma_id", sqlalchemy.String, ForeignKey(sale_proforma.c.id), nullable=False),

    sqlalchemy.Column("description"  , sqlalchemy.String),
    sqlalchemy.Column("event_name"  , sqlalchemy.String),


    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)





#19 Table Request_invoice
sales_invoice= sqlalchemy.Table(
    "sales_invoice",
    metadata,
        sqlalchemy.Column("id", sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("institution_id", sqlalchemy.String, ForeignKey(institution.c.id), nullable=False),
    sqlalchemy.Column("employee_id", sqlalchemy.String, ForeignKey(employee.c.id), nullable=False),
    sqlalchemy.Column("sale_request_id", sqlalchemy.String, ForeignKey(sale_request.c.id), nullable=False),
    sqlalchemy.Column("sale_proforma_id", sqlalchemy.String, ForeignKey(sale_proforma.c.id), nullable=False),
    sqlalchemy.Column("sales_purchase_order_id", sqlalchemy.String, ForeignKey(sales_purchase_order.c.id), nullable=False),

    sqlalchemy.Column("upload"  , sqlalchemy.String),
    sqlalchemy.Column("event_name"  , sqlalchemy.String),


    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)




#20 Table Request_advance_amount
sales_advance= sqlalchemy.Table(
    "sales_advance",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("institution_id", sqlalchemy.String, ForeignKey(institution.c.id), nullable=False),
    sqlalchemy.Column("employee_id", sqlalchemy.String, ForeignKey(employee.c.id), nullable=False),
    sqlalchemy.Column("sale_request_id", sqlalchemy.String, ForeignKey(sale_request.c.id), nullable=False),
    sqlalchemy.Column("sale_proforma_id", sqlalchemy.String, ForeignKey(sale_proforma.c.id), nullable=False),
    sqlalchemy.Column("sales_purchase_order_id", sqlalchemy.String, ForeignKey(sales_purchase_order.c.id), nullable=False),

    sqlalchemy.Column("event_name"  , sqlalchemy.String),
    sqlalchemy.Column("description"  , sqlalchemy.String),
    sqlalchemy.Column("amount"  , sqlalchemy.Float),
    sqlalchemy.Column("remain_amount"  , sqlalchemy.Float),

    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)







#Expenses Dashboard





#21 Table Expenses Request
expenses_request= sqlalchemy.Table(
    "expenses_request",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("institution_id", sqlalchemy.String, ForeignKey(institution.c.id), nullable=False),
    sqlalchemy.Column("employee_id", sqlalchemy.String, ForeignKey(employee.c.id), nullable=False),

    sqlalchemy.Column("description"  , sqlalchemy.String),
    sqlalchemy.Column("event_name"  , sqlalchemy.String),

    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)

#22 Table Expenses Request details
expense_request_detail= sqlalchemy.Table(
    "expense_request_detail",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("institution_id", sqlalchemy.String, ForeignKey(institution.c.id), nullable=False),
    sqlalchemy.Column("employee_id", sqlalchemy.String, ForeignKey(employee.c.id), nullable=False),
    sqlalchemy.Column("expenses_request_id", sqlalchemy.String, ForeignKey(expenses_request.c.id), nullable=False),

    sqlalchemy.Column("item"  , sqlalchemy.String),
    sqlalchemy.Column("quantity"  , sqlalchemy.Integer),
    sqlalchemy.Column("description"  , sqlalchemy.String),
    sqlalchemy.Column("unit_price", sqlalchemy.Float),


    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)




#23 Table Expenses Document
expenses_document= sqlalchemy.Table(
    "expenses_document",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("institution_id", sqlalchemy.String, ForeignKey(institution.c.id), nullable=False),
    sqlalchemy.Column("employee_id", sqlalchemy.String, ForeignKey(employee.c.id), nullable=False),
    sqlalchemy.Column("expenses_request_id", sqlalchemy.String, ForeignKey(expenses_request.c.id), nullable=False),

    sqlalchemy.Column("upload"  , sqlalchemy.String),
    sqlalchemy.Column("event_name"  , sqlalchemy.String),


    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)


#24 Table Expenses Document details
expense_document_details= sqlalchemy.Table(
    "expense_document_details",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("institution_id", sqlalchemy.String, ForeignKey(institution.c.id), nullable=False),
    sqlalchemy.Column("employee_id", sqlalchemy.String, ForeignKey(employee.c.id), nullable=False),
    sqlalchemy.Column("expenses_request_id", sqlalchemy.String, ForeignKey(expenses_request.c.id), nullable=False),
    sqlalchemy.Column("expenses_document_id", sqlalchemy.String, ForeignKey(expenses_document.c.id), nullable=False),

    sqlalchemy.Column("item"  , sqlalchemy.String),
    sqlalchemy.Column("quantity"  , sqlalchemy.Integer),
    sqlalchemy.Column("description"  , sqlalchemy.String),
    sqlalchemy.Column("unit_price", sqlalchemy.Float),


    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)





#25 Table Expenses Advance
expenses_advance= sqlalchemy.Table(
    "expense_advance",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("institution_id", sqlalchemy.String, ForeignKey(institution.c.id), nullable=False),
    sqlalchemy.Column("employee_id", sqlalchemy.String, ForeignKey(employee.c.id), nullable=False),
    sqlalchemy.Column("expenses_request_id", sqlalchemy.String, ForeignKey(expenses_request.c.id), nullable=False),

    
    sqlalchemy.Column("event_name"  , sqlalchemy.String),
    sqlalchemy.Column("description"  , sqlalchemy.String),
    sqlalchemy.Column("amount"  , sqlalchemy.Float),
    sqlalchemy.Column("remain_amount"  , sqlalchemy.Float),


    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)

#Share Holders


#26 Table ShareHolder
ShareHolder  = sqlalchemy.Table(
    "ShareHolder",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("institution_id", sqlalchemy.String, ForeignKey(institution.c.id), nullable=False),
    
    sqlalchemy.Column("description"  , sqlalchemy.String),
    sqlalchemy.Column("address1"  , sqlalchemy.String),
    sqlalchemy.Column("address2"  , sqlalchemy.String),
    sqlalchemy.Column("province"  , sqlalchemy.String),
    sqlalchemy.Column("district"  , sqlalchemy.String),
    sqlalchemy.Column("phone1"  , sqlalchemy.String),
    sqlalchemy.Column("phone2"  , sqlalchemy.String),
    sqlalchemy.Column("email"     , sqlalchemy.String),
    sqlalchemy.Column("value"    , sqlalchemy.String),
    sqlalchemy.Column("status"    , sqlalchemy.String),
    
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)




#Banking



#27 Table Accounts






#28 Table Account Recharge





#29 Table Account Withdraw







#30 Table Bank transaction






#31 Table Bank reconciliation