from portion.utils import Transformer


def test_camelcase():
    assert Transformer.camelcase("hello world") == "helloWorld"
    assert Transformer.camelcase("Hello World") == "helloWorld"
    assert Transformer.camelcase("multiple words here") == "multipleWordsHere"


def test_pascalcase():
    assert Transformer.pascalcase("hello world") == "HelloWorld"
    assert Transformer.pascalcase("Hello World") == "HelloWorld"
    assert Transformer.pascalcase("multiple words here") == "MultipleWordsHere"


def test_snakecase():
    assert Transformer.snakecase("hello world") == "hello_world"
    assert Transformer.snakecase("Hello World") == "hello_world"
    assert Transformer.snakecase("multiple words") == "multiple_words"


def test_kebabcase():
    assert Transformer.kebabcase("hello world") == "hello-world"
    assert Transformer.kebabcase("Hello World") == "hello-world"
    assert Transformer.kebabcase("multiple words") == "multiple-words"


def test_titlecase():
    assert Transformer.titlecase("hello world") == "Hello World"
    assert Transformer.titlecase("Hello World") == "Hello World"
    assert Transformer.titlecase("multiple words") == "Multiple Words"


def test_lowercase():
    assert Transformer.lowercase("Hello World") == "hello world"
    assert Transformer.lowercase("MULTIPLE Words") == "multiple words"


def test_uppercase():
    assert Transformer.uppercase("hello world") == "HELLO WORLD"
    assert Transformer.uppercase("Multiple Words") == "MULTIPLE WORDS"


def test_transform():
    assert Transformer.transform("hello world", "camelcase") == "helloWorld"
    assert Transformer.transform("hello world", "pascalcase") == "HelloWorld"
    assert Transformer.transform("hello world", "snakecase") == "hello_world"
    assert Transformer.transform("hello world", "kebabcase") == "hello-world"
    assert Transformer.transform("hello world", "titlecase") == "Hello World"
    assert Transformer.transform("Hello World", "lowercase") == "hello world"
    assert Transformer.transform("hello world", "uppercase") == "HELLO WORLD"

    try:
        Transformer.transform("hello world", "unknowncase")
    except ValueError as e:
        assert str(e) == "Unknown transform mode: unknowncase"
