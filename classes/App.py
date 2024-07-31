import customtkinter
from classes.mappings.FormatterMapping import FormatterMapping
from classes.mappings.TemplateMapping import TemplateMapping
from classes.factories.FormatterFactory import FormatterFactory
from classes.factories.TemplateFactory import TemplateFactory

class App(customtkinter.CTk):

    SETTINGS_APP_TITLE = 'Character Formatting Types Creator'
    SETTINGS_GEOMETRY_RESOLUTION = '800x600'

    DEFAULT_CHARACTER_NAME = 'Unknown'

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

    def _render_main_label_to_textarea_input(self, text = "Character description"):
        self.main_frame_label_input_textarea = customtkinter.CTkLabel(self.main_frame, text=text)
        self.main_frame_label_input_textarea.pack(side='top')

    def _render_main_texarea_input(self):
        self.main_frame_textbox_input = customtkinter.CTkTextbox(master=self.main_frame, width=700)
        self.main_frame_textbox_input.pack(side="top")

    def _render_main_label_to_textarea_output(self, text = "Generated text"):
        self.main_frame_label_output_textarea = customtkinter.CTkLabel(self.main_frame, text=text)
        self.main_frame_label_output_textarea.pack(side='top')

    def _render_main_texarea_output(self):
        self.main_frame_textbox_output = customtkinter.CTkTextbox(master=self.main_frame, height=500, width=700)
        self.main_frame_textbox_output.pack(side="bottom")

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

        # Input "Character name"
        self._render_sidebar_label_character_name()
        self._render_sidebar_input_character_name()

        # Dropdown "Format Type"
        self._render_sidebar_label_dropdown_type()
        self._render_sidebar_dropdown_format_type()

        # Dropdown "Template"
        self._render_sidebar_dropdown_template()
        self._render_sidebar_label_dropdown_template()

    def _render_frame_sidebar(self):
        self.sidebar_frame = customtkinter.CTkFrame(self, width=200, height=800, border_width=2)
        self.sidebar_frame.pack(side="left", fill="y", expand=True)

    def _render_sidebar_generate_button(self, text = "Generate"):
        self.sidebar_button = customtkinter.CTkButton(self.sidebar_frame, text=text, command=self.button_generate_output)
        self.sidebar_button.pack(side="bottom", anchor="sw", pady=10, padx=20)

    def _render_sidebar_label_dropdown_type(self, text = "Select style text format"):
        self.sidebar_label_dropdown_type = customtkinter.CTkLabel(self.sidebar_frame, text=text)
        self.sidebar_label_dropdown_type.pack(side='top')

    def _render_sidebar_dropdown_format_type(self):
        self.sidebar_dropdown_format = customtkinter.CTkComboBox(self.sidebar_frame, values=FormatterMapping.get_format_types())
        self.sidebar_dropdown_format.pack(side="top", pady=0, padx=0)

    def _render_sidebar_label_dropdown_template(self, text = "Use template"):
        self.sidebar_label_dropdown_template = customtkinter.CTkLabel(self.sidebar_frame, text=text)
        self.sidebar_label_dropdown_template.pack(side='bottom')

    def _render_sidebar_dropdown_template(self):
        self.sidebar_dropdown_template = customtkinter.CTkComboBox(self.sidebar_frame, values=TemplateMapping.get_template_types(), command=self.change_template)
        self.sidebar_dropdown_template.pack(side="bottom")

    def _render_sidebar_label_character_name(self, text = "Input character name"):
        self.sidebar_label_character_name = customtkinter.CTkLabel(self.sidebar_frame, text=text)
        self.sidebar_label_character_name.pack(side='top')

    def _render_sidebar_input_character_name(self, placeholder = "Character name"):
        self.sidebar_input_character_name = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text=placeholder)
        self.sidebar_input_character_name.pack(side='top')

    # ============================= Sidebar - End =============================================#
        
    # ============================= Events ====================================================#

    def button_generate_output(self):
        character_name = self.sidebar_input_character_name.get()
        if (character_name == ''):
            character_name = self.DEFAULT_CHARACTER_NAME
        character_description = self.main_frame_textbox_input.get(0.0, 'end')
        format_type = self.sidebar_dropdown_format.get()

        formatter = FormatterFactory.create(format_type)
        formatted_text = formatter.format(character_name, character_description)
        self._fill_output(formatted_text)

    def change_template(self, choice):
        template = TemplateFactory.create(choice)
        if (template is None):
            return

        template_text = template.get()
        self._fill_input(template_text)

    def _clear_output(self):
        self.main_frame_textbox_output.delete(0.0, 'end')

    def _clear_input(self):
        self.main_frame_textbox_input.delete(0.0, 'end')

    def _fill_output(self, output_text):
        self._clear_output()
        self.main_frame_textbox_output.insert('end', output_text)

    def _fill_input(self, input_text):
        self._clear_input()
        self.main_frame_textbox_input.insert('end', input_text)