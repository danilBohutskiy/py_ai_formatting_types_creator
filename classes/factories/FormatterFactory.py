from ..formatters.mappings.FormatterMapping import FormatterMapping

class FormatterFactory:
    def create(format_type, text):
        formatter_class = FormatterMapping.FORMATTER_MAPPING.get(format_type)
        if formatter_class:
            return formatter_class(text)
        else:
            raise ValueError("Unknown format type!")