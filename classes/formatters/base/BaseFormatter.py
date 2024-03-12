class BaseFormatter:
    def __init__(self, text) -> None:
        self.text = text
        pass
    
    @staticmethod
    def format(self):
        raise NotImplementedError("The method must be implemented in subclasses!")