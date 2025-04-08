from bson import ObjectId
from db import student_collection


def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "name": student["name"],
        "email": student["email"],
        "age": student["age"],
    }


# CREATE
def add_student(student_data: dict) -> dict:
    student = student_collection.insert_one(student_data)
    new_student = student_collection.find_one({"_id": student.inserted_id})
    return student_helper(new_student)


# READ ALL
def retrieve_students():
    students = []
    for student in student_collection.find():
        students.append(student_helper(student))
    return students


# READ ONE
def retrieve_student(id: str) -> dict:
    student = student_collection.find_one({"_id": ObjectId(id)})
    if student:
        return student_helper(student)


# UPDATE
def update_student(id: str, data: dict):
    if len(data) < 1:
        return False
    student = student_collection.find_one({"_id": ObjectId(id)})
    if student:
        student_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        return True
    return False


# DELETE
def delete_student(id: str):
    student = student_collection.find_one({"_id": ObjectId(id)})
    if student:
        student_collection.delete_one({"_id": ObjectId(id)})
        return True
    return False
