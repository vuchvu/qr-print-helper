import subprocess
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

from core.constants import (
    APP_NAME,
    DEFAULT_COLS,
    DEFAULT_INPUT_DIR,
    DEFAULT_OUTPUT,
    DEFAULT_ROWS,
    ERR_DIR_NOT_FOUND,
    ERR_NO_IMAGES,
    ERR_NO_OUTPUT,
    IMAGE_GLOB,
    LABEL_COLS,
    LABEL_INPUT_DIR,
    LABEL_OUTPUT,
    LABEL_ROWS,
)
from core.layout import create_layout_pdf


class App:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title(APP_NAME)
        self.root.resizable(False, False)
        self._set_icon()

        self._ensure_images_dir()
        self._build_widgets()

    def _set_icon(self):
        ico_path = Path(__file__).parent / "assets" / "icon.ico"
        png_path = Path(__file__).parent / "assets" / "icon.png"

        if sys.platform == "win32" and ico_path.exists():
            self.root.iconbitmap(default=str(ico_path))
        elif png_path.exists():
            icon = tk.PhotoImage(file=str(png_path))
            self.root.iconphoto(True, icon)

    def _ensure_images_dir(self):
        images_dir = Path(DEFAULT_INPUT_DIR).resolve()
        if not images_dir.exists():
            images_dir.mkdir()

    def _build_widgets(self):
        # --- 入力ディレクトリ ---
        tk.Label(self.root, text=f"{LABEL_INPUT_DIR}:").grid(
            row=0, column=0, sticky="e", padx=(10, 4), pady=(10, 4)
        )
        self.input_dir_var = tk.StringVar(
            value=str(Path(DEFAULT_INPUT_DIR).resolve())
        )
        self.input_dir_entry = tk.Entry(
            self.root, textvariable=self.input_dir_var, width=40
        )
        self.input_dir_entry.grid(row=0, column=1, padx=4, pady=(10, 4))
        tk.Button(self.root, text="参照", command=self._browse_input_dir).grid(
            row=0, column=2, padx=(4, 10), pady=(10, 4)
        )

        # ディレクトリ変更時にファイル一覧を更新
        self.input_dir_var.trace_add("write", lambda *_: self._refresh_file_list())

        # --- 出力PDFファイル名 ---
        tk.Label(self.root, text=f"{LABEL_OUTPUT}:").grid(
            row=1, column=0, sticky="e", padx=(10, 4), pady=4
        )
        self.output_var = tk.StringVar(
            value=str(Path(DEFAULT_OUTPUT).resolve())
        )
        tk.Entry(self.root, textvariable=self.output_var, width=40).grid(
            row=1, column=1, padx=4, pady=4
        )
        tk.Button(self.root, text="参照", command=self._browse_output).grid(
            row=1, column=2, padx=(4, 10), pady=4
        )

        # --- 列数 ---
        tk.Label(self.root, text=f"{LABEL_COLS}:").grid(
            row=2, column=0, sticky="e", padx=(10, 4), pady=4
        )
        self.col_var = tk.IntVar(value=DEFAULT_COLS)
        tk.Spinbox(
            self.root, from_=1, to=10, textvariable=self.col_var, width=5
        ).grid(row=2, column=1, sticky="w", padx=4, pady=4)

        # --- 行数 ---
        tk.Label(self.root, text=f"{LABEL_ROWS}:").grid(
            row=3, column=0, sticky="e", padx=(10, 4), pady=4
        )
        self.row_var = tk.IntVar(value=DEFAULT_ROWS)
        tk.Spinbox(
            self.root, from_=1, to=10, textvariable=self.row_var, width=5
        ).grid(row=3, column=1, sticky="w", padx=4, pady=4)

        # --- 画像一覧 ---
        self.file_count_var = tk.StringVar(value="画像一覧: (0件)")
        tk.Label(self.root, textvariable=self.file_count_var).grid(
            row=4, column=0, columnspan=3, sticky="w", padx=10, pady=(10, 2)
        )

        list_frame = tk.Frame(self.root)
        list_frame.grid(row=5, column=0, columnspan=3, padx=10, pady=(0, 4))

        self.file_listbox = tk.Listbox(list_frame, width=50, height=8)
        scrollbar = tk.Scrollbar(
            list_frame, orient="vertical", command=self.file_listbox.yview
        )
        self.file_listbox.configure(yscrollcommand=scrollbar.set)
        self.file_listbox.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # --- PDF生成ボタン ---
        tk.Button(
            self.root, text="PDF生成", command=self._generate_pdf, width=20
        ).grid(row=6, column=0, columnspan=3, pady=10)

        # --- ステータス ---
        self.status_var = tk.StringVar(value="")
        tk.Label(self.root, textvariable=self.status_var).grid(
            row=7, column=0, columnspan=3, padx=10, pady=(0, 10)
        )

        # 初期ファイル一覧
        self._refresh_file_list()

    def _browse_input_dir(self):
        current = Path(self.input_dir_var.get())
        initial = str(current) if current.is_dir() else str(Path.cwd())
        path = filedialog.askdirectory(initialdir=initial)
        if path:
            self.input_dir_var.set(path)

    def _browse_output(self):
        current = Path(self.output_var.get())
        parent = current.parent
        initial = str(parent) if parent.is_dir() else str(Path.cwd())
        path = filedialog.asksaveasfilename(
            initialdir=initial,
            initialfile=current.name,
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
        )
        if path:
            self.output_var.set(path)

    def _refresh_file_list(self):
        self.file_listbox.delete(0, tk.END)
        input_dir = Path(self.input_dir_var.get())
        if input_dir.is_dir():
            files = sorted(input_dir.glob(IMAGE_GLOB))
            for f in files:
                self.file_listbox.insert(tk.END, f.name)
            self.file_count_var.set(f"画像一覧: ({len(files)}件)")
        else:
            self.file_count_var.set("画像一覧: (0件)")

    def _generate_pdf(self):
        input_dir = Path(self.input_dir_var.get())
        output = self.output_var.get().strip()

        if not input_dir.is_dir():
            messagebox.showerror("エラー", ERR_DIR_NOT_FOUND.format(input_dir=input_dir))
            return

        mapping = {
            image.stem: str(image) for image in sorted(input_dir.glob(IMAGE_GLOB))
        }
        if not mapping:
            messagebox.showerror("エラー", ERR_NO_IMAGES.format(input_dir=input_dir))
            return

        if not output:
            messagebox.showerror("エラー", ERR_NO_OUTPUT)
            return

        output_path = Path(output).resolve()

        try:
            create_layout_pdf(
                mapping,
                out_path=str(output_path),
                cols=self.col_var.get(),
                rows=self.row_var.get(),
            )
            self.status_var.set(f"完了しました: {output_path}")
            self._open_file(output_path)
        except Exception as e:
            messagebox.showerror("エラー", str(e))
            self.status_var.set("エラーが発生しました")

    @staticmethod
    def _open_file(path: Path):
        devnull = {"stdout": subprocess.DEVNULL, "stderr": subprocess.DEVNULL}
        if sys.platform == "win32":
            subprocess.Popen(["start", "", str(path)], shell=True, **devnull)
        elif sys.platform == "darwin":
            subprocess.Popen(["open", str(path)], **devnull)
        else:
            subprocess.Popen(["xdg-open", str(path)], **devnull)


def main():
    root = tk.Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
