from dababase.db import pb

from model.Customer import Customer


def get_customer() -> list[Customer]:
    results = pb.collection("customer").get_full_list()
    car = map(lambda x: Customer(x.__dict__["collection_id"]), results)
    return list(car)


def create_customer(
    name: str, birthdate: str, address: str, driver_id: str, number: str, status: str
):
    c = pb.collection("customer").create(
        body_params={
            "name": name,
            "birthdate": birthdate,
            "address": address,
            "driver_id": driver_id,
            "number": number,
            'status': status,
        }
    )
    return Customer(c.__dict__["collection_id"])


def edit_customer():
    pass


def delete_customer():
    pass
