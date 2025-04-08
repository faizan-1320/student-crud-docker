from fastapi import FastAPI, HTTPException
from models import StudentCreate, StudentUpdate, StudentResponse
from crud import (
    add_student,
    retrieve_students,
    retrieve_student,
    update_student,
    delete_student,
)

app = FastAPI()


@app.post("/students", response_model=StudentResponse)
def create_student(student: StudentCreate):
    student = add_student(student.dict())
    return student


@app.get("/students", response_model=list[StudentResponse])
def get_students():
    return retrieve_students()


@app.get("/students/{id}", response_model=StudentResponse)
def get_student(id: str):
    student = retrieve_student(id)
    if student:
        return student
    raise HTTPException(status_code=404, detail="Student not found")


@app.put("/students/{id}")
def update_student_data(id: str, student: StudentUpdate):
    updated = update_student(id, student.dict(exclude_unset=True))
    if updated:
        return {"msg": "Student updated successfully"}
    raise HTTPException(status_code=404, detail="Student not found")


@app.delete("/students/{id}")
def delete_student_data(id: str):
    deleted = delete_student(id)
    if deleted:
        return {"msg": "Student deleted successfully"}
    raise HTTPException(status_code=404, detail="Student not found")
