import flet as ft
import string
import pygame
import time


class DrumKits(ft.UserControl):
    """the class for the drum kits"""

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.letters = string.ascii_letters
        self.letter_blocks = ft.Text()
        self.controller_keys = ft.GridView(
            expand=1,
            runs_count=4,
            max_extent=150,
            child_aspect_ratio=0.8,
            spacing=3,
            run_spacing=5,
            padding=20,
            width=1300,
        )
        self.beat_box_frequencies = ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5", "D5", "SD", "CY", "BD", "OH", "L",
                                     "RS", "CLK"]

    #  --------------------------------//------------------------------//
    def getting_all_controller_keys(self):
        """the function will create the container for the controls"""
        try:
            for letter in self.beat_box_frequencies:
                self.controller_keys.controls.append(
                    ft.Card(
                        color="white",
                        elevation=True,
                        content=ft.Container(
                            data=letter,
                            margin=ft.margin.only(top=70),
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Text(f"{letter}", size=30, weight=ft.FontWeight.W_500,
                                                    color="#212121")]
                                    )
                                ]
                            ),
                            #  ---------------the onclick function will be here----------//
                            on_click=self.on_click_beat_box

                        )
                    )
                )
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

    #  -------------------// the onclick function for the beat box here--------------//
    def on_click_beat_box(self, e):
        """the function will generate beatbox samples"""
        try:
            self.letter_blocks = e.control.data
            #  -----------------the controls for the if statements here--------------//
            if self.letter_blocks == "C4":
                # Initialize the pygame mixer
                pygame.mixer.init()
                # Create a pygame Sound object by loading an MP3 file
                pygame.mixer.music.load("assets/loops/808-bass-boom-hard-trap-loop-8-11510.mp3")
                # Play the MP3 file
                pygame.mixer.music.play()
                # Wait for the audio to finish playing (optional)
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            #  ---------------------//--------------------------//
            elif self.letter_blocks == "D4":
                # Initialize the pygame mixer
                pygame.mixer.init()
                # Create a pygame Sound object by loading an MP3 file
                pygame.mixer.music.load("assets/loops/909-sn-01a-rev-106047.mp3")
                # Play the MP3 file
                pygame.mixer.music.play()
                # Wait for the audio to finish playing (optional)
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            #  ---------------------//--------------------------//
            elif self.letter_blocks == "E4":
                # Initialize the pygame mixer
                pygame.mixer.init()
                # Create a pygame Sound object by loading an MP3 file
                pygame.mixer.music.load("assets/loops/071868_bass-impact-40571.mp3")
                # Play the MP3 file
                pygame.mixer.music.play()
                # Wait for the audio to finish playing (optional)
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            #  --------------------//--------------------------//
            elif self.letter_blocks == "F4":
                # Initialize the pygame mixer
                pygame.mixer.init()
                # Create a pygame Sound object by loading an MP3 file
                pygame.mixer.music.load("assets/loops/080038_bass_7wav-88247.mp3")
                # Play the MP3 file
                pygame.mixer.music.play()
                # Wait for the audio to finish playing (optional)
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            #  ----------------------//---------------//
            #  --------------------//--------------------------//
            elif self.letter_blocks == "F4":
                # Initialize the pygame mixer
                pygame.mixer.init()
                # Create a pygame Sound object by loading an MP3 file
                pygame.mixer.music.load("assets/loops/080207_bass_9wav-88245.mp3")
                # Play the MP3 file
                pygame.mixer.music.play()
                # Wait for the audio to finish playing (optional)
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            #  -----------------------//---------------------------//-----------------//
            elif self.letter_blocks == "G4":
                # Initialize the pygame mixer
                pygame.mixer.init()
                # Create a pygame Sound object by loading an MP3 file
                pygame.mixer.music.load("assets/loops/087403_kickwav-86944.mp3")
                # Play the MP3 file
                pygame.mixer.music.play()
                # Wait for the audio to finish playing (optional)
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            #  -----------------------//----------------------------//-----------//
            elif self.letter_blocks == "A4":
                # Initialize the pygame mixer
                pygame.mixer.init()
                # Create a pygame Sound object by loading an MP3 file
                pygame.mixer.music.load("assets/loops/bass-rvb-6-107514.mp3")
                # Play the MP3 file
                pygame.mixer.music.play()
                # Wait for the audio to finish playing (optional)
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            #  -----------------------//--------------------------//--------//
            elif self.letter_blocks == "B4":
                # Initialize the pygame mixer
                pygame.mixer.init()
                # Create a pygame Sound object by loading an MP3 file
                pygame.mixer.music.load("assets/loops/bassdrum-8-45879.mp3")
                # Play the MP3 file
                pygame.mixer.music.play()
                # Wait for the audio to finish playing (optional)
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            #  ---------------------------//-------------------------//
            elif self.letter_blocks == "C5":
                # Initialize the pygame mixer
                pygame.mixer.init()
                # Create a pygame Sound object by loading an MP3 file
                pygame.mixer.music.load("assets/loops/deep-bassy-drum-102346.mp3")
                # Play the MP3 file
                pygame.mixer.music.play()
                # Wait for the audio to finish playing (optional)
                while pygame.mixer.music.get_busy():
                    time.sleep(1)

            #  --------------------------------//-------------------------------------//
            elif self.letter_blocks == "D5":
                # Initialize the pygame mixer
                pygame.mixer.init()
                # Create a pygame Sound object by loading an MP3 file
                pygame.mixer.music.load("assets/loops/fx-reversed-149279.mp3")
                # Play the MP3 file
                pygame.mixer.music.play()
                # Wait for the audio to finish playing (optional)
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            #  -------------------------//-----------------------------//
            elif self.letter_blocks == "SD":
                # Initialize the pygame mixer
                pygame.mixer.init()
                # Create a pygame Sound object by loading an MP3 file
                pygame.mixer.music.load("assets/loops/kick-bass-808-drums-loop-6-11282.mp3")
                # Play the MP3 file
                pygame.mixer.music.play()
                # Wait for the audio to finish playing (optional)
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            #  ---------------------------//----------------------------//
            elif self.letter_blocks == "CY":
                # Initialize the pygame mixer
                pygame.mixer.init()
                # Create a pygame Sound object by loading an MP3 file
                pygame.mixer.music.load("assets/loops/kick-hardstyle-149281.mp3")
                # Play the MP3 file
                pygame.mixer.music.play()
                # Wait for the audio to finish playing (optional)
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            #  ---------------------------//----------------------------------//
            elif self.letter_blocks == "BD":
                # Initialize the pygame mixer
                pygame.mixer.init()
                # Create a pygame Sound object by loading an MP3 file
                pygame.mixer.music.load("assets/loops/pd-kick-02-97657.mp3")
                # Play the MP3 file
                pygame.mixer.music.play()
                # Wait for the audio to finish playing (optional)
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            #  -----------------------------------//-------------------------//
            elif self.letter_blocks == "OH":
                # Initialize the pygame mixer
                pygame.mixer.init()
                # Create a pygame Sound object by loading an MP3 file
                pygame.mixer.music.load("assets/loops/sanfte-hardstyle-kick-149796.mp3")
                # Play the MP3 file
                pygame.mixer.music.play()
                # Wait for the audio to finish playing (optional)
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            #  --------------------------------//-------------------------------//
            elif self.letter_blocks == "L":
                # Initialize the pygame mixer
                pygame.mixer.init()
                # Create a pygame Sound object by loading an MP3 file
                pygame.mixer.music.load("assets/loops/sub-rush-3-85033.mp3")
                # Play the MP3 file
                pygame.mixer.music.play()
                # Wait for the audio to finish playing (optional)
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            #  ----------------------------//------------------------//---------------//
            elif self.letter_blocks == "RS":
                # Initialize the pygame mixer
                pygame.mixer.init()
                # Create a pygame Sound object by loading an MP3 file
                pygame.mixer.music.load("assets/loops/sub-rush-4-104152.mp3")
                # Play the MP3 file
                pygame.mixer.music.play()
                # Wait for the audio to finish playing (optional)
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            #  ----------------------------//---------------------------//
            elif self.letter_blocks == "CLK":
                # Initialize the pygame mixer
                pygame.mixer.init()
                # Create a pygame Sound object by loading an MP3 file
                pygame.mixer.music.load("assets/loops/techno-bassline-81119.mp3")
                # Play the MP3 file
                pygame.mixer.music.play()
                # Wait for the audio to finish playing (optional)
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            #  ---------------------//thank you God i know you are with me---------------------//
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
        return self.controller_keys


class PianoKeys(ft.UserControl):
    """class for the piano here"""

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.piano_clicked_key = ft.Text()
        #  ----------------piano keys will be here-------------//
        self.piano_keys = ft.GridView(
            expand=10,
            runs_count=6,
            max_extent=90,
            child_aspect_ratio=0.2,
            spacing=10,
            run_spacing=10,
            padding=30,
            width=1500,
        )

        #  ----------------// piano notes will be here-------------------//
        self.notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

        #  ------------------// function for the piano here------------//

    def getting_piano_keys(self):
        """the function has all the basic notes for the piano"""
        try:
            if self.piano_keys:
                notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
                for single_note in notes:
                    self.piano_keys.controls.append(
                        ft.Container(
                            shadow=ft.BoxShadow(
                                blur_radius=4,
                                blur_style=ft.ShadowBlurStyle.INNER,
                                color="#311B92",
                            ),
                            data=single_note,
                            bgcolor="white",
                            height=600,
                            border_radius=ft.border_radius.only(bottom_left=10, bottom_right=10),
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.END,
                                        controls=[
                                            ft.Container(
                                                width=50,
                                                height=300,
                                                bgcolor="black",
                                                border_radius=ft.border_radius.only(bottom_left=10),
                                            ),

                                        ]
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Container(
                                                margin=ft.margin.only(top=50, left=30),
                                                content=ft.Row(
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.Text(
                                                            f"{single_note}",
                                                            style=ft.TextThemeStyle.HEADLINE_MEDIUM,
                                                            weight=ft.FontWeight.W_700,
                                                            color="#334A52"
                                                        )
                                                    ]
                                                ),
                                            )
                                        ]
                                    )
                                ]
                            ),
                            on_click=self.on_click
                        ),

                    )
                else:
                    return False

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

    #  -----------------------------------//---------------------------------//
    def on_click(self, e):
        """the function will be triggered when the container is clicked"""
        try:
            self.piano_clicked_key = e.control.data
            #  ------------------getting the sound notes here when the button is clicked---------//
            if self.piano_clicked_key == "C":
                # Initialize the pygame mixer
                pygame.mixer.init()
                # Create a pygame Sound object by loading an MP3 file
                pygame.mixer.music.load("assets/piano/do-stretched-7162.mp3")
                # Play the MP3 file
                pygame.mixer.music.play()
                # Wait for the audio to finish playing (optional)
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            #  ------------------------//------------------------//
            elif self.piano_clicked_key == "C#":
                # Initialize the pygame mixer
                pygame.mixer.init()
                # Create a pygame Sound object by loading an MP3 file
                pygame.mixer.music.load("assets/piano/c1-94637.mp3")
                # Play the MP3 file
                pygame.mixer.music.play()
                # Wait for the audio to finish playing (optional)
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            #  ---------------------------------//--------------------//
            elif self.piano_clicked_key == "D":
                # Initialize the pygame mixer
                pygame.mixer.init()
                # Create a pygame Sound object by loading an MP3 file
                pygame.mixer.music.load("assets/piano/do-stretched-7162.mp3")
                # Play the MP3 file
                pygame.mixer.music.play()
                # Wait for the audio to finish playing (optional)
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            #  ------------------------------//-----------------------//
            elif self.piano_clicked_key == "D#":
                # Initialize the pygame mixer
                pygame.mixer.init()
                # Create a pygame Sound object by loading an MP3 file
                pygame.mixer.music.load("assets/piano/la-80237.mp3")
                # Play the MP3 file
                pygame.mixer.music.play()
                # Wait for the audio to finish playing (optional)
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            #  --------------------------//------------------------//
            elif self.piano_clicked_key == "E":
                # Initialize the pygame mixer
                pygame.mixer.init()
                # Create a pygame Sound object by loading an MP3 file
                pygame.mixer.music.load("assets/piano/mi-80239.mp3")
                # Play the MP3 file
                pygame.mixer.music.play()
                # Wait for the audio to finish playing (optional)
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            #  ---------------------------//---------------------------//
            elif self.piano_clicked_key == "F":
                # Initialize the pygame mixer
                pygame.mixer.init()
                # Create a pygame Sound object by loading an MP3 file
                pygame.mixer.music.load("assets/piano/pianoffb6-audiotrimmercom-36364.mp3")
                # Play the MP3 file
                pygame.mixer.music.play()
                # Wait for the audio to finish playing (optional)
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            #  ----------------------//-------------------//---------//
            elif self.piano_clicked_key == "F#":
                # Initialize the pygame mixer
                pygame.mixer.init()
                # Create a pygame Sound object by loading an MP3 file
                pygame.mixer.music.load("assets/piano/pianomfc6-audiotrimmercom-36790.mp3")
                # Play the MP3 file
                pygame.mixer.music.play()
                # Wait for the audio to finish playing (optional)
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            #  -------------------------//-----------------------//
            elif self.piano_clicked_key == "G":
                # Initialize the pygame mixer
                pygame.mixer.init()
                # Create a pygame Sound object by loading an MP3 file
                pygame.mixer.music.load("assets/piano/pianoffg6-audiotrimmercom-36632.mp3")
                # Play the MP3 file
                pygame.mixer.music.play()
                # Wait for the audio to finish playing (optional)
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            #  --------------------//---------------------//----------//
            elif self.piano_clicked_key == "G#":
                # Initialize the pygame mixer
                pygame.mixer.init()
                # Create a pygame Sound object by loading an MP3 file
                pygame.mixer.music.load("assets/loops/080038_bass_7wav-88247.mp3")
                # Play the MP3 file
                pygame.mixer.music.play()
                # Wait for the audio to finish playing (optional)
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            #  -------------------------//--------------------------//
            elif self.piano_clicked_key == "A":
                # Initialize the pygame mixer
                pygame.mixer.init()
                # Create a pygame Sound object by loading an MP3 file
                pygame.mixer.music.load("assets/piano/piano-slam-97095.mp3")
                # Play the MP3 file
                pygame.mixer.music.play()
                # Wait for the audio to finish playing (optional)
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            #  --------------------------//--------------------------//
            elif self.piano_clicked_key == "A#":
                # Initialize the pygame mixer
                pygame.mixer.init()
                # Create a pygame Sound object by loading an MP3 file
                pygame.mixer.music.load("assets/piano/piano-reverse-101278.mp3")
                # Play the MP3 file
                pygame.mixer.music.play()
                # Wait for the audio to finish playing (optional)
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            #  ----------------------//-------------------------//
            elif self.piano_clicked_key == "B":
                # Initialize the pygame mixer
                pygame.mixer.init()
                # Create a pygame Sound object by loading an MP3 file
                pygame.mixer.music.load("assets/piano/mi-80239.mp3")
                # Play the MP3 file
                pygame.mixer.music.play()
                # Wait for the audio to finish playing (optional)
                while pygame.mixer.music.get_busy():
                    time.sleep(1)
            else:
                self.page.snack_bar = ft.SnackBar(
                    content=ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Text(
                                    "out of range key"
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
        return self.piano_keys


class InstrumentsView(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.fonts = {
            "OpenSans": "assets/fonts/static/OpenSans-Light.ttf",
            "Raleway": "assets/fonts/static/Raleway-Light.ttf",
            "Roboto-bold": "assets/fonts/Roboto-Bold.ttf",
            "Roboto-black": "assets/fonts/Roboto-Black.ttf",
            "Raleway-bold": "assets/fonts/static/Raleway-Bold.ttf"
        }
        #  -----------------calling the piano keys function here------//
        self.piano_keys = PianoKeys(page)
        self.piano_keys.getting_piano_keys()

        #  -----------------// calling the controller keys for the bit box-----------//
        self.controller_keys = DrumKits(page)
        self.controller_keys.getting_all_controller_keys()

    def build(self):
        return ft.ListView(
            expand=1,
            auto_scroll=True,
            spacing=10,
            height=800,
            scale=1.0,
            controls=[
                #  ------------// container that will wrap all the controls
                ft.Container(
                    content=ft.Column(
                        controls=[
                            #  ----------------// container for the text will be here---//
                            ft.Container(
                                margin=ft.margin.only(top=30),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text(
                                            "visual instrument trainer".capitalize(),
                                            color="#212121",
                                            font_family="Raleway",
                                            style=ft.TextThemeStyle.DISPLAY_SMALL
                                        )
                                    ]
                                )
                            ),

                            #  ---------------/container for the visual instruments/-----------------//
                            ft.Container(
                                margin=ft.margin.only(left=20, right=30, top=20),
                                bgcolor="#cfd8dc",
                                border_radius=ft.border_radius.all(10),
                                shadow=ft.BoxShadow(
                                    blur_radius=4,
                                    blur_style=ft.ShadowBlurStyle.INNER,
                                    color="#311B92",
                                ),
                                content=ft.Row(
                                    controls=[
                                        ft.Tabs(
                                            scrollable=True,
                                            animation_duration=9,
                                            animate_size=300,
                                            selected_index=0,
                                            tabs=[
                                                #  ---------------// first tab for the piano here //----------//
                                                ft.Tab(
                                                    tab_content=ft.Container(
                                                        content=ft.Row(
                                                            controls=[
                                                                ft.Icon(ft.icons.PIANO_ROUNDED, size=30, color="black"),
                                                                ft.Text("piano".capitalize(), size=20, color="black")
                                                            ]
                                                        )
                                                    ),
                                                    content=ft.Container(
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                self.piano_keys
                                                            ]
                                                        )
                                                    )
                                                ),
                                                #  ---------------// second tab--------//
                                                ft.Tab(
                                                    tab_content=ft.Container(
                                                        content=ft.Row(
                                                            controls=[
                                                                ft.Icon(ft.icons.KEYBOARD_HIDE_ROUNDED, size=30, color="black"),
                                                                ft.Text("drums".capitalize(), size=20, color="black")
                                                            ]
                                                        )
                                                    ),
                                                    content=ft.Container(
                                                        content=ft.Row(
                                                            # alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                self.controller_keys
                                                            ]
                                                        )
                                                    )
                                                ),
                                            ],
                                            width=1300,
                                            height=600
                                        )
                                    ]
                                )
                            ),
                        ]
                    )
                ),
                #  --------------// new container here------------//
                ft.Container(
                    height=200
                )
            ]
        )
