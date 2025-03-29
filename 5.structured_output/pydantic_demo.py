from pydantic import BaseModel, Field, EmailStr,PositiveFloat
from typing import List, Optional


class Student(BaseModel):
    name: str = "Kamesh"
    age: Optional[int] = None
    email: EmailStr 
    cgpa : PositiveFloat = Field(default=None, gt=0, lt=10,description="CGPA should be between 0 and 10")

new_student = {'age':'21','email':'kamesh@g.com'}

student = Student(**new_student)
print(student)
print(student.model_dump_json())
