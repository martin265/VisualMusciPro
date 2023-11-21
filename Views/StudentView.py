import flet as ft
import datetime
from classes.course import Student


class InstrumentsAlert(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

        #  ---------------// getting user input for the course here------//
        self.first_name = ft.TextField(
            width=400,
            height=100,
            border_color="#0050C1",
            keyboard_type=ft.KeyboardType.NAME,
            autocorrect=True,
            autofocus=True,
            prefix_icon=ft.icons.PERSON_2_ROUNDED,
            helper_text="characters only",
            hint_text="first name".capitalize(),
            label="first name".title(),
            focused_border_color="#1565c0",
        )
        # -------------------------//-------------------------------//----------------//
        self.last_name = ft.TextField(
            width=400,
            height=100,
            border_color="#0050C1",
            keyboard_type=ft.KeyboardType.NAME,
            autocorrect=True,
            autofocus=True,
            prefix_icon=ft.icons.PERSON_2_ROUNDED,
            helper_text="characters only",
            hint_text="first name".capitalize(),
            label="last name".title(),
            focused_border_color="#1565c0",
        )
        #  -------------------------//----------------------------//---------------------//
        self.age = ft.TextField(
            width=400,
            height=100,
            border_color="#0050C1",
            keyboard_type=ft.KeyboardType.NUMBER,
            autocorrect=True,
            autofocus=True,
            prefix_icon=ft.icons.PERSON_2_ROUNDED,
            helper_text="numbers only",
            hint_text="age".capitalize(),
            label="age".title(),
            focused_border_color="#1565c0",
        )
        #  -----------------------//------------------------//---------------------//
        self.phone_number = ft.TextField(
            autocorrect=True,
            autofocus=True,
            enable_suggestions=True,
            width=400,
            height=100,
            prefix_icon=ft.icons.PHONE_ANDROID_ROUNDED,
            helper_text="numbers only",
            border_color="#0050C1",
            label="phone number".capitalize(),
            capitalization=ft.TextCapitalization.WORDS,
            focused_border_color="#1565c0",
            keyboard_type=ft.KeyboardType.NAME,
            border_width=2
        )
        #  ------------------------//---------------------------//-------------------//
        self.email = ft.TextField(
            autocorrect=True,
            autofocus=True,
            enable_suggestions=True,
            width=400,
            height=100,
            prefix_icon=ft.icons.EMAIL_ROUNDED,
            helper_text="characters only",
            border_color="#0050C1",
            label="email".capitalize(),
            capitalization=ft.TextCapitalization.WORDS,
            focused_border_color="#1565c0",
            keyboard_type=ft.KeyboardType.EMAIL,
            border_width=2
        )
        #  ------------------------//---------------------------//-------------------//
        self.course = ft.Dropdown(
            label="select course....",
            hint_text="required field",
            helper_text="only characters",
            width=400,
            height=100,
            border_color="#0050C1",
            prefix_icon=ft.icons.LIBRARY_BOOKS_ROUNDED,
            focused_border_color="#1a237e", focused_color="#6200ea",
            options=[
                ft.dropdown.Option("Instruments Course"),
                ft.dropdown.Option("Vocal Training"),
                ft.dropdown.Option("Song Writing"),
            ]
        )
        #  ------------------------//------------------------//
        self.gender = ft.RadioGroup(
            content=ft.Container(
                width=400,
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "gender".capitalize(),
                            size=18,
                            weight=ft.FontWeight.W_700
                        ),
                        ft.Radio(value="male", label="male".capitalize()),
                        ft.Radio(value="female", label="female".capitalize())
                    ]
                )
            )
        )
        #  ---------------------//grade--------------------------------------//
        self.grade = ft.Dropdown(
            label="select grade....",
            width=400,
            height=100,
            hint_text="required field",
            helper_text="only characters",
            border_color="#0050C1",
            prefix_icon=ft.icons.GRADE_ROUNDED,
            focused_border_color="#1a237e", focused_color="#6200ea",
            options=[
                ft.dropdown.Option("starter"),
                ft.dropdown.Option("intermediate"),
                ft.dropdown.Option("advanced")
            ]
        )
        #  ------------------// -----------------------//
        self.current_date = ft.Text()
        self.date_picker = ft.DatePicker(
            on_change=self.get_current_date,
            first_date=datetime.datetime(2023, 10, 1),
            last_date=datetime.datetime(2024, 10, 1)
        )
        self.page.overlay.append(self.date_picker)

        #  ---------------// alert dialog------------//
        self.instruments_registration = ft.AlertDialog(
            content=ft.Container(
                width=900,
                border_radius=ft.border_radius.all(10),
                bgcolor="white",
                content=ft.Column(
                    scroll=ft.ScrollMode.HIDDEN,
                    controls=[
                        #  --------------//
                        ft.Container(
                            margin=ft.margin.only(top=20),
                            content=ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Text(
                                        "create course".capitalize(),
                                        style=ft.TextThemeStyle.DISPLAY_SMALL,
                                        color="#0050C1"
                                    )
                                ]
                            )
                        ),

                        ft.Container(
                            margin=ft.margin.only(top=20, bottom=20),
                            content=ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Image(
                                        src="assets/stickers/elearning.png",
                                        height=100,
                                        width=100,
                                    )
                                ]
                            )
                        ),

                        ft.Container(
                            margin=ft.margin.only(top=20),
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            self.first_name, self.last_name
                                        ]
                                    ),
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            self.age, self.gender
                                        ]
                                    ),
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            self.grade, self.phone_number,
                                        ]
                                    ),
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            self.email, self.course
                                        ]
                                    ),

                                    ft.Container(
                                        margin=ft.margin.only(left=40, top=10, bottom=20),
                                        content=ft.Row(
                                            controls=[
                                                ft.ElevatedButton(
                                                    icon=ft.icons.APP_REGISTRATION_ROUNDED,
                                                    icon_color="white",
                                                    height=60,
                                                    width=200,
                                                    text="register course".title(),
                                                    elevation=None,
                                                    style=ft.ButtonStyle(
                                                        bgcolor="#212121",
                                                        color="white",

                                                    ),
                                                    #  ------------the click function-------//
                                                    on_click=self.validate_inputs
                                                )
                                            ]
                                        )
                                    )
                                ]
                            )
                        )
                    ]
                )
            )
        )
        #  --------------// getting the actual date----------//

    def get_current_date(self, e):
        self.current_date = self.date_picker.value

    #  -----------------// function to validate inputs here-------------------//
    def validate_inputs(self, e):
        """the function will validate the input before saving the actual records"""
        try:
            if not self.first_name.value:
                self.first_name.error_text = "enter your first name".capitalize()
                self.page.update()
            #  -------------------//-----------------------//-------------------//
            elif not self.last_name.value:
                self.last_name.error_text = "enter last name first".capitalize()
                self.page.update()
            # ------------------------//------------------//------------------//
            elif not self.age.value:
                self.age.error_text = "provide your age".capitalize()
                self.page.update()
            #  ----------------------//--------------------//-------------------//
            elif not self.gender.value:
                self.gender.error_text = "provide your gender".capitalize()
                self.page.update()
            #  ------------------------//-------------------//-------------------//
            elif not self.grade.value:
                self.grade.error_text = "select grade first".capitalize()
                self.page.update()
            #  -----------------------//---------------------//----------------//
            elif not self.phone_number.value:
                self.phone_number.error_text = "enter your phone number".capitalize()
                self.page.update()
            #  ---------------------//-----------------------//----------------//
            elif not self.email.value:
                self.email.error_text = "enter your email".capitalize()
                self.page.update()
            #  -------------------------------//----------------//-----------//
            elif not self.course.value:
                self.course.error_text = "select course".capitalize()
                self.page.update()
            else:
                self.save_student_details()
                self.instruments_registration.open = False
                self.page.update()
        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "something went wrong at {}".format(ex)
                            )
                        ]
                    )
                )
            )
            self.page.snack_bar.open = True
            self.page.update()

        #  -----------------------------//function to save the details to the database-------------//

    def save_student_details(self):
        try:
            current_date = datetime.datetime.now().strftime("%d, %A, %B")
            student = Student(self.first_name.value, self.last_name.value, self.age.value, self.gender.value,
                              self.grade.value, self.phone_number.value, self.email.value, self.course.value,
                              current_date)
            student.add_new_course_details()
            #  -------------------opening the snack bar here-----------------//
            self.page.snack_bar = ft.SnackBar(
                bgcolor="#0050C1",
                content=ft.Container(
                    height=50,
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "course registered successfully".capitalize()
                            )
                        ]
                    )
                )
            )
            self.page.snack_bar.open = True
            self.page.update()
        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                "something went wrong at {}".format(ex)
                            )
                        ]
                    )
                )
            )
            self.page.snack_bar.open = True
            self.page.update()

    def build(self):
        return self.instruments_registration


class StudentView(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
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

        #  -----------------// calling the functions here------------//
        self.instruments_val = InstrumentsAlert(page=page)

    #  ----------------// function to call the instrument function here---------//
    def trigger_instrument_modal_func(self, e):
        try:
            instrument_dialog = self.instruments_val.instruments_registration
            self.page.dialog = instrument_dialog
            instrument_dialog.open = True
            self.page.update()
        except Exception as ex:
            print(ex)

    def build(self):
        return ft.ListView(
            expand=1,
            auto_scroll=True,
            spacing=10,
            height=800,
            scale=1.0,
            controls=[
                #  --------------// main container for the page here
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                margin=ft.margin.only(top=30),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text(
                                            "select course".capitalize(),
                                            color="#212121",
                                            font_family="Raleway",
                                            style=ft.TextThemeStyle.DISPLAY_SMALL
                                        )
                                    ]
                                )
                            ),

                            #  -----------// cards here---------------//
                            ft.Container(
                                margin=ft.margin.only(left=20, top=20),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        #  ------------// 1 //----------------------//
                                        ft.Container(
                                            width=400,
                                            height=450,
                                            border_radius=ft.border_radius.all(10),
                                            gradient=ft.LinearGradient(
                                                colors=[
                                                    "#0050C1",
                                                    "#311B92"
                                                ],
                                                begin=ft.alignment.top_left,
                                                end=ft.alignment.bottom_left
                                            ),
                                            content=ft.Column(
                                                controls=[
                                                    #  -----------//-------//
                                                    ft.Container(
                                                        margin=ft.margin.only(top=20),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Image(
                                                                    src="assets/stickers/people.png",
                                                                    height=100,
                                                                    width=100
                                                                )
                                                            ]
                                                        )
                                                    ),

                                                    #  -----------------//-----------------//
                                                    ft.Container(
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Text(
                                                                    "instruments course".capitalize(),
                                                                    color="white",
                                                                    size=20,
                                                                    font_family="Raleway-bold"
                                                                )
                                                            ]
                                                        )
                                                    ),

                                                    #  ------------// ----------------//
                                                    ft.Container(
                                                        margin=ft.margin.only(left=20, right=20),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            wrap=True,
                                                            controls=[
                                                                ft.Text(
                                                                    "Focus on teaching a specific musical instrument,"
                                                                    " such as guitar, piano, violin, trumpet, etc."
                                                                    " These courses can range from beginner to advanced"
                                                                    " levels, the course has a specified duration attached"
                                                                    "when taking part.",
                                                                    color="white",
                                                                    no_wrap=False,
                                                                    size=20
                                                                )
                                                            ]
                                                        )
                                                    ),

                                                    ft.Container(
                                                        margin=ft.margin.only(left=20, top=10),
                                                        content=ft.Row(
                                                            controls=[
                                                                ft.ElevatedButton(
                                                                    icon=ft.icons.APP_REGISTRATION_ROUNDED,
                                                                    icon_color="white",
                                                                    height=60,
                                                                    width=200,
                                                                    text="register course".title(),
                                                                    elevation=None,
                                                                    style=ft.ButtonStyle(
                                                                        bgcolor="#212121",
                                                                        color="white",

                                                                    ),
                                                                    #  ------------the click function-------//
                                                                    on_click=self.trigger_instrument_modal_func,
                                                                )
                                                            ]
                                                        )
                                                    )
                                                ]
                                            )
                                        ),

                                        #  ------------// 1 //----------------------//
                                        ft.Container(
                                            width=400,
                                            height=450,
                                            border_radius=ft.border_radius.all(10),
                                            gradient=ft.LinearGradient(
                                                colors=[
                                                    "#0050C1",
                                                    "#311B92"
                                                ],
                                                begin=ft.alignment.top_left,
                                                end=ft.alignment.bottom_left
                                            ),
                                            content=ft.Column(
                                                controls=[
                                                    #  -----------//-------//
                                                    ft.Container(
                                                        margin=ft.margin.only(top=20),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Image(
                                                                    src="assets/stickers/file.png",
                                                                    height=100,
                                                                    width=100
                                                                )
                                                            ]
                                                        )
                                                    ),

                                                    #  -----------------//-----------------//
                                                    ft.Container(
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Text(
                                                                    "song writing".capitalize(),
                                                                    color="white",
                                                                    size=20,
                                                                    font_family="Raleway-bold"
                                                                )
                                                            ]
                                                        )
                                                    ),

                                                    #  ------------// ----------------//
                                                    ft.Container(
                                                        margin=ft.margin.only(left=20, right=20),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            wrap=True,
                                                            controls=[
                                                                ft.Text(
                                                                    "Focus on teaching a specific musical instrument,"
                                                                    " such as guitar, piano, violin, trumpet, etc."
                                                                    " These courses can range from beginner to advanced"
                                                                    " levels, the course has a specified duration attached"
                                                                    "when taking part.",
                                                                    color="white",
                                                                    no_wrap=False,
                                                                    size=20
                                                                )
                                                            ]
                                                        )
                                                    ),

                                                    ft.Container(
                                                        margin=ft.margin.only(left=20, top=10),
                                                        content=ft.Row(
                                                            controls=[
                                                                ft.ElevatedButton(
                                                                    icon=ft.icons.APP_REGISTRATION_ROUNDED,
                                                                    icon_color="white",
                                                                    height=60,
                                                                    width=200,
                                                                    text="register course".title(),
                                                                    elevation=None,
                                                                    style=ft.ButtonStyle(
                                                                        bgcolor="#212121",
                                                                        color="white",

                                                                    ),
                                                                    #  ------------the click function-------//
                                                                    on_click={},
                                                                )
                                                            ]
                                                        )
                                                    )
                                                ]
                                            )
                                        ),
                                        #  ------------------------------//------------//
                                        #  ------------// 1 //----------------------//
                                        ft.Container(
                                            width=400,
                                            height=450,
                                            border_radius=ft.border_radius.all(10),
                                            gradient=ft.LinearGradient(
                                                colors=[
                                                    "#0050C1",
                                                    "#311B92"
                                                ],
                                                begin=ft.alignment.top_left,
                                                end=ft.alignment.bottom_left
                                            ),
                                            content=ft.Column(
                                                controls=[
                                                    #  -----------//-------//
                                                    ft.Container(
                                                        margin=ft.margin.only(top=20),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Image(
                                                                    src="assets/stickers/interview.png",
                                                                    height=100,
                                                                    width=100
                                                                )
                                                            ]
                                                        )
                                                    ),

                                                    #  -----------------//-----------------//
                                                    ft.Container(
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.Text(
                                                                    "vocal training".capitalize(),
                                                                    color="white",
                                                                    size=20,
                                                                    font_family="Raleway-bold"
                                                                )
                                                            ]
                                                        )
                                                    ),

                                                    #  ------------// ----------------//
                                                    ft.Container(
                                                        margin=ft.margin.only(left=20, right=20),
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            wrap=True,
                                                            controls=[
                                                                ft.Text(
                                                                    "Designed to improve singing skills,"
                                                                    " these courses cover vocal techniques, breathing"
                                                                    " exercises, pitch control, and performance skills "
                                                                    "the course has specified duration attached to it "
                                                                    "with all the details entered will be saved",
                                                                    color="white",
                                                                    no_wrap=False,
                                                                    size=20
                                                                )
                                                            ]
                                                        )
                                                    ),

                                                    ft.Container(
                                                        margin=ft.margin.only(left=20, top=10),
                                                        content=ft.Row(
                                                            controls=[
                                                                ft.ElevatedButton(
                                                                    icon=ft.icons.APP_REGISTRATION_ROUNDED,
                                                                    icon_color="white",
                                                                    height=60,
                                                                    width=200,
                                                                    text="register course".title(),
                                                                    elevation=None,
                                                                    style=ft.ButtonStyle(
                                                                        bgcolor="#212121",
                                                                        color="white",

                                                                    ),
                                                                    #  ------------the click function-------//
                                                                    on_click={},
                                                                )
                                                            ]
                                                        )
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                ),
                ft.Container(
                    height=300
                )
            ]
        )
