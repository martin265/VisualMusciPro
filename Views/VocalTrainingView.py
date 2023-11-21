import flet as ft
import pyaudio
import os
import wave
import pygame
import time


class RecordedFiles(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.recordings_path = "recordings"
        self.output_folder = "recordings"  # Change this to the folder where you want to save the recordings
        self.filename = "recordings"  # Change this to the desired filename
        self.record_duration = 10  # Change this to adjust the recording duration (in seconds)
        self.single_recording = ft.Text()
        self.audio_file = ft.Text(),
        self.recorded_files = ft.Dropdown(
            width=400,
            height=100,
            on_change=self.get_selected_recording,
            autofocus=True,
            prefix_icon=ft.icons.MUSIC_NOTE_ROUNDED,
            prefix_style=ft.TextStyle(
                color="white",
            ),
            helper_text="select your recordings",
            helper_style=ft.TextStyle(
                color="white"
            ),
            border_color="white",
            label="recordings".capitalize(),
            label_style=ft.TextStyle(
                color="white"
            ),
            border_radius=ft.border_radius.all(5),
            focused_border_color="white",
        )

        self.vocal_analyzer = ft.Dropdown(
            width=400,
            height=100,
            autofocus=True,
            prefix_icon=ft.icons.VOICE_CHAT_ROUNDED,
            prefix_style=ft.TextStyle(
                color="white",
            ),
            helper_text="select your analyser",
            helper_style=ft.TextStyle(
                color="white"
            ),
            border_color="white",
            label="analyzer".capitalize(),
            label_style=ft.TextStyle(
                color="white"
            ),
            border_radius=ft.border_radius.all(5),
            focused_border_color="white",
        )

    #  --------------------// function to get the recorded files---------------------//
    def fetch_all_recorded_files(self):
        try:
            for self.single_recording in os.listdir(self.recordings_path):
                self.recorded_files.options.append(
                    ft.dropdown.Option(
                        self.single_recording
                    )
                )

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

    def get_selected_recording(self, e):
        self.audio_file = self.recorded_files.value
        self.page.update()
        # Initialize the pygame mixer
        pygame.mixer.init()
        # Create a pygame Sound object by loading an MP3 file
        pygame.mixer.music.load(f"recordings/{self.audio_file}")
        # Play the MP3 file
        pygame.mixer.music.play()
        # Wait for the audio to finish playing (optional)
        while pygame.mixer.music.get_busy():
            time.sleep(1)

    #  --------------------// function to get the recorded files---------------------//
    def fetch_analyzer(self):
        try:
            analyzers = ["librosa numpy", "skit learn"]
            for single_analyzer in analyzers:
                self.vocal_analyzer.options.append(
                    ft.dropdown.Option(
                        single_analyzer
                    )
                )

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

    def build(self):
        return print("hello")


class ActiveMicrophone(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

        self.duration = float(30)
        self.recordings_path = "recordings"
        self.output_folder = "recordings"  # Change this to the folder where you want to save the recordings
        self.filename = "recordings"  # Change this to the desired filename
        self.record_duration = 10  # Change this to adjust the recording duration (in seconds)
        self.single_recording = ft.Text()

        self.microphone = ft.Dropdown(
            width=350,
            height=100,
            autofocus=True,
            prefix_icon=ft.icons.MIC_ROUNDED,
            prefix_style=ft.TextStyle(
                color="white",

            ),
            helper_text="select your active microphone",
            helper_style=ft.TextStyle(
                color="white"
            ),
            border_color="white",
            label="active mic".capitalize(),
            label_style=ft.TextStyle(
                color="white"
            ),
            border_radius=ft.border_radius.all(5),
            focused_border_color="white",

        )

        #  ---------------------// getting the recording channel here-----------------//
        self.recording_channel = ft.Dropdown(
            width=350,
            height=100,
            autofocus=True,
            prefix_icon=ft.icons.WIFI_CHANNEL_ROUNDED,
            prefix_style=ft.TextStyle(
                color="white",

            ),
            helper_text="select your active channel",
            helper_style=ft.TextStyle(
                color="white"
            ),
            border_color="white",
            label="active channel".capitalize(),
            label_style=ft.TextStyle(
                color="white"
            ),
            border_radius=ft.border_radius.all(5),
            focused_border_color="white",
        )
        #  ------------------------------//getting the recording duration here----------//
        self.recording_duration = ft.TextField(
            width=350,
            height=100,
            autocorrect=True,
            autofocus=True,
            enable_suggestions=True,
            prefix_icon=ft.icons.TIMELAPSE_ROUNDED,
            prefix_style=ft.TextStyle(
                color="white",

            ),
            helper_text="numbers only",
            helper_style=ft.TextStyle(
                color="white"
            ),
            border_color="white",
            label="recording duration".capitalize(),
            label_style=ft.TextStyle(
                color="white"
            ),
            border_radius=ft.border_radius.all(5),
            capitalization=ft.TextCapitalization.WORDS,
            focused_border_color="white",
            keyboard_type=ft.KeyboardType.NAME,
            color="white",
        )
        #  ---------------------//getting the file name here for the recording--------------//
        self.recording_filename = ft.TextField(
            width=350,
            height=100,
            autocorrect=True,
            autofocus=True,
            enable_suggestions=True,
            prefix_icon=ft.icons.FILE_OPEN_ROUNDED,
            prefix_style=ft.TextStyle(
                color="white",

            ),
            helper_text="characters only",
            helper_style=ft.TextStyle(
                color="white"
            ),
            border_color="white",
            label="recording filename".capitalize(),
            label_style=ft.TextStyle(
                color="white"
            ),
            border_radius=ft.border_radius.all(5),
            capitalization=ft.TextCapitalization.WORDS,
            focused_border_color="white",
            color="white",
            keyboard_type=ft.KeyboardType.NAME
        )

        #  ---------------------the grid view for the audio files here-----------------//
        self.audio_gallery = ft.GridView(
            runs_count=4,
            expand=True,
            max_extent=300,
            spacing=10
        )

        #  -------------------------the drop down for the audio file--------------//
        self.recorded_files = ft.Dropdown(
            width=350,
            height=100,
            autofocus=True,
            prefix_icon=ft.icons.MUSIC_NOTE_ROUNDED,
            prefix_style=ft.TextStyle(
                color="white",
            ),
            helper_text="select your recordings",
            helper_style=ft.TextStyle(
                color="white"
            ),
            border_color="white",
            label="recordings".capitalize(),
            label_style=ft.TextStyle(
                color="white"
            ),
            border_radius=ft.border_radius.all(5),
            focused_border_color="white",
        )

    def validate_input_fields(self):
        """the function to validate the input fields here--------"""
        try:
            if not self.microphone.value:
                self.microphone.error_text = "select active mic first".capitalize()
                self.page.update()
            #  ----------------------------//-------------------------------------//
            elif not self.recording_channel.value:
                self.recording_channel.error_text = "select active channel".capitalize()
                self.page.update()
            #  --------------------------------//---------------------------------//
            elif not self.recording_duration.value:
                self.recording_duration.error_text = "enter the time to record".capitalize()
                self.page.update()
            #  -------------------------------------//-------------------------------//
            elif not self.recording_filename.value:
                self.recording_filename.error_text = "enter the filename for saving".capitalize()
                self.page.update()
            #  -------------------------------------//-----------------------------------//
            else:
                self.record_audio(self.output_folder, self.recording_filename.value + ".wav",
                                  duration=int(self.recording_duration.value))

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

    #  -----------------------getting all the available microphones------------------//
    def list_microphones(self):
        p = pyaudio.PyAudio()

        device_count = p.get_device_count()

        for i in range(device_count):
            device_info = p.get_device_info_by_index(i)
            device_name = device_info["name"]
            device_is_input = device_info["maxInputChannels"] > 0

            if device_is_input:
                self.microphone.options.append(
                    ft.dropdown.Option(
                        device_name
                    )
                )

        p.terminate()

        #  ----------------------------function to start the recorder here------------------------//

    def record_audio(self, output_folder, filename, duration=5, channels=1, sample_rate=44100):
        # Initialize PyAudio
        audio = pyaudio.PyAudio()

        # Configure the audio stream
        stream = audio.open(format=pyaudio.paInt16,
                            channels=channels,
                            rate=sample_rate,
                            input=True,
                            frames_per_buffer=1024)

        # Start recording
        self.page.snack_bar = ft.SnackBar(
            bgcolor="#0050C1",
            content=ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "your recording has started".capitalize(),
                            weight=ft.FontWeight.W_700,
                            color="white"
                        )
                    ]
                )
            )
        )
        self.page.snack_bar.open = True
        self.page.update()

        frames = []
        for _ in range(0, int(sample_rate / 1024 * duration)):
            data = stream.read(1024)
            frames.append(data)

        # finished recording
        self.page.snack_bar = ft.SnackBar(
            bgcolor="#0050C1",
            content=ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "finished recording".capitalize(),
                            weight=ft.FontWeight.W_700,
                            color="white"
                        )
                    ]
                )
            )
        )
        self.page.snack_bar.open = True
        self.page.update()

        # Stop and close the audio stream
        stream.stop_stream()
        stream.close()
        audio.terminate()

        # Save the recorded audio to a WAV file
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
        file_path = os.path.join(output_folder, filename)
        with wave.open(file_path, 'wb') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
            wf.setframerate(sample_rate)
            wf.writeframes(b''.join(frames))

        print(f"Audio saved to {file_path}")

        #  -----------------// getting the active channel here-------------//
        #  --------------------------//the function to list all the available channels here-------------------//

    def show_active_channels(self):
        try:
            py_audios = pyaudio.PyAudio()
            for channel in py_audios.get_default_input_device_info():
                self.recording_channel.options.append(
                    ft.dropdown.Option(
                        channel
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

    def build(self):
        return self.validate_input_fields


class VocalTraining(ft.UserControl):
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

        #  ------------------// calling all microphones------------//
        self.microphones = ActiveMicrophone(page=page)
        self.microphones.list_microphones()
        #  ----------------------//------------------------------//

        self.microphones.show_active_channels()
        # -----------------------------// ----------------------//
        self.recorded_files = RecordedFiles(page=page)
        self.recorded_files.fetch_all_recorded_files()

        # -------------------------//---------------------//
        self.recorded_files.fetch_analyzer()

    def trigger_validations(self, e):
        self.microphones.validate_input_fields()

    def build(self):
        return ft.ListView(
            expand=1,
            auto_scroll=True,
            spacing=10,
            height=800,
            scale=1.0,
            controls=[
                #  -----------------// the first container-------------------//
                ft.Container(
                    margin=ft.margin.only(top=20),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                "vocal trainer".capitalize(),
                                style=ft.TextThemeStyle.DISPLAY_SMALL,
                                font_family="Raleway-bold",
                                color="#311B92"
                            )
                        ]
                    )
                ),

                #  ----------------// --------------------// ----------------//
                ft.Container(
                    content=ft.Row(
                        controls=[
                            #  -------------------//--------------------//
                            ft.Container(
                                margin=ft.margin.only(left=30, top=20),
                                border_radius=ft.border_radius.all(10),
                                width=800,
                                height=600,
                                gradient=ft.LinearGradient(
                                    colors=[
                                        "#0050C1",
                                        "#212121"
                                    ],
                                    begin=ft.alignment.top_left,
                                    end=ft.alignment.bottom_right
                                ),
                                content=ft.Column(
                                    controls=[
                                        #  --------------// -------------------//
                                        ft.Container(
                                            margin=ft.margin.only(top=20),
                                            content=ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    ft.Image(
                                                        src="assets/stickers/guitar.png",
                                                        height=120,
                                                        width=120
                                                    )
                                                ]
                                            )
                                        ),

                                        ft.Container(
                                            margin=ft.margin.only(left=20, right=20, top=20),
                                            content=ft.Row(
                                                wrap=True,
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    ft.Text(
                                                        "The quality of sound produced by the "
                                                        "vocal cords and amplified in the resonating"
                                                        " chambers of the throat and mouth  The span"
                                                        " of pitches that a person's voice can produce"
                                                        " from the lowest to the highest note",
                                                        color="white",
                                                        font_family="Raleway-bold",
                                                        size=18
                                                    )
                                                ]
                                            )
                                        ),

                                        ft.Container(
                                            margin=ft.margin.only(left=20, top=30, right=20),
                                            content=ft.Column(
                                                controls=[
                                                    ft.Row(
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                        controls=[
                                                            self.microphones.microphone,
                                                            self.microphones.recording_channel
                                                        ]
                                                    ),
                                                    ft.Row(
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                        controls=[
                                                            self.microphones.recording_duration,
                                                            self.microphones.recording_filename
                                                        ]
                                                    )
                                                ]
                                            )
                                        ),

                                        #  ------------// container for the buttons here------------//
                                        ft.Container(
                                            margin=ft.margin.only(left=30),
                                            content=ft.Row(
                                                controls=[
                                                    ft.ElevatedButton(
                                                        icon=ft.icons.RECORD_VOICE_OVER_ROUNDED,
                                                        icon_color="white",
                                                        height=60,
                                                        width=200,
                                                        text="start recording".title(),
                                                        elevation=None,
                                                        style=ft.ButtonStyle(
                                                            bgcolor="#212121",
                                                            color="white",

                                                        ),
                                                        #  ------------the click function-------//
                                                        on_click=self.trigger_validations,
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                )
                            ),
                            #  -----------------/ container for vocal analyzer/ --------------------//
                            ft.Container(
                                height=600,
                                width=480,
                                margin=ft.margin.only(top=20),
                                border_radius=ft.border_radius.all(10),
                                gradient=ft.LinearGradient(
                                    colors=[
                                        "#212121",
                                        "#0050C1",
                                    ],
                                    begin=ft.alignment.top_left,
                                    end=ft.alignment.bottom_right
                                ),
                                content=ft.Container(
                                    margin=ft.margin.only(top=20),
                                    content=ft.Column(
                                        controls=[
                                            ft.Row(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    ft.Text(
                                                        "vocal analyzer".capitalize(),
                                                        color="white",
                                                        font_family="Raleway",
                                                        style=ft.TextThemeStyle.DISPLAY_SMALL
                                                    )
                                                ]
                                            ),

                                            #  ----------------// for the stickers
                                            ft.Container(
                                                content=ft.Row(
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.Image(
                                                            src="assets/stickers/mic.png",
                                                            height=200,
                                                            width=200
                                                        )
                                                    ]
                                                )
                                            ),

                                            #  ---------------audio controls here-----------//
                                            ft.Container(
                                                margin=ft.margin.only(top=30),
                                                content=ft.Column(
                                                    controls=[
                                                        ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                self.recorded_files.recorded_files
                                                            ]
                                                        ),

                                                        ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            controls=[
                                                                self.recorded_files.vocal_analyzer
                                                            ]
                                                        ),

                                                        ft.Container(
                                                            margin=ft.margin.only(left=40, right=40),
                                                            content=ft.Row(
                                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                controls=[

                                                                    ft.ElevatedButton(
                                                                        icon=ft.icons.ANALYTICS_ROUNDED,
                                                                        icon_color="white",
                                                                        height=60,
                                                                        width=200,
                                                                        text="analyze audio".title(),
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
                            )
                        ]
                    )
                ),

                ft.Container(
                    height=200,
                )
            ]
        )
