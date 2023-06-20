import flet as ft

from view.AppPage import AppPage

from contorller.CarsController import get_trasaction


class AboutUsPage(AppPage):
        

    def __init__(self, root, route):
        super().__init__(root=root, route=route)
        
        self.page.scroll=ft.ScrollMode.ALWAYS
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        
        self.tansaction_list_view = ft.Ref[ft.ListView]()

        def load_transaction():
            products = get_trasaction()
            self.tansaction_list_view.current.controls.clear()
            for item in products:
                self.tansaction_list_view.current.controls.append(
                    ft.Container(ft.Row(controls=[
                        ft.Container(
                            image_src=f'http://127.0.0.1:8090/api/files/cars/{item.id}/{item.image}?=thumb100x100',
                            height=250,
                            width=450,
                        ),
                        ft.Column([
                            ft.Text(f'{item.car_model}' ,size=25,weight='bold'),
                            ft.Text(f'P {item.price} ',size=23),
                            ft.Text(f'{item.seats} Capacity',size=23),
                        ])
                    ]))
                ),
            self.tansaction_list_view.current.update()
            
            
        self.page.did_mount = lambda:load_transaction()
        
        textcontainer = ft.Container(
            margin=30,
            alignment=ft.alignment.center,  
            content=ft.Container(
                ft.Column(
                    [
                        ft.Text('About Us',size=42,weight='bold',color='black'),
                        ft.Text('Home > About Us',size=18,weight='bold',color='black')
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
            ft.Column(
                [
                    ft.Container(
                        alignment=ft.alignment.center, 
                        content=ft.Stack(
                            [
                                ft.Image(
                                    src=f"Pics/Rolls-Royce-Ghost-Named-Best-Super-Luxury-Car.jpg",
                                    fit='cover',
                                    height=200,
                                    width=1500,
                                ),
                                myimagecontainer
                            ],
                        )
                    )
                ]
            ),
            ft.Container(
                ft.Column(
                    [
                        ft.Text('''
                                Car rental services have become an integral part of modern transportation, providing convenience and flexibility to travelers and locals alike. Whether you're planning a road trip, need a temporary vehicle while yours is being repaired, or simply want to explore a new city at your own pace, car rental companies offer a wide range of vehicles to suit diverse needs. With a straightforward booking process, customers can select the type of car that suits their preferences and requirements, whether it's a compact car for urban maneuverability, a spacious SUV for family adventures, or a luxurious sedan for a touch of elegance. Additionally, car rental services often provide various add-ons like GPS navigation systems, child seats, and insurance options to enhance the overall experience and ensure peace of mind. By choosing car rental, individuals gain the freedom to explore their desired destinations comfortably, creating unforgettable memories along the way.
                                
                                ''',size=14,weight='bold'),
                    ]
                )
            ),
            ft.ListView(ref=self.tansaction_list_view), 
        ]

