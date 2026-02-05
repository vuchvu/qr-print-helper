import argparse
import sys
from pathlib import Path

from core.layout import create_layout_pdf


def build_parser():
    common_parser = argparse.ArgumentParser(add_help=False)
    common_parser.add_argument("--input-dir", default="images", help="QR画像のディレクトリ")
    common_parser.add_argument("--output", default="labels.pdf", help="出力PDFファイル名")
    common_parser.add_argument("--col", type=int, default=2, help="1ページあたりの列数")
    common_parser.add_argument("--row", type=int, default=3, help="1ページあたりの行数")

    parser = argparse.ArgumentParser(
        description="QRコード画像を含むPDFを生成します。",
        parents=[common_parser],
    )

    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser(
        "create",
        help="ラベルPDFを生成します。",
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
    mapping = {image.stem: str(image) for image in sorted(input_dir.glob("*.png"))}
    if len(mapping) <= 0:
        raise FileNotFoundError(f"{input_dir}の中にpngファイルがありません")

    create_layout_pdf(
        mapping,
        out_path=args.output,
        cols=args.col,
        rows=args.row,
    )


if __name__ == "__main__":
    main()
