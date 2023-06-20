import flet as ft
from view.AppPage import AppPage
from contorller.CustomerController1 import get_customer
from view.components.dataTable import customer

from dababase.db import pb

class CustomerPage(AppPage):
    def __init__(self, root, route):
        super().__init__(root=root, route=route)
        
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        
        self.appbar = ft.AppBar(
            leading_width=40,
            title=ft.Row([
                ft.IconButton(
                icon=ft.icons.ARROW_BACK,
                icon_color="black",
                icon_size=30,
                on_click=lambda _: self.root.go("/MainMenuPage")),
                ft.Text("CUSTOMER TRANSACTION", size=23, weight='bold', color='black'),
                ]),
            center_title=False,
            bgcolor=ft.colors.SECONDARY_CONTAINER,
            actions=[
            ],
        )

        self.customer_list_view = ft.Ref[ft.ListView]()

        self.page.controls = [
            self.appbar,
            customer,
            ft.Container(
                padding=10,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BROWN_100,
                content=ft.Row(
                    controls=[
                        ft.ListView(ref=self.customer_list_view),
                    ]
                )
            )
        ]
    
        self.page.did_mount = self.load_transaction
        
    def delete_car(self, item_id):
        result = pb.collection("customer").delete(item_id)
        self.load_transaction()
        self.customer_list_view.current.controls.clear()
        customer.rows.clear()
        self.root.update()
    
    def load_transaction(self):
        customer.rows.clear()
        products = get_customer()
        self.customer_list_view.current.controls.clear()
        for i in products:
            customer.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(i.created)),
                        ft.DataCell(ft.Text(i.name)),
                        ft.DataCell(ft.Text(i.address)),
                        ft.DataCell(ft.Text(i.driver_id)),
                        ft.DataCell(ft.Text(i.number)),
                        ft.DataCell(ft.Text(i.birthdate)),
                        ft.DataCell(ft.Text(i.status)),
                    ]
                )
            )
        self.customer_list_view.current.update()
