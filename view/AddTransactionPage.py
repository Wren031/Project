import flet as ft
from view.AppPage import AppPage

from contorller.CarsController import get_trasaction, create_car
from view.components.dataTable import car_variant
from model.Cars import Cars
from dababase.db import pb
from view.InquirePage import peending

class AddTransactionPage(AppPage):

    def invalid_keyword(self):
        self.root.snack_bar = ft.SnackBar(ft.Text(f"Invalid Keyword"))
        self.root.snack_bar.open = True
        self.root.update()
        
    def edit_done(self):
        self.dlg = ft.AlertDialog(
                open=True,
                title=ft.Text('Edit Succsessfully',size=25,weight='bold',color='green'),
            )
        self.root.dialog = self.dlg
        self.dlg.open = True
        self.root.update()
        
    def edit_done1(self):
        self.dlg = ft.AlertDialog(
                open=True,
                title=ft.Text('Deleted Succsessfully',size=25,weight='bold',color='green')
            )
        self.root.dialog = self.dlg
        self.dlg.open = True
        self.root.update()

    def on_create(self, e):

        if self.tansaction_price == '':
            self.invalid_keyword()
        else:
            price = self.tansaction_price.current.value

        if self.tansaction_seats == '':
            self.invalid_keyword()
        else:
            seats = self.tansaction_seats.current.value

        if self.transaction_stock == '':
            self.invalid_keyword()
        else:
            stock = self.transaction_stock.current.value
        fuel_type = self.tansaction_fuel_type.current.value
        date_model = self.tansaction_date_model.current.value

        car_model = self.tansaction_car_model.current.value

        image = self.transaction_image.current
        status = self.transaction_status.current.value

        stock = 0 if stock is None else int(stock)
        status = '' if status is None else status
        image = "" if image is None else image
        fuel_type = "" if fuel_type is None else fuel_type
        date_model = "" if date_model is None else date_model
        seats = "" if seats is None else seats

        try:
            stock = 0 if stock is None or stock == '' else int(stock)
        except ValueError:
            self.invalid_keyword()
            return

        try:
            seats = 0 if seats is None or seats == '' else int(seats)
        except ValueError:
            self.invalid_keyword()
            return

        try:
            price = 0 if price is None or price == '' else float(price)
        except ValueError:
            self.invalid_keyword()
            return

        e.control.page.dialog = self.dlg_modal
        e.control.page.dialog.open = False
        self.dlg_modal.update()
        e.control.page.update()

        create_car(
            fuel_type=fuel_type,
            date_model=date_model,
            seats=seats,
            car_model=car_model,
            image=image,
            price=price,
            status=status,
            stock=stock,
        )

        self.load_transaction()

        self.tansaction_date_model.current.value = ""
        self.tansaction_seats.current.value = ""
        self.tansaction_fuel_type.current.value = ""
        self.tansaction_price.current.value = ""
        self.tansaction_car_model.current.value = ""
        self.tansaction_fuel_type.current.value=''
        self.transaction_stock.current.value=''
        e.control.page.dialog = self.dlg_modal
        e.control.page.dialog.open = False
        e.control.page.update()
        e.control.page.update()

    def __init__(self, root, route):
        super().__init__(root=root, route=route)

        self.page.scroll = ft.ScrollMode.ALWAYS

        self.transaction_stock = ft.Ref[ft.RadioGroup]()
        self.tansaction_list_view = ft.Ref[ft.ListView]()
        self.tansaction_fuel_type = ft.Ref[ft.RadioGroup]()
        self.tansaction_date_model = ft.Ref[ft.TextField]()
        self.tansaction_seats = ft.Ref[ft.TextField]()
        self.tansaction_car_model = ft.Ref[ft.TextField]()
        self.tansaction_price = ft.Ref[ft.TextField]()
        self.transaction_image = ft.Ref[ft.ListView]()

        self.transaction_status = ft.Ref[ft.RadioGroup]()

        def close_dlg(e):   
            e.control.page.dialog = self.dlg_modal
            e.control.page.dialog.open = False
            e.control.page.update()

        self.dlg_modal = ft.AlertDialog(
            content=ft.Column([
                ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=close_dlg),
                ft.Text("Add New Car Variant", color="black",
                    size=25,),
                ft.Container(
                    margin=0,
                    padding=0,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.WHITE,
                    width=350,
                    height=450,
                    border_radius=0,
                    content=ft.Column([
                        ft.Container(content=ft.Row(
                            [
                                ft.TextField(label="Car Model",
                                     ref=self.tansaction_car_model,
                                     width=250,height=55),
                                ft.TextField(label="Date Model",
                                     ref=self.tansaction_date_model,
                                     width=250,height=55),
                            ])
                        ),
                        ft.Divider(),
                        ft.Container(content=ft.Row(
                            [
                                ft.TextField(label="Seat Capacity",
                                     ref=self.tansaction_seats,
                                     width=250,height=55),
                                ft.TextField(label="Price",
                                     ref=self.tansaction_price,
                                    width=250,height=55),
                            ])
                        ),
                        ft.Divider(),
                        ft.Text("Fuel Type", size=18),
                        ft.Container(content=ft.RadioGroup(
                            content=ft.Row([ft.Radio(
                                value="Petrol", label="Petrol"),
                                ft.Radio(value="Unleaded", label="Unleaded"),
                                ft.Radio(value="Diesel", label="Diesel"),
                            ]), ref=self.tansaction_fuel_type,
                        )),
                        ft.Container(content=ft.RadioGroup(
                            content=ft.Row([ft.Radio(
                                value=1, label="Stock"),
                            ]), ref=self.transaction_stock)
                        ),
                        ft.Text('Status', size=18),
                        ft.Container(content=ft.RadioGroup(
                            content=ft.Row([ft.Radio(
                                value="Available", label="Available"),
                                ft.Radio(value="Not Available",
                                         label="Not Available"),
                                ft.Radio(value="Under Maintenance",
                                         label="Under Maintenance"),
                            ]), ref=self.transaction_status),
                        )],
                    )),
            ], height=550,width=500,
            ),
            # BUTTON AFTER CREATE THE TRANSACTION UI
            actions=[
                ft.Divider(),
                ft.Row(
                    [
                        ft.Container(
                            margin=0,
                            padding=0,
                            alignment=ft.alignment.center,
                            bgcolor=ft.colors.GREEN_ACCENT_200,
                            width=350,
                            border_radius=0,
                            content=ft.TextButton(
                                "Save Car", on_click=self.on_create, width=350
                            ),
                        )
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.CENTER,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )

        def show_banner_click(e):
            e.control.page.dialog = self.dlg_modal
            e.control.page.dialog.open = True
            e.control.page.update()

        self.pending_dlg = ft.AlertDialog(
            title=ft.Text('Pending List', size=23,
                          color='black', weight='bold'),
            content=ft.Container(width=500, height=360, content=ft.Column(controls=[
                peending
            ])
            )
        )

        def pending_list(e):
            e.control.page.dialog = self.pending_dlg
            e.control.page.dialog.open = True
            e.control.page.update()

        self.appbar = ft.AppBar(
            leading_width=40,
            title=ft.Row([
                ft.IconButton(
                icon=ft.icons.ARROW_BACK,
                icon_color="black",
                icon_size=30,
                on_click=lambda _: self.root.go("/MainMenuPage")),
                ft.Text("Availabe Car Variants", size=23, weight='bold', color='black'),
                ]),
            center_title=False,
            bgcolor=ft.colors.SECONDARY_CONTAINER,
            actions=[
                ft.IconButton(icon=ft.icons.SHOPPING_CART_ROUNDED,
                              on_click=pending_list,
                              ),
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(
                            text="Admin",
                            on_click=None,
                            icon=ft.icons.ADMIN_PANEL_SETTINGS_OUTLINED,
                        ),
                        ft.PopupMenuItem(
                            text="Add New Car",
                            on_click=show_banner_click,
                            icon=ft.icons.CAR_RENTAL,
                        ),
                    ]
                ),
            ],
        )
        self.page.did_mount = lambda: self.load_transaction()

        self.page.controls = [
            ft.Divider(),
            car_variant,
            ft.ListView(ref=self.tansaction_list_view),
            self.appbar,
        ]
        self.page.did_mount = self.load_transaction

    def delete_car(self, item_id):
        self.dlg.open = False
        self.dlg.update()
        self.tansaction_list_view.current.controls.clear()
        pb.collection("cars").delete(item_id)
        self.page.update()
        self.edit_done1()
        self.root.dialog = self.dlg
        self.load_transaction()
        self.root.update()

    def update_status(self, item_id):

        if self.tansaction_price == '':
            self.invalid_keyword()
        else:
            price = self.tansaction_price.current.value

        if self.tansaction_seats == '':
            self.invalid_keyword()
        else:
            seats = self.tansaction_seats.current.value

        try:
            seats = 0 if seats is None or seats == '' else int(seats)
        except ValueError:
            self.invalid_keyword()
            return

        try:
            price = 0 if price is None or price == '' else float(price)
        except ValueError:
            self.invalid_keyword()
            return

        self.dlg.open = False
        self.dlg.update()
        print(item_id)
        pb.collection("users").auth_with_password("user", "12345678")
        results = pb.collection("cars").update(
            item_id,
            {
                'status': self.transaction_status.current.value,
                'stock': self.transaction_stock.current.value
            }
        )
        self.tansaction_list_view.current.controls.clear()
        self.edit_done()
        self.root.dialog = self.dlg
        self.root.update()
        self.load_transaction()
        self.page.update()

    def save_data(self, item_id):
        if self.tansaction_price == '':
            self.invalid_keyword()
        else:
            price = self.tansaction_price.current.value

        if self.tansaction_seats == '':
            self.invalid_keyword()
        else:
            seats = self.tansaction_seats.current.value

        try:
            seats = 0 if seats is None or seats == '' else int(seats)
        except ValueError:
            self.invalid_keyword()
            return

        try:
            price = 0 if price is None or price == '' else float(price)
        except ValueError:
            self.invalid_keyword()
            return

        self.dlg.open = False
        self.dlg.update()
        print(item_id)
        pb.collection("users").auth_with_password("user", "12345678")
        results = pb.collection("cars").update(
            item_id,
            {"car_model": self.tansaction_car_model.current.value,
             "price": self.tansaction_price.current.value,
             'seats': self.tansaction_seats.current.value,
             'date_model': self.tansaction_date_model.current.value,
             'fuel_type': self.tansaction_fuel_type.current.value,
             }
        )
        self.tansaction_list_view.current.controls.clear()
        self.edit_done()
        self.root.dialog = self.dlg
        self.root.update()
        self.load_transaction()
        self.page.update()

    def show_dlf(self, item: Cars):
        self.dlg = ft.AlertDialog(
            open=True,
            title=ft.Text(item.car_model),
            content=ft.Column([
                ft.Text('Update Status', size=23, weight='bold'),
                ft.Container(content=ft.RadioGroup(
                    content=ft.Row([
                        ft.Radio(value=1, label="Available"),
                        ft.Radio(
                            value=0, label="Not Available"),
                    ]), ref=self.transaction_stock)
                ),
                ft.Divider(),
                ft.Text('Status', size=18),
                ft.Container(
                    content=ft.RadioGroup(
                        content=ft.Row([
                            ft.Radio(
                                value="Available", label="Available"),
                            ft.Radio(
                                value="Not Available", label="Not Available"),
                            ft.Radio(
                                value="Under Maintenance", label="Under Maintenance"),
                        ]),
                        ref=self.transaction_status)),
            ]),
            actions=[
                ft.ElevatedButton(
                    "SAVE",
                    icon="save",
                    icon_color="green",
                    on_click=lambda _: self.update_status(item.id), width=450),
            ]
        )
        self.root.dialog = self.dlg
        self.dlg.open = True
        self.root.update()

    def show_dialog(self, item: Cars):
        self.dlg = ft.AlertDialog(
            open=True,
            title=ft.Container(
                content=ft.Column(horizontal_alignment=ft.CrossAxisAlignment.START,
                                  controls=[
                                      ft.Text(
                                          f"Car Model -> {item.car_model}", size=24, weight="bold", color="black"),
                                      ft.Divider(),
                                  ])
            ),
            content=ft.Column(width=600, height=360,
                              controls=[
                                  ft.Container(content=ft.Row(
                                      [
                                          ft.TextField(label="Input New Model",
                                                       ref=self.tansaction_car_model,
                                                       width=300, height=50),
                                          ft.TextField(label="Input New Date Model",
                                                       ref=self.tansaction_date_model,
                                                       width=300, height=50),
                                      ]
                                  )),
                                  ft.Container(content=ft.Row(
                                      [
                                          ft.TextField(label="Input New Capacity",
                                                       ref=self.tansaction_seats,
                                                       width=300, height=50),
                                          ft.TextField(label="Input New Price",
                                                       ref=self.tansaction_price,
                                                       width=300, height=50),
                                      ])
                                  ),
                                  ft.Divider(),
                                  ft.Text("Fuel Type", size=18),
                                  ft.Container(
                                      content=ft.RadioGroup(
                                          content=ft.Row([
                                              ft.Radio(
                                                  value="Petrol", label="Petrol"),
                                              ft.Radio(
                                                  value="Unleaded", label="Unleaded"),
                                              ft.Radio(
                                                  value="Diesel", label="Diesel"),
                                          ]),
                                          ref=self.tansaction_fuel_type)
                                  ),
                                  ft.Divider(),
                              ]),
            actions=[
                ft.Container(content=ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            "DELETE",
                            icon="delete",
                            icon_color="red",
                            on_click=lambda _: self.delete_car(item.id), width=300),
                        ft.ElevatedButton(
                            "SAVE",
                            icon="save",
                            icon_color="green", on_click=lambda _: self.save_data(item.id), width=300),
                    ])
                )], actions_alignment=ft.MainAxisAlignment.END)
        self.root.dialog = self.dlg
        self.dlg.open = True
        self.root.update()

    def load_transaction(self):
        car_variant.rows.clear()
        products = get_trasaction()
        self.tansaction_list_view.current.controls.clear()
        ui = map(
            lambda i: ft.Container(
                content=car_variant.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(i.id)),
                            ft.DataCell(ft.Text(i.car_model)),
                            ft.DataCell(ft.Text(i.date_model)),
                            ft.DataCell(ft.Text(i.price)),
                            ft.DataCell(ft.Text(i.seats)),
                            ft.DataCell(ft.Text(i.fuel_type)),
                            ft.DataCell(ft.Container(
                                on_click=lambda _: self.show_dlf(
                                    item=i),
                                content=ft.Row(
                                    [
                                        ft.Text(i.status),
                                    ]
                                )
                            )),
                            ft.DataCell(ft.Container(
                                margin=0,
                                padding=0,
                                bgcolor=ft.colors.GREEN_400,
                                width=100,
                                border_radius=0,
                                content=ft.Row(
                                        [
                                            ft.TextButton('Edit', width=100,
                                                          on_click=lambda _: self.show_dialog(
                                                              item=i),
                                                          ),
                                        ], alignment=ft.MainAxisAlignment.CENTER,
                                        ))),
                        ])
                ),
            ), products,
        )
        for i in list(ui):
            self.tansaction_list_view.current.controls.append(i)
        self.tansaction_list_view.current.update(),
