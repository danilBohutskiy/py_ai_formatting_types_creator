from ..mappings.TemplateMapping import TemplateMapping

class TemplateFactory:
    def create(template):
        template_class = TemplateMapping.TEMPLATE_MAPPING.get(template)
        if template_class is not None:
            return template_class()
        else:
            return None