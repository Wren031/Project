import flet as ft
from view.AppPage import AppPage
from view.DashboardPage import DashboardPage
from view.MainMenuPage import MainMenuPage
from view.AddTransactionPage import AddTransactionPage
from view.InquirePage import InquirePage
from view.CustomerPage import CustomerPage
from view.LoginPage import LoginPage
from view.RentalPage import RentalPage
from view.AboutUsPage import AboutUsPage

from view.ContactUsPage import ContactUsPage

def main(page: ft.Page):
    pages: list[AppPage] = [
        LoginPage(root=page, route='/'),
        #DashboardPage(root=page, route="/"),
        MainMenuPage(root=page, route="/MainMenuPage"),
        AddTransactionPage(root=page, route="/AddTransactionPage"),
        InquirePage(root=page, route="/CarRentPage"),
        CustomerPage(root=page, route="/CustomerPage"),
        AboutUsPage(root=page, route="/AboutUsPage"),
        ContactUsPage(root=page, route="/ContactUsPage"),
        RentalPage(root=page, route="/RentalPage"),
    ]

    page.title = "App"

    theme = ft.Theme(color_scheme_seed=ft.colors.WHITE, use_material3=True)

    page.theme = theme
    page.dark_theme = theme
    page.theme_mode = ft.ThemeMode.LIGHT

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.theme = ft.Theme(
        color_scheme_seed=ft.colors.ON_PRIMARY,
    )
    page.window_height = 800
    page.window_width = 1500
    page.window_resizable = True

    def route_change(_):
        page.views.clear()
        print(pages[0].page.route)

        sel = tuple(filter(lambda x: x.page.route == page.route, pages))
        page.views.append(sel[0].get_page())
        page.go(sel[0].page.route)

    page.on_route_change = route_change
    page.go(page.route)
