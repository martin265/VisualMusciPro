import flet as ft
from Views.InstrumentsView import InstrumentsView
from Views.StudentView import StudentView
from Views.IndexView import IndexView
from Views.VocalTrainingView import VocalTraining
from Views.LylicFormatterView import LyricFormatter


class Routers:
    """class that will handle all the page transitions"""

    def __init__(self, page: ft.Page):
        self.page = page
        self.ft = ft
        self.routes = {
            "/": IndexView(page),
            "/courses": StudentView(page=page),
            "/instruments": InstrumentsView(page=page),
            "/vocal_training": VocalTraining(page=page),
            "/lyrics": LyricFormatter(page=page)
        }
        self.body = ft.Container(content=self.routes['/'])

    # the route change function will be here---------------//
    def route_change(self, route):
        try:
            self.body.content = self.routes[route.route]
            self.body.update()
        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "something went wrong at {}".format(ex)
                        )
                    ]
                )
            )
            self.page.snack_bar.open = True
            self.page.update()
