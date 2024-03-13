import re

class BaseFormatter:
    def normalize_line(self, text):
        return re.sub(r'\s+', ' ', text).strip()

    def format(self, charachter_name, charachter_description_text):
        raise NotImplementedError("The method must be implemented in subclasses!")