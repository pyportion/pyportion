

class Transformer:

    @classmethod
    def camelcase(cls, text: str) -> str:
        words = text.split()
        return words[0].lower() + ''.join(
            word.capitalize() for word in words[1:])

    @classmethod
    def pascalcase(cls, text: str) -> str:
        return ''.join(word.capitalize() for word in text.split())

    @classmethod
    def snakecase(cls, text: str) -> str:
        return '_'.join(text.lower().split())

    @classmethod
    def kebabcase(cls, text: str) -> str:
        return '-'.join(text.lower().split())

    @classmethod
    def titlecase(cls, text: str) -> str:
        return text.title()

    @classmethod
    def lowercase(cls, text: str) -> str:
        return text.lower()

    @classmethod
    def uppercase(cls, text: str) -> str:
        return text.upper()

    @classmethod
    def transform(cls, text: str, mode: str) -> str:
        func = getattr(cls, mode, None)
        if not func:
            raise ValueError(f"Unknown transform mode: {mode}")
        return func(text)
