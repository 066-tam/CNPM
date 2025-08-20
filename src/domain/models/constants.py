from enum import Enum

class Role(str, Enum):
    ADMIN = "admin"
    HR = "hr_manager"
    COORDINATOR = "coordinator"
    MENTOR = "mentor"
    INTERN = "intern"