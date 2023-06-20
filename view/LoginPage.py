import flet as ft
from contorller.AuthController import login
from view.AppPage import AppPage
from pocketbase.utils import ClientResponseError

class LoginPage(AppPage):
    username = ft.Ref[ft.TextField]()
    password = ft.Ref[ft.TextField]()
    
    def close(self):
        self.root.banner = self.banner
        self.banner.open = False
        self.root.update()         
    
    def greetings(self):
        self.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.PERSON, color=ft.colors.AMBER, size=40),
        content=ft.Text(
            'Welcome Admin',size=23,weight='bold'
            ),
        actions=[
            ft.TextButton("Close",  on_click=lambda _:self.close()),
            ],
        )
        self.root.banner = self.banner
        self.banner.open = True
        self.root.update()    

    def __init__(self, root, route):
        super().__init__(root=root, route=route)
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.did_mount = self.did_mount

    def did_mount(self):
        self.username.current.value = ''
        self.password.current.value = ''

    def get_page(self) -> ft.View:
        textcontainer = ft.Container(
                content=ft.Container(
                    ft.Column([
                        ft.Text('  LETS GET YOU',color='white',size=70,weight='bold'),
                        ft.Text('ON THE ROAD',color='red',size=70,weight='bold'),  
                    ft.Container(
                        margin=0,
                        padding=0,
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.BROWN_100,
                        width=355,
                        height=290,
                        border_radius=0,
                content=ft.Column([
                    ft.Container(
                        margin=0,
                        padding=0,
                        alignment=ft.alignment.center,
                        width=340,
                        height=285,
                        border_radius=0,
                content=ft.Column([
                            ft.Text(),                                       
                            ft.TextField(
                                ref=self.username,label="Username",
                                width=350),
                    ft.Divider(),   
                            ft.TextField(
                                ref=self.password,password=True,can_reveal_password=True,
                                label="Password",
                                width=350),
                    ft.Divider(),   
                    ft.Container(
                        margin=0,
                        padding=0,
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.BLACK,
                        width=350,
                        border_radius=0,
                content=ft.Column(controls=[
                            ft.TextButton('LOGIN',width=350,
                                    on_click=self.on_login        
                                    ),
                                ],alignment=ft.MainAxisAlignment.CENTER,
                            )
                        )],alignment=ft.MainAxisAlignment.CENTER,
                    )),
                ],alignment=ft.MainAxisAlignment.CENTER,
            ))
        ])
    ))

        myimagecontainer = ft.Container(
            content=ft.Stack(
                [
                    textcontainer,
                ]
            )
        )
        
        self.page.controls = [
            ft.Column([
                ft.Container(
                    alignment=ft.alignment.center, 
                    content=ft.Stack([
                            ft.Image(
                                src=f"Pics/audi-r8-supercars-angel-lghts-matte-black-r8-audi.jpg",
                                fit='cover',
                                height=800,
                                width=1500,
                            ),myimagecontainer
                        ])
                    )]
                )
            ]

        return self.page

    def on_login(self, _):
        try:
            login(username=self.username.current.value,
                  password=self.password.current.value)
            self.greetings()
            self.root.go(route='/MainMenuPage')

        except ClientResponseError:
            ok = ft.Ref[ft.TextButton]()
            dialog = ft.AlertDialog(
                modal=True,
                content=ft.Text('Just Relax and try to Remember you password'),
                actions=[
                    ft.TextButton('OK', ref=ok)
                ]
            )

            def on_close(_):
                dialog.open = False
                self.root.update()

            ok.current.on_click = on_close

            self.root.dialog = dialog
            dialog.open = True
            self.root.update()