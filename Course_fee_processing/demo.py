import datetime
import csv
from datetime import datetime
from abc import ABC,abstractmethod

file_path=r"C:\Users\varshini.anumalla\OneDrive - Acuvate Software Private Limited\Desktop\review2\Course_fee_processing\course.csv"
file=open(file_path,"r",encoding="utf-8")
text=csv.DictReader(file)
data=list(text)

data1 = []
seen_ids = set()

with open("errors.txt", "w", encoding="utf-8") as error_file:
    for course in data:
        valid=True
        #Course ID must be unique
        if course["CourseID"] in seen_ids:
            error_file.write(f"Duplicate course ID found: {course}\n")
            valid = False
        else:
            seen_ids.add(course["CourseID"])

        #Course name must not be empty
        if not course["CourseName"] or not course["CourseName"].strip():
            error_file.write(f"Empty course name found: {course}\n")
            valid = False

        #Course type validation
        if course["CourseType"] not in ["Classroom", "Online"]:
            error_file.write(f"Invalid course type found: {course}\n")
            valid = False

        #Base fee validation
        try:
            base_fee = float(course["BaseFee"])
            if base_fee <= 0:
                error_file.write(f"Invalid base fee found: {course}\n")
                valid = False
        except (ValueError, TypeError):
            error_file.write(f"Invalid base fee found: {course}\n")
            valid = False
        #Offer discount validation
        try:
            discount = float(course["OfferDiscount"])

            if not 0 <= discount <= 100:
                error_file.write(f"Invalid offer discount found: {course}\n")
                valid = False
        except (ValueError, TypeError):
            error_file.write(f"Invalid offer discount found: {course}\n")
            valid = False
        #Offer end date validation
        if course["OfferEndDate"]:
            try:
                datetime.strptime(course["OfferEndDate"], "%Y-%m-%d")
            except (ValueError, TypeError):
                error_file.write(f"Invalid date format found: {course}\n")
                valid = False
        # 7. Accept or reject the record
        if valid:
            course["BaseFee"] = base_fee
            course["OfferDiscount"] = discount
            data1.append(course)
        else:
            error_file.write(f"Rejected record: {course}\n\n")
print("Valid courses:", data1)

class Course(ABC):
    def __init__(self, courseId, courseName, basefee, discount, offerEndDate):
        self.courseId = courseId
        self.courseName = courseName
        self.basefee = float(basefee)
        self.discount = float(discount)
        self.offerEndDate = offerEndDate

    @abstractmethod
    def Fee_Calculation(self):
        pass

    def display(self, offerstatus, final_fee):
        print("Course ID:", self.courseId)
        print("Course Name:", self.courseName)
        print("Base Fee:", self.basefee)
        print("Offer Status:", offerstatus)
        print("Offer Discount:", self.discount)
        print("Final Fee:", final_fee)
        print("-" * 40)

class ClassroomCourse(Course):
    def Fee_Calculation(self):
        total_fee = self.basefee + 2000
        return total_fee

class OnlineCourse(Course):
    def Fee_Calculation(self):
        today = datetime.now().strftime("%Y-%m-%d")
        if self.discount > 0 and self.offerEndDate and self.offerEndDate >= today:
            discount_amount = self.basefee * self.discount / 100
            total_fee = self.basefee - discount_amount
            return total_fee
        return self.basefee
for record in data1:
    if record["CourseType"] == "Classroom":
        course = ClassroomCourse(
            record["CourseID"],
            record["CourseName"],
            record["BaseFee"],
            record["OfferDiscount"],
            record["OfferEndDate"]
        )
        final_fee = course.Fee_Calculation()
        course.display("Not Applied", final_fee)
    elif record["CourseType"] == "Online":
        course = OnlineCourse(
            record["CourseID"],
            record["CourseName"],
            record["BaseFee"],
            record["OfferDiscount"],
            record["OfferEndDate"]
        )
        today = datetime.now().strftime("%Y-%m-%d")
        if course.discount > 0 and course.offerEndDate and course.offerEndDate >= today:
            offerstatus = "Applied"
        else:
            offerstatus = "Not Applied"
        final_fee = course.Fee_Calculation()
        course.display(offerstatus, final_fee)