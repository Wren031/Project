from pprint import pprint
from pocketbase.models.utils import BaseModel
from model.Customer import Customer
from model.Cars import Cars

class Transaction(BaseModel):
    customer: Customer
    car: Cars
    duration: int
    borrow_date: str
    return_date: str
    location: str

    def __init__(self, data: dict):
        super().__init__(data)
        self.customer = Customer(data=data['expand']['customer'])
        self.car = Cars(data=data["expand"]['car'])
        self.duration = int(data.get("duration"))
        self.borrow_date = data.get("borrow_date", "")
        self.return_date = data.get("return_date", "")
        self.location = data.get("location", "")
