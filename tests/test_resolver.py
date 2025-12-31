from portion.utils import Resolver


def test_resolve() -> None:
    memory = {
        "VAR1": "value1",
        "VAR2": "value2",
    }
    path = ["$VAR1", "static", "$VAR2", "$UNKNOWN"]
    expected = ["value1", "static", "value2", "$UNKNOWN"]
    result = Resolver.resolve(memory, path)
    assert result == expected
