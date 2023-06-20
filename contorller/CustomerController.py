from pocketbase import PocketBase

from model.Customer import Customer

pb = PocketBase('http://localhost:8090')


def get_customer_transaction() -> list[Customer]:
    results = pb.collection('customer_transaction').get_full_list()
    transaction1 = map(lambda x: Customer(
        x.__dict__['collection_id']), results)

    return list(transaction1)


def create_customer_transaction(name: str,
                                age: int,
                                address: str,
                                driver_id: str,
                                days: int,
                                location: str,
                                cars: str,
                                price: float,
                                contact: str,
                            ):    
    
    pb.collection('customer_transaction').create({
        'name': name,
        'age' : age,
        'address': address,
        'driver_id' : driver_id,
        'location': location,
        'days': days,
        'cars': cars,
        'price': price,
        'contact': contact,
        })
    