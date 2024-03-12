from ..WppFormatter import WppFormatter
from ..BoostyleFormatter import BoostyleFormatter
from ..BracketedListFormatter import BracketedListFormatter

class FormatterMapping:
    FORMATTER_MAPPING = {
        "W++ Format": WppFormatter,
        "Boostyle": BoostyleFormatter,
        "Bracked List": BracketedListFormatter
    }

    @staticmethod
    def get_format_types():
        return list(FormatterMapping.FORMATTER_MAPPING.keys())
