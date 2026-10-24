import pyodbc
connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=ACU-HYD-LT-2010\\SQLEXPRESS;"
    "DATABASE=pythonpractice;"
    "Trusted_Connection=yes;"
)
conn = pyodbc.connect(connection_string)
print("Database connected successfully!")

cur=conn.cursor()
cur.execute("select * from E_commerce")
columns=[column[0] for column in cur.description]
print(columns)
rows=cur.fetchall()
data=[]
for row in rows:
    data.append(dict(zip(columns, row)))
print(data)

#product sold
quantity={}
for item in data:
    product=item["productName"]
    if product in quantity:
        quantity[product]+=item["quantity"]
    else:
        quantity[product]=item['quantity']
print(quantity)

#total revenue
revenue={}
for item in data:
    # quantity=item["quantity"]
    # unitPrice=item["unitPrice"]\
    product=item["productName"]
    total=item["quantity"]*item["unitPrice"]
    if product in revenue:
        revenue[product]+=total
    else:
        revenue[product]=total
print(revenue)

#product ranking
product_rank=list(revenue.keys())
print(product_rank)
for i in range(len(product_rank)):
    for j in range(i+1,len([product_rank])):
        p1=product_rank[i]
        p2=product_rank[j]
        if revenue[p1]<revenue[p2]:
            product_rank[i],product_rank[j]=product_rank[j],product_rank[i]
        elif revenue[p1]==revenue[p2]:
            if quantity[p1]<quantity[p2]:
                product_rank[i],product_rank[j]=product_rank[j],product_rank[i]
            elif quantity[p1]==quantity[p2]:
                if p1>p2:
                    product_rank[i],product_rank[j]=product_rank[j],product_rank[i]  
for product in product_rank:
    print(product,"-","quantity:", quantity[product],"revenue:",revenue[product])
    
#product with highest total quantity sold
high_pro=""
high_quantity=0
for item in quantity:
    if quantity[item]>high_quantity:
        high_pro =item
print(high_pro)         

#highest revenue product
revenue_pro=''
high_revenue=0
for item in revenue:
    if revenue[item]>high_revenue:
        high_revenue=revenue[item]
        revenue_pro=item
print(revenue_pro)

purchase={}
for item in data:
    customer=item["customer_id"]
    if customer in purchase:
        purchase[customer]+=item["unitPrice"]
    else:
        purchase[customer]=item["unitPrice"]
print(purchase) 
# # list_purchase=list(purchase)   
# # for i in range(list_purchase[:3]):
# #     print(i)
# purchase_list=list(purchase.keys())
# for item in purchase:
#     if 
sorted_purchase=sorted(
    purchase.items(),key=lambda x:x[1],reverse=True
)
print(sorted_purchase)

rank=1
for p in sorted_purchase[:3]:
    print(rank,p[0],p[1])
    rank+=1 
    
    
orders_by_date={}
for item in data:
    date=item["order_date"]
    if date in orders_by_date:
        orders_by_date[date]+=1
    else:
        orders_by_date[date]=1
print("Orders by date:",orders_by_date)

quantity_by_date={}
for item in data:
    date1=item["order_date"]
    if date1 in quantity_by_date:
        quantity_by_date[date1]+=item["quantity"]
    else:
        quantity_by_date[date1]=item["quantity"]
print("Quantity by date:", quantity_by_date)

revenue_by_date={}
for item in data:
    date2=item["order_date"]
    total=item["quantity"]*item["unitPrice"]
    if date2 in revenue_by_date:
        revenue_by_date[date2]+=total
    else:
        revenue_by_date[date2]=total
print("Revenue by date:", revenue_by_date)

date_rev=""
high_date_rev=0
for item in revenue_by_date:
    if revenue_by_date[item] > high_date_rev:
        high_date_rev=revenue_by_date[item]
        date_rev=item
print(date_rev)

print("Total no.of orders:",len(data))
total_quantity=0
for item in data:
    total_quantity+=item["quantity"]
print("total quantity sold:",total_quantity)
total_revenue=0
for item in data:
    total_revenue+=item["quantity"]*item['unitPrice']
print("Total revenue:",total_revenue)
products = []
for item in data:
    product = item["productName"]
    if product not in products:
        products.append(product)
print("Unique products:", products)
print("Number of unique products:", len(products))

