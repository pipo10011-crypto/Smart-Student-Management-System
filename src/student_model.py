from dataclasses import dataclass


@dataclass
class Student:
    student_id: int
    name: str
    age: int
    department: str
    level: int
    gpa: float