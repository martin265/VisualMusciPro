import flet as ft
from Routers.Routers import Routers


def main(page: ft.Page):
    page.theme_mode = "light"
    page.padding = 0
    page.spacing = 0

    #  -------// getting the fonts to be used here----------------//
    page.fonts = {
        "Raleway": "assets/fonts/static/Raleway-Light.ttf"
    }
    page.theme = ft.Theme(font_family="Raleway")
    page.update()

    #  ---------------getting router controls here-----------//
    myRouters = Routers(page=page)
    page.on_route_change = myRouters.route_change

    #  -------------------// navigation bar will be here-------------------//
    main_navigation_bar = ft.Container(
        gradient=ft.LinearGradient(
            colors=[
                "#0050C1",
                "#0050C1"
            ]
        ),
        height=80,
        content=ft.Row(
            #  ---------------// the links for the navigation will be here----//
            controls=[
                #  -------------------the container for the logo here----------//
                ft.Container(
                    margin=ft.margin.only(left=30),
                    content=ft.Row(
                        controls=[
                            ft.Image(
                                src=f"assets/icons/wave-sound.png",
                                height=50,
                                width=50,
                                color="white",
                                semantics_label="logo"
                            )
                        ]
                    )
                ),
                #  -----------------// the container for the home link here-------//
                ft.Container(
                    margin=ft.margin.only(left=10),
                    ink=False,
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "home".title(),
                                color="white",
                                size=15
                            )
                        ]
                    ),
                    on_click=lambda _: page.go('/'),
                ),
                #  -------------------// instruments link will be here-------//
                ft.Container(
                    margin=ft.margin.only(left=10),
                    ink=False,
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "courses".title(),
                                color="white",
                                size=15
                            )
                        ]
                    ),
                    on_click=lambda _: page.go('/courses'),
                ),
                # ft.Divider(),
                #  ------------------// link for the instuments page will be here------//
                ft.Container(
                    margin=ft.margin.only(left=10),
                    ink=False,
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "instrument".title(),
                                color="white",
                                size=15
                            )
                        ]
                    ),
                    on_click=lambda _: page.go('/instruments'),
                ),
                #  -------------------// -----------------------//
                ft.Container(
                    margin=ft.margin.only(left=10),
                    ink=False,
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "vocals".title(),
                                color="white",
                                size=15
                            )
                        ]
                    ),
                    on_click=lambda _: page.go('/vocal_training'),
                ),

                #  -------------------// -----------------------//
                ft.Container(
                    margin=ft.margin.only(left=10),
                    ink=False,
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "lyrics".title(),
                                color="white",
                                size=15
                            )
                        ]
                    ),
                    on_click=lambda _: page.go('/lyrics'),
                ),
            ]
        )
    )
    #  ----------------// adding the page controls here for the model---------//
    page.add(
        ft.Column(
            scroll=ft.ScrollMode.HIDDEN,
            controls=[
                main_navigation_bar,
                myRouters.body
            ]
        )
    )
    page.go("/")
    page.update()


if __name__ == "__main__":
    ft.app(target=main, port=9090, assets_dir="assets", view=ft.WEB_BROWSER)
