import pytest

from cli import build_parser
from core.constants import DEFAULT_COLS, DEFAULT_INPUT_DIR, DEFAULT_OUTPUT, DEFAULT_ROWS


def test_parser_defaults():
    # オプション未指定 → 各引数がデフォルト値になる
    parser = build_parser()
    args = parser.parse_args(["create"])
    assert args.input_dir == DEFAULT_INPUT_DIR
    assert args.output == DEFAULT_OUTPUT
    assert args.col == DEFAULT_COLS
    assert args.row == DEFAULT_ROWS


def test_parser_custom_values():
    # 全オプション指定 → 指定した値が反映される
    parser = build_parser()
    args = parser.parse_args(
        ["create", "--input-dir", "qr", "--output", "out.pdf", "--col", "3", "--row", "4"]
    )
    assert args.input_dir == "qr"
    assert args.output == "out.pdf"
    assert args.col == 3
    assert args.row == 4


def test_parser_no_command_raises():
    # サブコマンド未指定 → SystemExit
    parser = build_parser()
    with pytest.raises(SystemExit):
        parser.parse_args([])
