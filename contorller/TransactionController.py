from dababase.db import pb

from model.Transaction import Transaction

def get_transaction() -> list[Transaction]:
    results = pb.collection("transaction").get_full_list(
         query_params={'expand': 'customer,car'}   
    )
    car = map(lambda x: Transaction(x.__dict__["collection_id"]), results)
    return list(car)


def create_transaction(
    customer: str,
    car: str,
    duration: int,
    borrow_date: str,
    return_date: str,
    location: str,
):
    return pb.collection("transaction").create(
        {
            "customer": customer,
            "car": car,
            "duration": duration,
            "borrow_date": borrow_date,
            "return_date": return_date,
            "location": location,
        }
    )
