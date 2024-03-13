from ..formatters.mappings.FormatterMapping import FormatterMapping

class FormatterFactory:
    def create(format_type):
        formatter_class = FormatterMapping.FORMATTER_MAPPING.get(format_type)
        if formatter_class:
            return formatter_class()
        else:
            raise ValueError("Unknown format type!")