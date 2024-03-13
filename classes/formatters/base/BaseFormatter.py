import re

class BaseFormatter:
    def normalize_line(self, text):
        return re.sub(r'\s+', ' ', text).strip()

    def is_empty_value(self, value):
        return not value.strip() 

    def format(self, character_name, character_description_text):
        raise NotImplementedError("The method must be implemented in subclasses!")