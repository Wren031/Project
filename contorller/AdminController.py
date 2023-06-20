from pocketbase import PocketBase

from model.Admin import Admin
pb = PocketBase('http://localhost:8090')

def get_admin() -> list[Admin]:
    results = pb.collection('users').get_full_list()
    transaction1 = map(lambda x: Admin(
        x.__dict__['collection_id']), results)

    return list(transaction1)