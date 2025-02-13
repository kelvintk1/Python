from abc import ABC, abstractmethod

class Department(ABC):
    @abstractmethod
    def print_department_details(self):
        pass

class Student(Department):
    def __init__(self, student_name, regd_no, elective_subject, avg_marks, dept_name, dept_head, hostel_name, hostel_location, number_of_rooms):
        self.student_name = student_name
        self.regd_no = regd_no
        self.elective_subject = elective_subject
        self.avg_marks = avg_marks
        self.dept_name = dept_name
        self.dept_head = dept_head
        self.hostel_name = hostel_name
        self.hostel_location = hostel_location
        self.number_of_rooms = number_of_rooms

    def set_student_details(self, student_name, regd_no, elective_subject, avg_marks, dept_name, dept_head, hostel_name, hostel_location, number_of_rooms):
        self.student_name = student_name
        self.regd_no = regd_no
        self.elective_subject = elective_subject
        self.avg_marks = avg_marks
        self.dept_name = dept_name
        self.dept_head = dept_head
        self.hostel_name = hostel_name
        self.hostel_location = hostel_location
        self.number_of_rooms = number_of_rooms

    def get_student_details(self):
        return {
            "Student Name": self.student_name,
            "Registration Number": self.regd_no,
            "Elective Subject": self.elective_subject,
            "Average Marks": self.avg_marks,
            "Department Name": self.dept_name,
            "Department Head": self.dept_head,
            "Hostel Name": self.hostel_name,
            "Hostel Location": self.hostel_location,
            "Number of Rooms": self.number_of_rooms
        }

    def print_department_details(self):
        print(f"Department Name: {self.dept_name}")
        print(f"Department Head: {self.dept_head}")

    def migrate_hostel(self, new_hostel, new_location, new_rooms):
        self.hostel_name = new_hostel
        self.hostel_location = new_location
        self.number_of_rooms = new_rooms
        print(f"Hostel details updated for {self.student_name}.")

class UniversityManager:
    def __init__(self):
        self.student_record = None

    def admit_student(self, student):
        self.student_record = student
        print(f"Student {student.student_name} admitted successfully.")

    def display_student_details(self):
        if self.student_record:
            details = self.student_record.get_student_details()
            for key, value in details.items():
                print(f"{key}: {value}")
        else:
            print("No student record found.")

    def update_hostel(self, new_hostel, new_location, new_rooms):
        if self.student_record:
            self.student_record.migrate_hostel(new_hostel, new_location, new_rooms)
        else:
            print("No student record found.")


student1 = Student(
    student_name="Kelvin Tetteh K.",
    regd_no="22017033",
    elective_subject="Information Technology",
    avg_marks= 80.0,
    dept_name="Computer Science",
    dept_head="Dr. Smith",
    hostel_name="Pent Hostel",
    hostel_location="Legon Campus",
    number_of_rooms= 300
)

university_manager = UniversityManager()
university_manager.admit_student(student1)

university_manager.update_hostel("Diamond Hostel", "Legon Campus", 1200)

university_manager.display_student_details()