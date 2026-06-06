import pytest
from pydantic import ValidationError

from core.constants import DEFAULT_COLS, DEFAULT_OUTPUT, DEFAULT_ROWS
from core.models import LayoutConfig


def test_layout_config_defaults():
    # itemsのみ指定 → 各フィールドがデフォルト値になる
    config = LayoutConfig(items={"a": "a.png"})
    assert config.cols == DEFAULT_COLS
    assert config.rows == DEFAULT_ROWS
    assert config.out_path == DEFAULT_OUTPUT
    assert config.margin == 36


def test_layout_config_cols_zero_raises():
    # cols=0 → ValidationError
    with pytest.raises(ValidationError):
        LayoutConfig(items={"a": "a.png"}, cols=0)


def test_layout_config_rows_zero_raises():
    # rows=0 → ValidationError
    with pytest.raises(ValidationError):
        LayoutConfig(items={"a": "a.png"}, rows=0)


def test_layout_config_items_empty_raises():
    # items={} → ValidationError
    with pytest.raises(ValidationError):
        LayoutConfig(items={})
