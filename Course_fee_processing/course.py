import csv
from datetime import datetime
from abc import ABC,abstractmethod

file_path=r"C:\Users\varshini.anumalla\OneDrive - Acuvate Software Private Limited\Desktop\review2\Course_fee_processing\course.csv"
file=open(file_path,"r",encoding="utf-8")
text=csv.DictReader(file)
data=list(text)
file.close()

print()
data1=[]
seen=set()

with open(r"C:\Users\varshini.anumalla\OneDrive - Acuvate Software Private Limited\Desktop\review2\Course_fee_processing\Errors_file.txt","w",encoding="utf-8") as error_file:
    for row in data:
        valid =True
        if row["CourseID"] in seen:
            error_file.write(f"Duplicate course id found:{row}\n")
            valid =False
        else:
            seen.add(row["CourseID"])
        if not row["CourseName"] or not row["CourseName"].strip():
            error_file.write(f"invalid name found:{row}\n")
            valid=False      
#course type must be either Classroom or Online.for 
        if row['CourseType'] not in ['Classroom','Online']:
            error_file.write(f"Invalid course type found:{row}\n")
            valid =False    
#Base fee must be numeric and greater than zero.
        try:    
            base_fee=float(row["BaseFee"])
            if base_fee<=0:
                error_file.write(f"invalid base fee:{row}\n")
                valid =False
        except(TypeError, ValueError):
            error_file.write(f"invalid base fee:{row}\n")
            valid =False
#Offer discount must be numeric and between 0 and 100, inclusive.
        try:
            offer=float(row["OfferDiscount"])
            if not 0 <= offer<= 100:
                error_file.write(f"invalid offer:{row}\n")
                valid=False
        except(TypeError,ValueError):
            error_file.write(f"invalid offer:{row}\n")
            valid=False
#offer end date must be a valid date in YYYY-MM-DD format when provided.
        if row["OfferEndDate"]:
            try:
                datetime.strptime(row["OfferEndDate"], "%Y-%m-%d")
            except (ValueError, TypeError):
                error_file.write(f"Invalid date format found: {row}\n")
                valid = False
#reject records that violate any validation rule.
        if valid:
            row["BaseFee"]=base_fee
            row["OfferDiscount"]=offer 
            data1.append(row)
        else:
            error_file.write(f"Rejected rows:{row}\n")
print("valid rows",data1) 
print(len(data1))
  
#baseclass
class Course(ABC):
    def __init__(self,courseId,courseName,basefee,offer,offerdate):
        self.courseId=courseId
        self.courseName=courseName
        self.basefee=basefee
        self.offer=offer
        self.offerdate=offerdate
    @abstractmethod
    def Fee_Calculation(self):
        pass
    
class ClassroomCourse(Course):
    def Fee_Calculation(self):
        return self.basefee+2000
            
class OnlineCourse(Course):
    def Fee_Calculation(self):
        return self.basefee-(self.basefee*10/100)

with open(r"C:\Users\varshini.anumalla\OneDrive - Acuvate Software Private Limited\Desktop\review2\Course_fee_processing\report.csv","w",encoding="utf-8") as report_file:
    # next(report_file)
    writer=csv.writer(report_file)
    writer.writerow(["CourseID,CourseName,CourseType,BaseFee,OfferDiscount,OfferEndDate","AdjustedFee","OfferStatus","OfferDiscount","FinalFee"])
    for line in data1:
        courseId=line["CourseID"]
        name=line["CourseName"]
        type=line["CourseType"]
        basefee=line["BaseFee"]
        offer=line["OfferDiscount"]
        offerdate=line["OfferEndDate"]
        
        if type=="Classroom":
            course=ClassroomCourse(courseId,name,basefee,offer,offerdate)
            adjusted_fee=basefee+2000
        elif type=="Online":
            course=OnlineCourse(courseId,name,basefee,offer,offerdate)
            adjusted_fee=basefee-(basefee*10/100)
        
        today=datetime.now().date()
        offer_amount=0
        
        if offer>0 and offerdate:
            end_date=datetime.strptime(offerdate,"%Y-%m-%d").date()
            if end_date>today:
                offer_amount=adjusted_fee*offer/100
        final_fee=adjusted_fee-offer_amount
        if offer_amount>0:
            offerStatus="WithOffer"
        else:
            offerStatus="WithoutOffer"
        writer.writerow(
            [courseId,
            name,
            type,
            basefee,
            offer,
            offerdate,
            adjusted_fee,
            offerStatus,
            offer_amount,
            final_fee]
        )
        
        
        
    