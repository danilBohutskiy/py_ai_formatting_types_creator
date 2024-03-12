import customtkinter
from classes.formatters.mappings.FormatterMapping import FormatterMapping

class App(customtkinter.CTk):

    SETTINGS_APP_TITLE = 'AI App'
    SETTINGS_GEOMETRY_RESOLUTION = '800x600'

    def __init__(self):
        super().__init__()

        self.title(self.SETTINGS_APP_TITLE)
        self.geometry(self.SETTINGS_GEOMETRY_RESOLUTION)
        customtkinter.set_appearance_mode("dark")

    # ============================= Public methods =============================================#

    def render(self):
        self._render_sidebar()
        self._render_main()

        self.mainloop()

    # ============================= Content - Start =============================================#

    # Main: START
    def _render_main(self):
        # Frame
        self._render_frame_main()

        # Textarea input
        self._render_main_label_to_textarea_input()
        self._render_main_texarea_input()

        # Textarea output
        self._render_main_label_to_textarea_output()
        self._render_main_texarea_output()

    def _render_main_label_to_textarea_input(self, text = "Input text"):
        self.main_frame_label_input_textarea = customtkinter.CTkLabel(self.main_frame, text=text)
        self.main_frame_label_input_textarea.pack(side='top')

    def _render_main_texarea_input(self):
        self.main_textbox_input = customtkinter.CTkTextbox(master=self.main_frame, width=800)
        self.main_textbox_input.pack(side="top")

    def _render_main_label_to_textarea_output(self, text = "Output text"):
        self.main_frame_label_output_textarea = customtkinter.CTkLabel(self.main_frame, text=text)
        self.main_frame_label_output_textarea.pack(side='top')

    def _render_main_texarea_output(self):
        self.main_textbox_output = customtkinter.CTkTextbox(master=self.main_frame, height=500, width=800)
        self.main_textbox_output.pack(side="bottom")

    def _render_frame_main(self):
        self.main_frame = customtkinter.CTkFrame(self, width=600, height=800)
        self.main_frame.pack(side="right", fill="y", expand=True)

    # ============================= Content - End =============================================#

    # ============================= Sidebar - Start =============================================#

    def _render_sidebar(self):
        # Frame
        self._render_frame_sidebar()

        # Button "Generate"
        self._render_sidebar_generate_button()

        # Dropdown "Format Type"
        self._render_sidebar_label_to_dropdown_type()
        self._render_sidebar_dropdown()

    def _render_frame_sidebar(self):
        self.sidebar_frame = customtkinter.CTkFrame(self, width=200, height=800, border_width=2)
        self.sidebar_frame.pack(side="left", fill="y", expand=True)

    def _render_sidebar_generate_button(self, text = "Generate"):
        self.sidebar_button = customtkinter.CTkButton(self.sidebar_frame, text=text)
        self.sidebar_button.pack(side="bottom", anchor="sw", pady=10, padx=20)

    def _render_sidebar_label_to_dropdown_type(self, text = "Select style text format"):
        self.sidebar_label_dropdown_type = customtkinter.CTkLabel(self.sidebar_frame, text=text)
        self.sidebar_label_dropdown_type.pack(side='top', pady=10, padx=20)

    def _render_sidebar_dropdown(self):
        self.sidebar_dropdown_format = customtkinter.CTkComboBox(self.sidebar_frame, values=FormatterMapping.get_format_types())
        self.sidebar_dropdown_format.pack(side="top", pady=0, padx=0)

    # ============================= Sidebar - End =============================================#