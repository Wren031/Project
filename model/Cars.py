from pocketbase.models.utils import BaseModel

class Cars(BaseModel):
    fuel_type: str
    date_model: str
    seats: str
    car_model: str
    price: float
    image: str
    status: str
    stock: int


    def __init__(self, data: dict):
        super().__init__(data)
        self.stock = int(data.get('stock',0))
        self.status = data.get('status','')
        self.image = data.get('image','')
        self.fuel_type = data.get('fuel_type', '')
        self.date_model = data.get('date_model', '')
        self.seats = data.get('seats', '')
        self.car_model = data.get('car_model', '')
        self.price = float(data.get('price', 0))

        
        



