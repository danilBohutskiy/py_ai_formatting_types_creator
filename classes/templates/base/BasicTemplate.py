class BasicTemplate:

    TEMPLATE_BODY = []

    def get(self):
        return '\n'.join(self.TEMPLATE_BODY) 