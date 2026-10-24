import csv
import json
import math
import sqlite3
from datetime import datetime,date,timedelta

# Read CSV files
with open(r"C:\Users\varshini.anumalla\OneDrive - Acuvate Software Private Limited\Desktop\review2\billing_engine\plans.csv","r",newline="") as plan_file, \
     open(r"C:\Users\varshini.anumalla\OneDrive - Acuvate Software Private Limited\Desktop\review2\billing_engine\billing.csv","r",newline="") as bill_file:

    plan_reader=csv.DictReader(plan_file)
    plan_data=list(plan_reader)

    bill_reader=csv.DictReader(bill_file)
    bill_data=list(bill_reader)
def segment():
    customers={}
    segment_data=[]
    for bill in bill_data:
        customer_id=bill["customer_id"]
        if customer_id not in customers:
            customers[customer_id]=[]
        customers[customer_id].append(bill)

    start_date=date(2026,9,1)
    end_date=date(2026,9,30)

    for customer_id in customers:
        events=customers[customer_id]

        # Process events in date order
        events.sort(key=lambda event:datetime.strptime(event["event_date"],"%Y-%m-%d"))

        current_plan=None
        segment_start=None

        for event in events:
            event_date=datetime.strptime(event["event_date"],"%Y-%m-%d").date()
            event_type=event["event_type"]
            plan_code=event["plan_code"]

            if event_type=="START":
                current_plan=plan_code
                segment_start=event_date
                
            elif event_type=="CHANGE":
                if current_plan is not None:
                    segment_end=event_date-timedelta(days=1)
                    actual_start=max(segment_start,start_date)
                    actual_end=min(segment_end,end_date)

                    if actual_start<=actual_end:
                        days=(actual_end-actual_start).days+1
                        segment_data.append({
                            "customer_id":customer_id,"plan":current_plan,"start":actual_start,"end":actual_end,"days":days})
                current_plan=plan_code
                segment_start=event_date
                
            elif event_type=="CANCEL":
                if current_plan is not None:
                    actual_start=max(segment_start,start_date)
                    actual_end=min(event_date,end_date)
                    if actual_start<=actual_end:
                        days=(actual_end-actual_start).days+1
                        segment_data.append({
                            "customer_id":customer_id,
                            "plan":current_plan,
                            "start":actual_start,
                            "end":actual_end,
                            "days":days
                        })
                current_plan=None
                segment_start=None

        # If the plan is still active
        if current_plan is not None:
            actual_start=max(segment_start,start_date)
            actual_end=end_date

            if actual_start<=actual_end:
                days=(actual_end-actual_start).days+1
                segment_data.append({
                    "customer_id":customer_id,
                    "plan":current_plan,
                    "start":actual_start,
                    "end":actual_end,
                    "days":days
                })
    return segment_data


# Calculate segment fees and customer totals
def pricing(segment_data):
    days_in_month=30

    for segment in segment_data:
        plan_code=segment["plan"]
        days=segment["days"]
        plan_found=False
        for plan in plan_data:
            if plan["plan_code"]==plan_code:
                monthly_fee=float(plan["monthly_fee"])
                included_units=int(plan["included_units"])
                plan_found=True
                break

        if not plan_found:
            raise ValueError(f"Plan not found: {plan_code}")
        segment_fee=round(monthly_fee*days/days_in_month,2)
        segment_allowance=math.floor(included_units*days/days_in_month)
        segment["segment_fee"]=segment_fee
        segment["segment_allowance"]=segment_allowance

    # 2. Group segment fees by customer
    customer_data={}
    for segment in segment_data:
        customer_id=segment["customer_id"]
        fee=segment["segment_fee"]
        if customer_id not in customer_data:
            customer_data[customer_id]=[]
        customer_data[customer_id].append(fee)
        
    customer_totals={}
    for customer_id in customer_data:
        fees=customer_data[customer_id]

        segment1_fee=fees[0] if len(fees)>0 else 0
        segment2_fee=fees[1] if len(fees)>1 else 0
        total_fee=round(sum(fees),2)

        customer_totals[customer_id]={
            "segment1_fee":segment1_fee,
            "segment2_fee":segment2_fee,
            "total_fee":total_fee,
            "segment_count":len(fees)
        }
    print("Customer totals:")
    for customer_id in customer_totals:
        print(customer_id,customer_totals[customer_id])
    return segment_data,customer_totals

# function call
segment_data=segment()
segment_data,customer_totals=pricing(segment_data)


# Database connection
conn=sqlite3.connect(
    r"C:\Users\varshini.anumalla\OneDrive - Acuvate Software Private Limited\Desktop\review2\billing_engine\billing.db"
)

cursor=conn.cursor()

# Recreate the table
cursor.execute("DROP TABLE IF EXISTS segment_billing")

cursor.execute("""
CREATE TABLE segment_billing(
    segment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    billing_month TEXT,
    customer_id TEXT,
    plan_code TEXT,
    start_date TEXT,
    end_date TEXT,
    active_days INTEGER,
    segment1_fee TEXT,
    segment2_fee TEXT,
    total_fee TEXT
)
""")

# Insert segments into the database

for segment in segment_data:
    customer_id = segment["customer_id"]
    segment1_fee = customer_totals[customer_id]["segment1_fee"]
    segment2_fee = customer_totals[customer_id]["segment2_fee"]
    total_fee = customer_totals[customer_id]["total_fee"]

    cursor.execute("""
    INSERT INTO segment_billing
    (billing_month,customer_id,plan_code,start_date,end_date,
     active_days,segment1_fee,segment2_fee,total_fee)
    VALUES(?,?,?,?,?,?,?,?,?)
    """,(
        "2026-09",
        segment["customer_id"],
        segment["plan"],
        str(segment["start"]),
        str(segment["end"]),
        segment["days"],
        format(customer_totals[segment["customer_id"]]["segment1_fee"], ".2f"),
        format(customer_totals[segment["customer_id"]]["segment2_fee"], ".2f"),
        format(total_fee,".2f")
    ))

conn.commit()

# Display database records
print("\nDatabase records:")

cursor.execute("SELECT * FROM segment_billing")

for row in cursor.fetchall():
    print(row)


# Read segments back from the database for JSON output
cursor.execute("""
SELECT customer_id, plan_code, start_date, end_date,
       active_days, segment1_fee, segment2_fee
FROM segment_billing
WHERE billing_month=?
ORDER BY customer_id, start_date
""", ("2026-09",))

rows=cursor.fetchall()

# Group database records by customer
customer_data={}

for row in rows:
    customer_id, plan_code, start_date, end_date, days, fee1, fee2 = row

    # print(customer_id, fee1, fee2)

    if customer_id not in customer_data:
        customer_data[customer_id]={
            "customer_id":customer_id,
            "segments":[],
            "active_days":0,
            "total_fee":0
        }

    segment_info={
        "plan_code":plan_code,
        "start_date":start_date,
        "end_date":end_date,
        "days":days,
        "segment1_fee": fee1,
        "segment2_fee": fee2,
    }

    customer_data[customer_id]["segments"].append(segment_info)
    customer_data[customer_id]["active_days"]+=days
    customer_data[customer_id]["total_fee"]+=float(fee1)
    customer_data[customer_id]["total_fee"]+=float(fee2)
    

# Build customer list
customers=[]

for customer_id in sorted(customer_data):
    customer=customer_data[customer_id]
    customer["total_fee"]=format(customer["total_fee"],".2f")
    customers.append(customer)

# Find customers without segments
all_customer_ids=set()

for bill in bill_data:
    all_customer_ids.add(bill["customer_id"])

customers_without_segments=len(all_customer_ids-set(customer_data.keys()))

# Get plan totals using SQL aggregate query
cursor.execute("""
SELECT plan_code,COUNT(*),CAST(segment1_fee AS NUMERIC)
       + CAST(segment2_fee AS NUMERIC) AS total_fee
FROM segment_billing
WHERE billing_month=?
GROUP BY plan_code
ORDER BY plan_code
""",("2026-09",))

plan_totals=[]

for row in cursor.fetchall():
    plan_code,segment_count,plan_fee=row

    plan_totals.append({
        "plan_code":plan_code,
        "segment_count":segment_count,
        "total_fee":format(float(plan_fee),".2f")
    })

# Build output document
total_fee=sum(float(row[5]) for row in rows)

document={
    "billing_month":"2026-09",
    "days_in_month":30,
    "customers":customers,
    "summary":{
        "customer_count":len(customers),
        "segment_count":len(rows),
        "customers_without_segments":customers_without_segments,
        "total_fee":format(total_fee,".2f")
    },
    "plan_totals":plan_totals
}

# Write segments.json
with open(
    r"C:\Users\varshini.anumalla\OneDrive - Acuvate Software Private Limited\Desktop\review2\billing_engine\segments.json",
    "w",
    encoding="utf-8"
) as file:
    json.dump(document,file,indent=2)

print("\nsegments.json created successfully")

conn.close()