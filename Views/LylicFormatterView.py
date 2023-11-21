import flet as ft


class LyricFormatter(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.padding = 0
        self.page.spacing = 0
        self.page.fonts = {
            "OpenSans": "assets/fonts/static/OpenSans-Light.ttf",
            "Raleway": "assets/fonts/static/Raleway-Light.ttf",
            "Roboto-bold": "assets/fonts/Roboto-Bold.ttf",
            "Roboto-black": "assets/fonts/Roboto-Black.ttf",
            "Raleway-bold": "assets/fonts/static/Raleway-Bold.ttf"
        }

    def build(self):
        return ft.ListView(
            expand=1,
            auto_scroll=True,
            spacing=10,
            height=800,
            scale=1.0,
            controls=[
                #  ----------------// the top container here----------//
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                content=ft.Row(
                                    wrap=True,
                                    controls=[
                                        ft.Text(
                                            ""
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ),
                ft.Container(
                    width=1200,
                    height=600,
                    margin=ft.margin.only(left=30, right=30, top=30),
                    border_radius=ft.border_radius.all(10),
                    shadow=ft.BoxShadow(
                        blur_radius=4,
                        blur_style=ft.ShadowBlurStyle.OUTER,
                        color="#0050C1",
                    ),
                    content=ft.Column(
                        controls=[

                        ]
                    )
                ),

                ft.Container(
                    height=200
                )
            ]
        )
