import re


def strip_ansi(text: str) -> str:
    ansi_escape = re.compile(r'(\x1b\[[0-9;]*m)|(\n)')
    return ansi_escape.sub('', text)
