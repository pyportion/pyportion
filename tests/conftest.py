from pathlib import PosixPath

import pytest

from portion.portion import Portion
from portion.portion import load_handlers


@pytest.fixture
def app() -> Portion:
    app = Portion()
    load_handlers(app.cli)
    return app


@pytest.fixture
def mock_user_data_dir(tmp_path: PosixPath,
                       monkeypatch: pytest.MonkeyPatch) -> PosixPath:
    monkeypatch.setattr("portion.core.template_manager.user_data_dir",
                        lambda: tmp_path)
    return tmp_path
