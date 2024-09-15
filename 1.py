from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)



class Student(BaseModel):
    id :int
    name : str
    grade :int 
    
students = [
    Student(id=22,name="khalil",grade=4),
    Student(id = 15,name ="ibrahim",grade =3),
    Student(id = 56,name ="aymen",grade =5)
]


@app.get("/student/")
def read_stud():
    return students



@app.post("/student/")
def create_stud(New_Student : Student):
    students.append(New_Student)
    return New_student


@app.put("/student/{student_id}")
def update_stud(student_id:int,update_student:Student):
    for index , student in enumerate(student):
        if student.id == student_id : 
            students[index] = update_student
            return update_student
    return {"error":"Student not found "}


@app.delete("/student/{student_id}")
def update_stud(student_id:int):
    for index , student in enumerate(students):
        if student.id == student_id : 
            del students[index]
            {"message":"Student deleted"}
    return {"error":"Student not found "}