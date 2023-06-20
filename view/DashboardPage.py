import flet as ft

from view.AppPage import AppPage

class DashboardPage (AppPage):

    def __init__(self, root, route):
        super().__init__(root=root, route=route)
        
    def get_page(self) -> ft.View:
        
        textcontainer = ft.Container(
            margin=30,
            content=ft.Container(
                ft.Column(
                    [
                        ft.Text('LETS GET YOU',color='white',size=70,weight='bold'),
                        ft.Text('ON THE ROAD',color='red',size=70,weight='bold'),
                        ft.Text(''),
                        ft.Text(''),
                        ft.Divider(),
                        ft.Container(
                            margin=0,
                            padding=0,
                            alignment=ft.alignment.center,
                            bgcolor=ft.colors.RED_ACCENT_100,
                            width=350,
                            border_radius=0,
                            content=ft.Column(
                                [
                                    ft.TextButton('LOGIN',width=350,
                                    on_click=lambda _: self.root.go('/MainMenuPage')           
                                                  ),
                                ],alignment=ft.MainAxisAlignment.CENTER,
                            )
                        )
                    ]
                )
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
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            
            controls=[
                        ft.Column(
                                        [
                                            ft.Container(
                                                alignment=ft.alignment.center, 
                                                content=ft.Stack(
                                                    [
                                                        ft.Image(
                                                            src='Pics/audi-r8-supercars-angel-lghts-matte-black-r8-audi.jpg',
                                                            fit='cover',
                                                            height=760,
                                                            width=1200,
                                                        ),
                                                        myimagecontainer
                                                    ],
                                                )
                                            )
                                        ]
                                    )
                    ],
            )
        ]
        return self.page

    def did_mount(self):
        pass
