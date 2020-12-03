from pydantic import BaseModel

"""
aca estamos creando la clase UserIn y UserOut que hereda o extiende de la clase padre (BaseModel)
"""

class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str
    balance: int