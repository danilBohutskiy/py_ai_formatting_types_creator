from .base.BaseFormatter import BaseFormatter

class BoostyleFormatter(BaseFormatter):
    def format(self, character_name, character_description_text):
        processed_lines = []

        for line in character_description_text.splitlines():
            proccessed_line = self._process_line(line)
            if proccessed_line:
                processed_lines.append(proccessed_line)

        processed_lines.sort()
        
        processed_lines = '+'.join(processed_lines)
        formatter_text = f'{character_name}[{processed_lines}]'
        return formatter_text

    def _process_line(self, line):
        key, value = self.split_line(line)
        if not key or self.is_empty_value(value):
            return
        
        values_joined = '+'.join([f'"{v.strip()}"' for v in value.split(',')])
        processed_line = f"{values_joined}"
        return self.normalize_line(processed_line)