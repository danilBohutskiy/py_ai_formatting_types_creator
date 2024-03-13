from .base.BaseFormatter import BaseFormatter

class BoostyleFormatter(BaseFormatter):
    def format(self, charachter_name, charachter_description_text):
        processed_lines = [self._process_line(line) for line in charachter_description_text.splitlines() if line.strip()]
        processed_lines = '+'.join(processed_lines)
        formatter_text = f'{charachter_name}[{processed_lines}]'
        return formatter_text

    def _process_line(self, line):
        key, value = line.split(':')
        values_joined = '+'.join([f'"{v.strip()}"' for v in value.split(',')])
        processed_line = f"{values_joined}"
        return self.normalize_line(processed_line)