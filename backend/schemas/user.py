from pydantic import BaseModel

class UserPublic(BaseModel):
    email: str
    name: str


    class Config:
        from_attributes = True
