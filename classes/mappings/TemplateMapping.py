from ..templates.SimpleTemplate import SimpleTemplate

class TemplateMapping:
    TEMPLATE_MAPPING = {
        "None": None,
        "Simple": SimpleTemplate,
    }

    @staticmethod
    def get_template_types():
        return list(TemplateMapping.TEMPLATE_MAPPING.keys())
