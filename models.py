# models.py
from pydantic import BaseModel, EmailStr
from typing import Optional


class StudentBase(BaseModel):
    name: str
    email: EmailStr
    age: int


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    age: Optional[int]


class StudentResponse(StudentBase):
    id: str
