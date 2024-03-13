from .base.BaseFormatter import BaseFormatter

class WppFormatter(BaseFormatter):
    def format(self, text):
        processed_lines = [self._process_line(line) for line in text.splitlines() if line.strip()]
        formatter_text = '[{' + '\n'.join(processed_lines) + '}]'
        return formatter_text

    def _process_line(self, line):
        key, value = line.split(':')
        values_joined = ', '.join([f'"{v.strip()}"' for v in value.split(',')])
        processed_line = f"{key}({values_joined})"
        return processed_line