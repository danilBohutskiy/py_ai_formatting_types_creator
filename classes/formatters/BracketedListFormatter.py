from .base.BaseFormatter import BaseFormatter

class BracketedListFormatter(BaseFormatter):
    def format(self, character_name, character_description_text):
        character_name_description = f'Name: {character_name}\n {character_description_text}'
        processed_lines = []
        for line in character_name_description.splitlines():
            proccessed_line = self._process_line(line)
            if proccessed_line:
                processed_lines.append(proccessed_line)
        formatter_text = '\n'.join(processed_lines)
        return formatter_text

    def _process_line(self, line):
        key, value = line.split(':')
        if self.is_empty_value(value):
            return
        values_joined = ', '.join([f'{v.strip().replace("+", "and")}' for v in value.split(',')])
        processed_line = f"{key}[{values_joined}]"
        return self.normalize_line(processed_line)