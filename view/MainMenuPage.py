import flet as ft
from view.AppPage import AppPage


class MainMenuPage(AppPage):
    def __init__(self, root, route):
        super().__init__(root=root, route=route)

        def hover_delete(e):
            e.control.icon_color = "red" if e.data == "true" else ft.colors.RED_ACCENT_100
            e.control.update()

        appbar = ft.AppBar(
            leading_width=60,
            title=ft.Row([
                ft.IconButton(
                    icon=ft.icons.LIST,
                    icon_color="black300",
                    icon_size=45,
                ),
                ft.Text('CAR RENTAL SYSTEM', size=23, weight='bold')
            ]),
            center_title=False,
            bgcolor=ft.colors.PRIMARY_CONTAINER,
            actions=[
                ft.Divider(),
                ft.TextButton('Home', on_click=lambda _: self.root.go('/MainMenuPage'), width=150,
                              on_hover=hover_delete),
                ft.Divider(),
                ft.TextButton('About Us', on_click=lambda _: self.root.go('/AboutUsPage'), width=150,
                              on_hover=hover_delete),
                ft.Divider(),
                ft.TextButton('Contact Us', on_click=lambda _: self.root.go('/ContactUsPage'), width=150,
                              on_hover=hover_delete),
            ],
        )

        a2 = ft.Container(
            alignment=ft.alignment.center,
            content=ft.Column([
                ft.Text(''),
                ft.Container(
                    margin=0,
                    padding=0,
                    bgcolor=ft.colors.ON_TERTIARY,
                    width=320,
                    border_radius=0,
                    content=ft.Row([
                        ft.Divider(),
                        ft.TextButton('CAR VARIANT', width=300,
                                      on_click=lambda _: self.root.go('/AddTransactionPage')),
                    ], alignment=ft.MainAxisAlignment.CENTER)
                ),
                ft.Container(
                    margin=0,
                    padding=0,
                    bgcolor=ft.colors.ON_TERTIARY,
                    width=320,
                    border_radius=0,
                    content=ft.Row([
                        ft.Divider(),
                        ft.TextButton('INQUIRE CAR',
                                      on_click=lambda _: self.root.go(
                                          '/CarRentPage'),
                                      width=300),
                    ], alignment=ft.MainAxisAlignment.CENTER),
                ),
                ft.Container(
                    margin=0,
                    padding=0,
                    bgcolor=ft.colors.ON_TERTIARY,
                    width=320,
                    border_radius=0,
                    content=ft.Row([
                        ft.Divider(),
                        ft.TextButton('CUSTOMER',
                                      on_click=lambda _: self.root.go(
                                          '/CustomerPage'),
                                      width=300),
                    ], alignment=ft.MainAxisAlignment.CENTER),
                ),
                ft.Container(
                    margin=0,
                    padding=0,
                    bgcolor=ft.colors.ON_TERTIARY,
                    width=320,
                    border_radius=0,
                    content=ft.Row([
                        ft.Divider(),
                        ft.TextButton('RENTAL', width=300,
                                      on_click=lambda _: self.root.go('/RentalPage')),
                    ], alignment=ft.MainAxisAlignment.CENTER),
                ),
                ft.Container(
                    margin=0,
                    padding=0,
                    bgcolor=ft.colors.ON_TERTIARY,
                    width=320,
                    border_radius=0,
                    content=ft.Row([
                        ft.Divider(),
                        ft.TextButton('LOGOUT',
                                      on_click=lambda _: self.root.go('/'),
                                      width=300),
                    ], alignment=ft.MainAxisAlignment.CENTER),
                ),
            ]),
        )

        self.page.controls = [
            appbar,

            ft.ResponsiveRow(
                vertical_alignment=ft.CrossAxisAlignment.STRETCH,
                controls=[
                    ft.Column(col=3, controls=[ft.Container(
                        content=ft.Row([a2]),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.SECONDARY_CONTAINER,
                        width=350,
                        height=700,
                        border_radius=10,
                    ),]),
                    ft.Column(
                        col=9,
                        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                        controls=[ft.Column(controls=[
                            ft.Container(
                                margin=1,
                                padding=1,
                                bgcolor=ft.colors.BLACK,
                                border_radius=1,
                                content=ft.Column(controls=[
                                    ft.Container(
                                            margin=1,
                                            padding=1,
                                            bgcolor=ft.colors.WHITE,
                                            border_radius=10,
                                            content=ft.Column(controls=[
                                                
                                                ft.Container(
                                                    alignment=ft.alignment.center,
                                                    content=ft.Stack(
                                                        [
                                                            ft.Image(
                                                                src='Pics/200_rental_hero.jpg',
                                                                fit='cover',
                                                                height=650
                                                            ),
                                                        ])
                                                ),
                                            ])
                                        ),
                                ])),
                        ])]
                    ),
                ]
            ),
        ]
