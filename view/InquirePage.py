from view.components.dataTable import customer_list_view
import flet as ft
from view.AppPage import AppPage
from model.Transaction import Transaction
from model.Cars import Cars
from model.Customer import Customer
from contorller.CarsController import get_trasaction
from contorller.TransactionController import create_transaction
from contorller.CustomerController1 import create_customer, get_customer
from dababase.db import pb


avail_recipt_transaction = ft.ListView()
avail_recipt_information = ft.ListView()
peending = ft.ListView()


class InquirePage(AppPage):

    product_listview = ft.GridView(
        expand=5,
        runs_count=5,
        max_extent=500,
        child_aspect_ratio=1.0,
        spacing=0,
        run_spacing=0,
    )

    def invalid_keyword(self):
        self.dlg = ft.AlertDialog(
            open=True,
            title=ft.Text('Not Available!!', size=25,
                          weight='bold', color='red900')
        )
        self.root.dialog = self.dlg
        self.dlg.open = True
        self.root.update()

    def recipt_dlg(self):
        self.dlg = ft.AlertDialog(
            open=True,
            title=ft.Text(),
            content=ft.Container(
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    width=400, height=500, controls=[
                        avail_recipt_transaction,
                        avail_recipt_information,
                        ft.Divider(),
                        ft.Text(''),
                        ft.Text('   Thank You', size=25,
                                weight='bold', color='green'),
                    ])
            )
        )
        self.root.dialog = self.dlg
        self.dlg.open = True
        self.root.update()

    def __init__(self, root, route):
        super().__init__(root=root, route=route)

        self.transaction_age = ft.Ref[ft.RadioGroup]()
        self.transaction_address = ft.Ref[ft.TextField]()
        self.transaction_driver = ft.Ref[ft.TextField]()
        self.transaction_days = ft.Ref[ft.TextField]()
        self.transaction_location = ft.Ref[ft.TextField]()
        self.transaction_name = ft.Ref[ft.TextField]()
        self.transaction_number = ft.Ref[ft.TextField]()
        self.tansaction_status = ft.Ref[ft.RadioGroup]()
        self.transaction_start = ft.Ref[ft.TextField]()
        self.transaction_end = ft.Ref[ft.TextField]()
        
        self.transaction_status = ft.Dropdown(
            label='Status',
            width=270,
            height=35,
            options=[
                ft.dropdown.Option("Approve"),
                ft.dropdown.Option("Decline"),
                ft.dropdown.Option("Pending"),
            ],
        )

        self.customer_list_view = ft.Ref[ft.ListView]()
        self.page.scroll = ft.ScrollMode.ALWAYS

        self.appbar = ft.AppBar(
            leading_width=40,
            title=ft.Row([
                ft.IconButton(
                icon=ft.icons.ARROW_BACK,
                icon_color="black",
                icon_size=30,
                on_click=lambda _: self.root.go("/MainMenuPage")),
                ft.Text("BOOK THE BEST CAR FOR YOU", size=23, weight='bold', color='black'),
                ]),         
            center_title=False,
            bgcolor=ft.colors.SECONDARY_CONTAINER,
            actions=[
            ]
        )

        textcontainer = ft.Container(
            margin=30,
            alignment=ft.alignment.center,
            content=ft.Container(
                ft.Column([
                    ft.Text('LETS GET', size=45, weight='bold', color='red'),
                    ft.Text('   ON THE ROAD', size=45,
                            weight='bold', color='white')
                ])
            )
        )
        myimagecontainer = ft.Container(
            alignment=ft.alignment.center,
            content=ft.Stack(
                [
                    textcontainer,
                ]
            )
        )
        self.page.controls = [
            self.appbar,
            ft.ResponsiveRow(
                vertical_alignment=ft.CrossAxisAlignment.STRETCH,
                controls=[
                    ft.Column(col=9, controls=[self.product_listview]),
                    ft.Column(
                        col=3,
                        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                        controls=[ft.Column(controls=[
                                ft.Container(
                                    margin=1,
                                    padding=1,
                                    bgcolor=ft.colors.BLACK,
                                    width=350,
                                    height=1200,
                                    border_radius=1,
                                    content=ft.Column(controls=[
                                ft.Container(
                                    margin=1,
                                    padding=1,
                                    bgcolor=ft.colors.WHITE,
                                    width=350,
                                    height=1200,
                                    border_radius=10,
                                        content=ft.Column(controls=[
                                        customer_list_view,
                                        ft.ListView(ref=self.customer_list_view),
                                        ])
                                    ),
                            ])),
                        ])]
                    ),
                ]
            ),
        ]
        self.page.did_mount = self.load_cars

    def close(self, _):
        self.page.dialog = self.dlg
        self.dlg.open = False
        self.root.go('/CashierPage')
        self.page.update()

    def avail_transaction(self, i: Cars):
        
        age = self.transaction_age.current.value
        days = self.transaction_days.current.value

        if age == '':
            self.invalid_keyword()
        else:
            age = self.transaction_age.current.value

        if days == '':
            self.invalid_keyword()
        else:
            days = self.transaction_days.current.value   
                 
        address = self.transaction_address.current.value
        driver = self.transaction_driver.current.value

        name = self.transaction_name.current.value
        contact = self.transaction_number.current.value
        start = self.transaction_start.current.value
        end = self.transaction_end.current.value
        distanation = self.transaction_location.current.value
        status = self.transaction_status.value if self.transaction_status else ''

        cars = self.list_view
        price = self.price_view
        
        price = float(price)
        days = int(days)
        total = price * days
        
        self.peending = i.car_model
        peending.controls.append(
            ft.Container(
                ft.Column(controls=[
                    ft.Text(f'Pending... {i.car_model}', size=23)
                ])
            )
        )
        print(total)
        avail_recipt_information.controls.append(
            ft.Container(ft.Column(controls=[
                ft.Text(f'Full Name: {name}', size=15),
                ft.Text(f'Contact No: {contact}', size=15),
                ft.Text(f'Destination: {distanation}', size=15),
                ft.Text(f'Age: {age}', size=15),
                ft.Text(f'Address: {address}', size=15),
                ft.Text(f'Driver license: {driver}', size=15),
                ft.Text(f'Days Rent: {days}', size=15),
                ft.Text(f'Total Coast: {total}', size=15),
            ])
            )
        )
        self.page.dialog = self.dlg
        self.page.dialog.open = False
        self.dlg.update()
        self.root.snack_bar = ft.SnackBar(ft.Text("Submited Successfully"))
        self.root.snack_bar.open = True
        self.root.update()

        contact = '' if contact is None else contact
        name = '' if name is None else name
        distanation = '' if distanation is None else distanation
        age = ' 12:00:00.000Z' if age is None else age
        address = '' if address is None else address
        driver = '' if driver is None else driver
        days = 0 if days is None else int(days)
        cars = '' if cars is None else cars
        price = 0 if price is None else float(price)
        start = ' 12:00:00.000Z' if start is None else start
        end = ' 12:00:00.000Z' if end is None else end

        self.transaction_age.current.value = ''
        self.transaction_address.current.value = ''
        self.transaction_driver.current.value = ''
        self.transaction_days.current.value = ''
        self.transaction_name.current.value = ''
        self.transaction_number.current.value = ''
        self.transaction_driver.current.value = ''
        self.transaction_location.current.value = ''
        # Customer Transaction
        customer = create_customer(
            name=name,
            birthdate=age,
            address=address,
            driver_id=driver,
            number=contact,
            status=status
        )
        create_transaction(
            customer=customer.id,
            car=i.id,
            duration=days,
            borrow_date=start,
            return_date=end,
            location=distanation,
        )
        self.recipt_dlg()
        self.customer_list()
        self.page.update()

    def total_coast(self, _):
        days = self.transaction_days.current.value
        days = 0 if days is None else int(days)
        price = float(self.price_view)
        total = price * days
        print(total)
        self.page.update()

    def show_dialog(self, item: Cars):
        avail_recipt_information.controls.clear()
        avail_recipt_transaction.controls.clear()
        if item.stock == 0:
            self.invalid_keyword()
        else:
            self.dlg = ft.AlertDialog(
                open=True,
                title=ft.Container(
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                image_src=f'http://127.0.0.1:8090/api/files/cars/{item.id}/{item.image}?=thumb100x100',
                                height=250,
                                width=450,
                            )
                        ],
                    ),
                ),
                content=ft.Container(
                    width=550,
                    height=650,
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Column([
                                ft.Text(
                                    f'{item.car_model}    P {item.price}', size=23),
                                ft.Divider(),
                                ft.Row([
                                    ft.TextField(
                                        label='Driver Licensed ID ', ref=self.transaction_driver, width=250, height=35),
                                    ft.TextField(
                                        label='Destination', ref=self.transaction_location, width=250, height=35),
                                ]),
                                ft.Row([
                                    ft.TextField(
                                        label='Address', ref=self.transaction_address, width=250, height=35),
                                    ft.TextField(
                                        label='Birthday YY-MM-DD', ref=self.transaction_age, width=250, height=35),
                                ]),
                                ft.Row([
                                    ft.TextField(
                                        label='Duration Days', ref=self.transaction_days, width=250, height=35),
                                    ft.TextField(
                                        label='Name', ref=self.transaction_name, width=250, height=35),
                                ]),
                                ft.Row([
                                    ft.TextField(
                                        label='Contact Number ', ref=self.transaction_number, width=250, height=35),
                                    ft.Row([self.transaction_status]),
                                ]),
                                ft.Column([
                                    ft.TextField(
                                        label='Start date YY-MM-DD', ref=self.transaction_start, width=250, height=32),
                                    ft.TextField(
                                        label='End date YY-MM-DD', ref=self.transaction_end, width=250, height=35)
                                ]),
                            ]),
                        ]
                    ),
                ),
                actions=[
                    ft.FilledButton(
                        'Avail Now', on_click=lambda _:self.avail_transaction(i=item), width=250),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
            )
            avail_recipt_transaction.controls.append(
                ft.Container(ft.Column(controls=[
                    ft.Text(
                        f'               Date: {item.created}', size=15, weight='bold'),
                    ft.Divider(),
                    ft.Text(f'Car Selected: {item.car_model}', size=15),
                    ft.Text(f'Price Per/day: {item.price}', size=15),
                ])
                )
            )
            self.peending = item.car_model
            self.list_view = item.car_model
            self.price_view = item.price
            self.root.dialog = self.dlg
            self.dlg.open = True
            self.root.update()
            self.page.update()

    def load_cars(self):
        self.customer_list()
        cars = get_trasaction()
        self.product_listview.controls.clear()
        ui = map(lambda i:
            ft.Container(
                on_click=lambda _: self.show_dialog(item=i),
                content=ft.Column(controls=[
                    ft.Column([
                        ft.Container(
                            margin=1,
                            padding=1,
                            alignment=ft.alignment.center,
                            bgcolor=ft.colors.BLACK,
                            width=380,
                            height=340,
                            border_radius=1,
                        content=ft.Container(
                            bgcolor=ft.colors.SECONDARY_CONTAINER,
                            border_radius=5,
                            padding=20,
                            margin=2,
                        content=ft.Column([
                            ft.Column([
                                ft.Card(content=ft.Container(
                                    content=ft.Row([
                                        ft.Row([
                                            ft.Container(
                                                image_src=f'http://127.0.0.1:8090/api/files/cars/{i.id}/{i.image}?=thumb100x100',
                                                height=300,
                                                width=300),
                                            ]),
                                        ], alignment=ft.MainAxisAlignment.CENTER,
                                    ),width=380,height=150,padding=5,
                                )),
                            ft.Text(f'{i.car_model}',size=20, weight='bold'),
                            ft.Text(f"P {i.price}/Day", size=13),
                            ft.Text(f'{i.status}', size=20,weight='bold')
                        ]),
                            ft.Row([
                                ft.IconButton(
                                    icon=ft.icons.LOCAL_GAS_STATION,icon_color="black"),
                                ft.Text(i.fuel_type, size=13),
                                ft.IconButton(
                                    icon=ft.icons.CALENDAR_MONTH,icon_color="black900"),
                                ft.Text(f"{i.date_model}Model", size=13),
                                ft.IconButton(icon=ft.icons.PERSON_2,icon_color="black900"),
                                ft.Text(f"{i.seats}Seats", size=13),
                            ])
                       ]),width=380, height=340
                    ))
                ])
            ])
        ), cars)
        for i in list(ui):
            self.product_listview.controls.append(
                i
            ),

    def did_mount(self):
        pass

    def show_dlg(self, item: Customer):
        self.dlg = ft.AlertDialog(
            open=True,
            content=ft.Container(
                width=250,
                height=250,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Column([
                            ft.Text('UPDATE STATUS'),
                            ft.Text(item.name),
                            ft.Row([self.transaction_status]),
                        ]),
                    ]
                ),
            ),
            actions=[
                ft.Column([
                    ft.ElevatedButton(
                        "UPDATE",
                        icon_color="green",
                        on_click=lambda _: self.update_status(item.id), width=300),
                ])
            ]
        )
        self.root.dialog = self.dlg
        self.dlg.open = True
        self.root.update()
        
    def delete_car(self, item_id):
        pb.collection("customer").delete(item_id)
        self.customer_list()
        self.root.update()

    def customer_list(self):
        customer_list_view.rows.clear()
        products = get_customer()
        self.customer_list_view.current.controls.clear()
        ui = map(
            lambda i: ft.Container(
                customer_list_view.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Container(
                                on_click=lambda _: self.show_details(
                                    item=i),
                                content=ft.Row(
                                    [
                                        ft.Text(i.name)
                                    ]
                                )
                            )),
                            ft.DataCell(ft.Container(
                                on_click=lambda _: self.show_dlg(
                                    item=i),
                                content=ft.Row(
                                    [
                                        ft.Text(i.status),
                                    ]
                                )
                            )),
                            ft.DataCell(ft.Container(
                                content=ft.IconButton(
                                icon=ft.icons.DELETE,
                                icon_color="red200",
                                icon_size=20,
                                tooltip="Delete Customer",
                                 on_click=lambda _, item_id=i.id: self.delete_car(item_id)
                            ),
                            ))
                        ]
                    )
                )
            ), products,
        )
        for i in list(ui):
            self.customer_list_view.current.controls.append(i)
        self.customer_list_view.current.update(),


    def update_status(self, item_id):
        self.root.dialog = self.dlg
        self.dlg.open = False
        self.root.update()
        pb.collection("users").auth_with_password("user", "12345678")
        results = pb.collection("customer").update(
            item_id,
            {
                'status': self.transaction_status.value
            }
        )
        self.customer_list_view.current.controls.clear()
        self.customer_list()
        self.page.update()
        

    def update_transaction(self, item_id):
        pb.collection("users").auth_with_password("user", "12345678")
        results = pb.collection("transaction").update(
            item_id,
            body_params={
                'duration': self.transaction_days.current.value,
                'borrow_date': self.transaction_start.current.value,
                'return_date': self.transaction_end.current.value,
                'location': self.transaction_location.current.value
            }
        )
        print(results.__dict__)
        self.customer_list_view.current.controls.clear()
        self.root.dialog = self.dlg
        self.root.update()
        self.customer_list()
        self.page.update()
        
        
    def show_details(self, item: Transaction):
        self.dlg = ft.AlertDialog(
            open=True,
            content=ft.Container(
                width=350,
                height=350,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Column([
                            ft.Text(item.name),
                            ft.Text('UPDATE DETAILS'),
                            ft.Divider(),
                            ft.TextField(
                                label='Duration Days', ref=self.transaction_days, width=250, height=35),
                            ft.TextField(
                                label='Destination', ref=self.transaction_location, width=250, height=35),
                            ft.Column([
                                ft.TextField(
                                    label='Start date DD-MM-YY', ref=self.transaction_start, width=250, height=32),
                                ft.TextField(
                                    label='End date DD-MM-YY', ref=self.transaction_end, width=250, height=35)
                            ]),
                        ]),
                    ]
                ),
            ),
            actions=[
                ft.Column([
                    ft.ElevatedButton(
                        "UPDATE",
                        icon_color="green",
                        on_click=lambda _: self.update_transaction(item.id), width=300),
                ])
            ]
        )
        self.root.dialog = self.dlg
        self.dlg.open = True
        self.root.update()
