from .base.BaseFormatter import BaseFormatter

class BracketedListFormatter(BaseFormatter):
    def format(self, charachter_name, charachter_description_text):
        charachter_name_description = f'Name: {charachter_name}\n {charachter_description_text}'
        processed_lines = [self._process_line(line) for line in charachter_name_description.splitlines() if line.strip()]
        formatter_text = '\n'.join(processed_lines)
        return formatter_text

    def _process_line(self, line):
        key, value = line.split(':')
        values_joined = ', '.join([f'{v.strip().replace("+", "and")}' for v in value.split(',')])
        processed_line = f"{key}[{values_joined}]"
        return self.normalize_line(processed_line)