import pytest
from PIL import Image

from core.layout import create_layout_pdf
from core.models import LayoutConfig


def test_create_layout_pdf_creates_file(tmp_path):
    # 有効な画像1枚 → PDFファイルが生成される
    img = tmp_path / "test.png"
    Image.new("RGB", (100, 100)).save(img)
    out = tmp_path / "output.pdf"
    create_layout_pdf(LayoutConfig(items={"test": str(img)}, out_path=str(out)))
    assert out.exists()


def test_create_layout_pdf_multiple_pages(tmp_path):
    # 2cols×3rows=6件/ページで7件 → 2ページ分のPDFが生成される
    items = {}
    for i in range(7):
        img = tmp_path / f"{i}.png"
        Image.new("RGB", (100, 100)).save(img)
        items[str(i)] = str(img)
    out = tmp_path / "output.pdf"
    create_layout_pdf(LayoutConfig(items=items, out_path=str(out), cols=2, rows=3))
    assert out.exists()


def test_create_layout_pdf_missing_image_raises(tmp_path):
    # itemsに存在しないパスを指定 → FileNotFoundError
    out = tmp_path / "output.pdf"
    with pytest.raises(FileNotFoundError):
        create_layout_pdf(LayoutConfig(items={"missing": str(tmp_path / "none.png")}, out_path=str(out)))
