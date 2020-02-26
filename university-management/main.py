from pyexcel_ods import get_data, save_data
import json
import easygui
import os

class ParseODS():
    def __init__(self, filename):
        self.doc = get_data(filename)
        self.data = json.loads(json.dumps(self.doc))["Sheet1"]
        self.subjects = self.data[2]

    def get_names(self):
        students = []
        for student in self.data[3:]:
            if student:
                students.append(student[0])
        return students

    def get_student(self, name):
        student_ = {"name": name}
        for student in self.data[3:]:
            if student[0] == name:
                for marks in student[1:]:
                    student_[self.subjects[student.index(marks)]] = marks
                break
        return student_

    def get_average(self, name):
        average = 0
        total = 0
        for student in self.data[3:]:
            if student[0] == name:
                for marks in student[1:]:
                    if self.subjects[student.index(marks)] == "Physics" or self.subjects[student.index(
                            marks)] == "Geometry" or self.subjects[student.index(marks)] == "Algebra":
                        average += marks * 2
                        total += 2
                    else:
                        average += marks
                        total += 1
                break
        return average / total



def academics_average(mark1, mark2, mark3, mark4):
    average = 0
    total = 0

    for sub in mark1:
        if sub == "name":
            pass
        elif sub == "Physics":
            average += mark1[sub] * 2
            total += 2
        elif sub == "Geometry":
            average += mark1[sub] * 2
            total += 2
        elif sub == "Algebra":
            average += mark1[sub] * 2
            total += 2
        else:
            average += mark1[sub]
            total += 1

    for sub in mark2:
        if sub == "name":
            pass
        elif sub == "Physics":
            average += mark2[sub] * 2
            total += 2
        elif sub == "Geometry":
            average += mark2[sub] * 2
            total += 2
        elif sub == "Algebra":
            average += mark2[sub] * 2
            total += 2
        else:
            average += mark2[sub]
            total += 1

    for sub in mark3:
        if sub == "name":
            pass
        elif sub == "Physics":
            average += mark3[sub] * 2
            total += 2
        elif sub == "Geometry":
            average += mark3[sub] * 2
            total += 2
        elif sub == "Algebra":
            average += mark3[sub] * 2
            total += 2
        else:
            average += mark3[sub]
            total += 1

    for sub in mark4:
        if sub == "name":
            pass
        elif sub == "Physics":
            average += mark4[sub] * 2
            total += 2
        elif sub == "Geometry":
            average += mark4[sub] * 2
            total += 2
        elif sub == "Algebra":
            average += mark4[sub] * 2
            total += 2
        else:
            average += mark4[sub]
            total += 1
    return average / total


def sort(students):
    total_averages = {}
    sorted_students = {}
    for student in students:
        total_averages[student] = students[student]["Total average"]
    total_averages = {k: rem for k, rem in sorted(total_averages.items(), key=lambda item: item[1], reverse=True)}
    for student in total_averages:
        sorted_students[student] = students[student]
    return sorted_students


def save_ods(students, filename):
    data = {"Sheet1": []}
    data["Sheet1"].append(["Name", "Academics", "IELTS", "Interview", "Total average"])
    for student in students:
        result = [student]
        for marks in students[student].values():
            result.append(marks)
        data["Sheet1"].append(result)
    save_data(filename, data)

def check_result():
    if os.path.exists("result.ods"):
        print("\n[+] The result file has been saved successfully!")
    else:
        print("\n[-] File not saved... Please try again!")

if __name__ == "__main__":
    students_dict = {}
    print("Welcome to the University Data Management Program!")
    input("\nPress Enter to continue...")
    folder = easygui.diropenbox(msg="Choose the Files Directory...")
    acad_t1 = ParseODS(folder+"/Data1.ods")
    acad_t2 = ParseODS(folder+"/Data2.ods")
    acad_t3 = ParseODS(folder+"/Data3.ods")
    acad_t4 = ParseODS(folder+"/Data4.ods")
    ielts = ParseODS(folder+"/IELTS.ods")
    interview = ParseODS(folder+"/Interview.ods")
    for student_name in acad_t1.get_names():
        students_dict[student_name] = {}

    for student in students_dict:
        students_dict[student]["academics"] = academics_average(
            acad_t1.get_student(student),
            acad_t2.get_student(student),
            acad_t3.get_student(student),
            acad_t4.get_student(student)
        )
        students_dict[student]["ielts"] = ielts.get_average(student)
        students_dict[student]["interview"] = interview.get_average(student)

    for student in students_dict.values():
        student["Total average"] = 0.4*(student["academics"]/100)+0.3*(student["ielts"]/9)+0.3*(student["interview"]/10)
    
    students_dict = sort(students_dict)
    save_ods(students_dict, "result.ods")
    check_result()
