import flet as ft
from flet import UserControl
from model.Customer import Customer
from pocketbase import PocketBase

pb = PocketBase("http://localhost:8090")
from view.components.dataTable import dt


class CustomerTransaction(UserControl):
    def __init__(self, customer: Customer, root=None):
        super().__init__(
            None
        )  # Pass 'None' as the argument to the superclass constructor
        self.customer = customer
        self.dlg_modal = None
        self.refp = self
        self.root = root  # Assign the 'root' argument to an instance variable

        self.dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Please confirm"),
            content=ft.Text("Do you really want to delete all those files?"),
            actions=[
                ft.TextButton("Yes", on_click=None),
                ft.TextButton("No", on_click=None),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )

    def open_dlg_modal(self, event=None):
        if self.root is not None:
            self.root.dialog = self.dlg_modal
            self.dlg_modal.open = True
            self.root.update()

    def build(self):
        return ft.Container(
            content=dt.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(self.customer.created)),
                        ft.DataCell(ft.Text(self.customer.name)),
                        ft.DataCell(ft.Text(self.customer.address)),
                        ft.DataCell(ft.Text(self.customer.location)),
                        ft.DataCell(ft.Text(self.customer.driver_id)),
                        ft.DataCell(ft.Text(self.customer.age)),
                        ft.DataCell(ft.Text(self.customer.cars)),
                        ft.DataCell(ft.Text(self.customer.price)),
                    ]
                )
            )
        )
