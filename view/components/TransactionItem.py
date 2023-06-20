import flet as ft
from model.Cars import Cars

from pocketbase import PocketBase
from view.components.dataTable import car_variant

pb = PocketBase('http://localhost:8090')


class TransactionItem(ft.UserControl):
    def __init__(self, transaction: Cars, root: ft.View):
        super().__init__(root)
        self.transaction = transaction
        self.dlg_modal = None
        self.refp = self

        
        self.days = ft.TextField(label='Input Days', value='0',width=200)
        
        self.cash = ft.TextField(label='Input Cash', value='0',width=250)
        
        self.vw_totaltext = ft.Text(f'P {0}',
                                weight=ft.FontWeight.W_900,
                                size=30)
        
        self.Name = ft.TextField(label='Enter full name',width=350)
        self.address = ft.TextField(label='Address',width=350)
        self.age = ft.TextField(label='Age',width=200)
        self.id_driver = ft.TextField(label='ID No',width=350)
        
        
    def confirm_payment(self,_):
        self.days.value = int(self.days.value)
        self.cash_var = int(self.cash.value)
        self.vw_totaltext = f'P {self.days.value * self.transaction.price}'
        self.cash_var = int(self.cash.value) - (self.days.value * self.transaction.price)
        print(self.vw_totaltext)
        print('change',self.cash_var)
        
        
    def build(self):
        return ft.Container(
            
        )
    

    def edit_details(self):
        return ft.Container(
            on_click=self.item,
            content=ft.Container(
                ft.Row([
                    ft.Text(self.transaction.car_model,size=32)
                ])
            )
        )
    
    def item(self):
        print(self.transaction)
        

    product_listview = ft.GridView(
        expand=5,
        runs_count=5,
        max_extent=640,
        child_aspect_ratio=2.0,
        spacing=0,
        run_spacing=0
    )

    def delete_data(self):
        pb.collection('users').auth_with_password('user', '12345678')
        pb.collection('car_model').delete(self.transaction.id)
