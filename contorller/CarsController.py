from pocketbase import PocketBase

from model.Cars import Cars

pb = PocketBase("http://localhost:8090")

pb.collection("users").auth_with_password("user", "12345678")


def get_trasaction() -> list[Cars]:
    results = pb.collection("cars").get_full_list()
    transaction = map(lambda x: Cars(x.__dict__["collection_id"]), results)

    return list(transaction)


def create_car(
    fuel_type: str,
    date_model: str,
    seats: str,
    car_model: str,
    price: float,
    image: str,
    status: str,
    stock: int
):
   return pb.collection("cars").create(
        {
            "fuel_type": fuel_type,
            "date_model": date_model,
            "seats": seats,
            "car_model": car_model,
            "price": price,
            "image": image,
            'status': status,
            'stock': stock
        },
        
)


    


   

