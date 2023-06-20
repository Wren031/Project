import flet as ft
from view.AppPage import AppPage

class ContactUsPage(AppPage):
        
    def __init__(self, root, route):
        super().__init__(root=root, route=route)
        
        self.page.scroll=ft.ScrollMode.ALWAYS
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        
        textcontainer = ft.Container(
            margin=30,
            alignment=ft.alignment.center,  
            content=ft.Container(
                ft.Column(
                    [
                        ft.Text('Contact Us',size=42,weight='bold',color='black'),
                        ft.Text('Home > Contact Us',size=18,weight='bold',color='black')
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
        def hover_delete(e):
            e.control.icon_color = "red" if e.data == "true" else ft.colors.RED_ACCENT_100,
            e.control.update()
            
        appbar = ft.AppBar(
                leading_width=60,
                title=ft.Text("CAR RENTAL "
                              ,color='black',
                              size=25,
                              weight='bold'),
                center_title=False,
                bgcolor=ft.colors.SECONDARY_CONTAINER,
                actions=[
                    ft.Divider(),
                    ft.TextButton('Home',on_click=lambda _: self.root.go('/MainMenuPage'),width=150,
                                   on_hover=hover_delete
                                  ),
                    ft.Divider(),
                    ft.TextButton('About Us',on_click=lambda _: self.root.go('/AboutUsPage'),width=150,
                                   on_hover=hover_delete
                                  ),
                    ft.Divider(),
                    ft.TextButton('Contact Us',on_click=lambda _: self.root.go('/ContactUsPage'),width=150,
                                   on_hover=hover_delete
                                ),
                            ],
                        )
        
        self.page.controls = [
        appbar,
        ft.Divider(),
        #Picture UI
        ft.Column(controls=[
            ft.Container(
                alignment=ft.alignment.center, 
                content=ft.Stack([ft.Image(
                                src="Pics/renty-car-w1200.png",
                                fit='cover',
                                height=200,
                                width=1500,
                            ), myimagecontainer
                        ])
                    )
                ]),
            # Second UI
            ft.Container(
                ft.Row(controls=[
            ft.Container(ft.Column(controls=[
                    ft.Container(content=ft.Column([
                    ft.Text('Get in touch using the form below',size=32,weight='bold',color='black'),
                    ft.TextField(label='Full Name',width=350,height=35),
                    ft.TextField(label='Email Address',width=350,height=35),
                    ft.TextField(label='Phone Number',width=350,height=35),
                    ft.TextField(label='Message',width=450),
                    ft.Row([ft.ElevatedButton('Send Message Now',width=450)])
                ]),         
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.SECONDARY_CONTAINER,
                    width=600,
                    height=450,
                ),
            ])
        ),
            #Second UI
            ft.Container(ft.Column(controls=[
                ft.Card(content=ft.Container(
                    content=ft.Column([
                            ft.Text('Contact Info',size=32,weight='bold'),
                            ft.Text(''),
                            ft.Row([
                            ft.Icon(name=ft.icons.LOCATION_ON, color=ft.colors.BLACK),
                                    ft.Text('Valencia City Bukidnon',size=17),
                            ]),
                            ft.Text(''),
                            ft.Row([ft.Icon(name=ft.icons.EMAIL, color=ft.colors.BLACK),
                                ft.Text('renrenjavier1@gmail.com',size=17),
                            ]),
                            ft.Text(''),
                            ft.Row([ft.Icon(name=ft.icons.LOCAL_PHONE_ROUNDED, color=ft.colors.BLACK),                       
                            ft.Text('+639095540145',size=17)
                            ])]
                        ),width=400,height=450,
                    ))
                ]))
            ])
        )
    ]
        
