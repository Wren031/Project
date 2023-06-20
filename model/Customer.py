from pocketbase.models.utils import BaseModel

class Customer(BaseModel):
    name: str
    birthdate: str
    address: str
    driver_id: str
    number: str
    status: str
    
    def __init__(self, data: dict):

        super().__init__(data)
        self.status = data.get('status', '')
        self.name = data.get('name','')
        self.birthdate = data.get('birthdate','')
        self.address = data.get('address','')
        self.driver_id = data.get('driver_id','')
        self.number = data.get('number','')
        
        