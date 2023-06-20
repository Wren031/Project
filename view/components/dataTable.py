import flet as ft

header = ['CAR ID', 'MODEL', 'DATE MODEL', 'PRICE' , 'SEAT', 'FUEL TYPE', 'STATUS', 'EDIT DETAILS',]

columns = []
for i in header:
    columns.append(
        ft.DataColumn(
            ft.Text(
                i,
                size=15,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        )
    )
car_variant = ft.DataTable(
    columns=columns,
    rows=[],
)


pending =ft.DataTable(
    columns=[
                ft.DataColumn(
                    ft.Text("Name",size=13,weight=ft.FontWeight.BOLD,
                            color=ft.colors.BLACK)),
                ft.DataColumn(
                    ft.Text("Car Selected",size=13,weight=ft.FontWeight.BOLD,
                            color=ft.colors.BLACK)),
            ],
            rows=[],
        )

dt = ft.DataTable(
    columns=[
        ft.DataColumn(
            ft.Text(
                "DATE",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        ),
        ft.DataColumn(
            ft.Text(
                "CUSTOMER NAME",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        ),
        ft.DataColumn(
            ft.Text(
                "ADDRESS",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        ),
        ft.DataColumn(
            ft.Text(
                "DESTINATION",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        ),
        ft.DataColumn(
            ft.Text(
                "DRIVER LICENSED ID",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        ),
        ft.DataColumn(
            ft.Text(
                "AGE",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        ),
        ft.DataColumn(
            ft.Text(
                "CAR TYPE",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        ),
        ft.DataColumn(
            ft.Text(
                "TOTAL COAST",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        ),
    ],
    rows=[],
)

avail_recipt = ft.DataTable(
    columns=[
        ft.DataColumn(
            ft.Text(
                "DATE",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        ),
        ft.DataColumn(
            ft.Text(
                "CUSTOMER NAME",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        ),
        ft.DataColumn(
            ft.Text(
                "ADDRESS",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        ),
        ft.DataColumn(
            ft.Text(
                "DESTINATION",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        ),
        ft.DataColumn(
            ft.Text(
                "DRIVER LICENSED ID",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        ),
        ft.DataColumn(
            ft.Text(
                "AGE",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        ),
        ft.DataColumn(
            ft.Text(
                "CAR TYPE",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        ),
        ft.DataColumn(
            ft.Text(
                "TOTAL COAST",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        ),
    ],
    rows=[],
)

customer = ft.DataTable(
    columns=[
        ft.DataColumn(
            ft.Text(
                "DATE",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        ),
        ft.DataColumn(
            ft.Text(
                "CUSTOMER NAME",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        ),
        ft.DataColumn(
            ft.Text(
                "ADDRESS",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        ),
        ft.DataColumn(
            ft.Text(
                "DRIVER LICENSED ID",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        ),
        ft.DataColumn(
            ft.Text(
                "NUMBER",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        ),
        ft.DataColumn(
            ft.Text(
                "BIRTH DATE",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        ),
        ft.DataColumn(
            ft.Text(
                "STATUS",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        ),
    ],
    rows=[],
)


transaction_data = ft.DataTable(
    columns=[
        ft.DataColumn(
            ft.Text(
                "DATE",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        ),
        ft.DataColumn(
            ft.Text(
                "CUSTOMER NAME",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        ),
        ft.DataColumn(
            ft.Text(
                "CAR RENT",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        ),
        ft.DataColumn(
            ft.Text(
                "DURATION DAYS",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        ),
        ft.DataColumn(
            ft.Text(
                "DISTINATION",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        ),
        ft.DataColumn(
            ft.Text(
                "START DATE",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        ),
        ft.DataColumn(
            ft.Text(
                "END DATE",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        ),
        ft.DataColumn(
            ft.Text(
                "DELETE",
                size=13,
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLACK,
            )
        )
    ],
    rows=[],
)

customer_list_view = ft.DataTable(
    columns=[
        ft.DataColumn(
            ft.Text(
                "Customer",
                size=13,
                color=ft.colors.BLACK,
            )
        ),
        ft.DataColumn(
            ft.Text(
                'Status',
                size=13,
                color=ft.colors.BLACK,
            )
        ),
        ft.DataColumn(
            ft.Text(
                'Delete',
                size=13,
                color=ft.colors.BLACK,
            )
        ),
    ],
    rows=[],
)