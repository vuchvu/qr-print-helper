from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from PIL import Image
import math
import os

from core.constants import ERR_IMAGE_NOT_FOUND, ERR_PDF_GENERATION
from core.models import LayoutConfig


def create_layout_pdf(config: LayoutConfig):
    items = config.items
    out_path = config.out_path
    cols = config.cols
    rows = config.rows
    margin = config.margin

    pw, ph = A4
    c = canvas.Canvas(out_path, pagesize=A4)
    cell_w = (pw - 2*margin) / cols
    cell_h = (ph - 2*margin) / rows

    pad = 8  # 内部余白
    text_height = 18  # キー表示用高さ

    positions = []
    for r in range(rows):
        for col in range(cols):
            x = margin + col * cell_w
            y = ph - margin - (r+1) * cell_h
            positions.append((x, y, cell_w, cell_h))

    keys = list(items.keys())
    total = len(keys)
    pages = math.ceil(total / (cols*rows))

    idx = 0
    for p in range(pages):
        for pos_idx in range(cols*rows):
            if idx >= total:
                break
            key = keys[idx]
            img_path = items[key]
            x, y, w, h = positions[pos_idx]

            # 枠描画
            c.rect(x, y, w, h, stroke=1, fill=0)

            # キーを上部中央に描画
            tx = x + w/2
            ty = y + h - pad - 4
            c.setFont("Helvetica", 12)
            c.drawCentredString(tx, ty, str(key))

            # 画像配置領域
            img_x = x + pad
            img_y = y + pad
            img_w = w - 2*pad
            img_h = h - text_height - 3*pad

            # 画像読み込みとアスペクト比維持でフィットしたサイズで描画
            if not os.path.exists(img_path):
                raise FileNotFoundError(ERR_IMAGE_NOT_FOUND.format(img_path=img_path))
            try:
                with Image.open(img_path) as im:
                    iw, ih = im.size
                    scale = min(img_w / iw, img_h / ih)
                    draw_w = iw * scale
                    draw_h = ih * scale
                    draw_x = img_x + (img_w - draw_w)/2
                    draw_y = img_y + (img_h - draw_h)/2
                    img_reader = ImageReader(img_path)
                    c.drawImage(img_reader, draw_x, draw_y, draw_w, draw_h, preserveAspectRatio=True)
            except Exception:
                raise RuntimeError(ERR_PDF_GENERATION.format(filename=os.path.basename(img_path)))

            idx += 1

        c.showPage()
    c.save()

