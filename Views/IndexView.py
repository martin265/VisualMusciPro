import flet as ft


class IndexView(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.ListView(
            controls=[
                #  --------------// main container for the page here
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                "index view",
                                color="black"
                            )
                        ]
                    )
                )
            ]
        )