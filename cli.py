import argparse
import sys
from pathlib import Path

from core.constants import (
    DEFAULT_COLS,
    DEFAULT_INPUT_DIR,
    DEFAULT_OUTPUT,
    DEFAULT_ROWS,
    DESCRIPTION,
    ERR_NO_IMAGES,
    IMAGE_GLOB,
    LABEL_CREATE,
    LABEL_COLS,
    LABEL_INPUT_DIR,
    LABEL_OUTPUT,
    LABEL_ROWS,
)
from core.layout import create_layout_pdf


def build_parser():
    common_parser = argparse.ArgumentParser(add_help=False)
    common_parser.add_argument(
        "--input-dir", default=DEFAULT_INPUT_DIR, help=LABEL_INPUT_DIR,
    )
    common_parser.add_argument(
        "--output", default=DEFAULT_OUTPUT, help=LABEL_OUTPUT,
    )
    common_parser.add_argument(
        "--col", type=int, default=DEFAULT_COLS, help=f"1ページあたりの{LABEL_COLS}",
    )
    common_parser.add_argument(
        "--row", type=int, default=DEFAULT_ROWS, help=f"1ページあたりの{LABEL_ROWS}",
    )

    parser = argparse.ArgumentParser(
        description=DESCRIPTION,
        parents=[common_parser],
    )

    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser(
        "create",
        help=LABEL_CREATE,
        parents=[common_parser],
    )

    return parser


def main():
    parser = build_parser()
    if len(sys.argv) == 1:
        parser.print_help()
        return

    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    mapping = {image.stem: str(image) for image in sorted(input_dir.glob(IMAGE_GLOB))}
    if len(mapping) <= 0:
        raise FileNotFoundError(ERR_NO_IMAGES.format(input_dir=input_dir))

    create_layout_pdf(
        mapping,
        out_path=args.output,
        cols=args.col,
        rows=args.row,
    )


if __name__ == "__main__":
    main()
