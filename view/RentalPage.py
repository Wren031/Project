import flet as ft
from view.AppPage import AppPage

from contorller.TransactionController import get_transaction
from view.components.dataTable import transaction_data
from model.Transaction import Transaction
from dababase.db import pb

class RentalPage(AppPage):
    def __init__(self, root, route):
        super().__init__(root=root, route=route)
        
        self.transaction_status = ft.Ref[ft.RadioGroup]()

        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.appbar = ft.AppBar(
            leading_width=40,
            title=ft.Row([
                ft.IconButton(
                icon=ft.icons.ARROW_BACK,
                icon_color="black",
                icon_size=30,
                on_click=lambda _: self.root.go("/MainMenuPage")),
                ft.Text("TRANSACTION HISTORY", size=23, weight='bold', color='black'),
                ]),
            center_title=False,
            bgcolor=ft.colors.SECONDARY_CONTAINER,
            actions=[
            ],
        )

        self.customer_list_view = ft.Ref[ft.ListView]()

        self.page.controls = [
            self.appbar,
            transaction_data,
            ft.Container(
                padding=10,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BROWN_100,
                content=ft.Row(
                    controls=[
                        ft.ListView(ref=self.customer_list_view),
                    ]
                ),
            ),
        ]

        self.page.did_mount = self.load_transaction
        
    def show_dlf(self, item: Transaction):
        self.dlg = ft.AlertDialog(
            open=True,
            title=ft.Text(item.customer.id),
        actions=[
            ft.Column([
              ft.ElevatedButton(
                            "DELETE",
                            icon="delete",
                            icon_color="red",
                            on_click=lambda _: self.delete_car(item.id), width=300),   
                        ])
                    ]
                )

        self.root.dialog = self.dlg
        self.dlg.open = True
        self.root.update()
        
    def delete_car(self, item_id):
        self.dlg.open = False
        self.dlg.update()
        pb.collection("transaction").delete(item_id)
        self.page.update()
        self.root.dialog = self.dlg
        self.load_transaction()
        self.root.update()

    def load_transaction(self):
        transaction_data.rows.clear()
        products = get_transaction()
        self.customer_list_view.current.controls.clear()
        ui = map(
        lambda i: ft.Container(
            content=transaction_data.rows.append(
                ft.DataRow(
                    cells=[
                            ft.DataCell(ft.Text(i.created)),
                            ft.DataCell(ft.Text(i.customer.name)),
                            ft.DataCell(ft.Text(i.car.car_model)),
                            ft.DataCell(ft.Text(f'{i.duration} Days')),
                            ft.DataCell(ft.Text(i.location)),
                            ft.DataCell(ft.Text(f'Start Date {i.borrow_date}')),
                            ft.DataCell(ft.Text(f'Return Date {i.return_date}')),
                              ft.DataCell(ft.Container(
                              margin=0,
                              padding=0,
                              bgcolor=ft.colors.BLUE_300,
                              width=150,
                              border_radius=0,
                              content=ft.Row(
                                      [
                                      ft.TextButton('Delete', width=150,
                                       on_click=lambda _: self.show_dlf(
                                      item=i),
                                      )

                                      ], alignment=ft.MainAxisAlignment.CENTER,
                                  ))),
                        ])
                ),
            ), products,
        )
        for i in list(ui):
            self.customer_list_view.current.controls.append(i)
        self.customer_list_view.current.update(),

