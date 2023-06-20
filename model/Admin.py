from pocketbase.models.utils import BaseModel

class Admin(BaseModel):
    avatar: str
    name: str
    username: str
    email: str

    def __init__(self, data: dict):
        super().__init__(data)
        self.avatar = data.get('avatar', '')
        self.name = data.get('name', '')
        self.username = data.get('username','')
        self.email = data.get('email','')
