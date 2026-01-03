import re

from typer.testing import CliRunner

from portion.portion import Portion
from tests.utils import strip_ansi


def test_version_command(app: Portion) -> None:
    runner = CliRunner()
    result = runner.invoke(app.cli, ["version"])

    assert result.exit_code == 0
    output = strip_ansi(result.output)
    assert re.match(r"PyPortion: \d+\.\d+\.\d+", output)
