from .base.BasicTemplate import BasicTemplate

class SimpleTemplate(BasicTemplate):
    
    TEMPLATE_BODY = [
            "Nickname: ",
            "Species: ",
            "Age: ",
            "Features: ",
            "Body: ",
            "Mind: ",
            "Description: ",
        ]
    
    def get(self):
        return '\n'.join(self.TEMPLATE_BODY) 
