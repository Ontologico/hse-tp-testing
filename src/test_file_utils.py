import shutil
from pathlib import Path

import pytest

from src.file_utils import create_file, read_file


@pytest.fixture
def temp_dir():
    p = Path("temp")
    p.mkdir(exist_ok=True)
    # time.sleep(10)
    yield p
    shutil.rmtree(p)

    # Ещё решение:
    # with tempfile.TemporaryDirectory() as tmpdir:
    #     yield Path(tmpdir)


def test_create_and_read_file(temp_dir):
    # tmp_path
    content = "Hello, pytest!"
    path = temp_dir / "test.txt"

    create_file(path, content)

    assert path.exists()
    assert read_file(path) == content
