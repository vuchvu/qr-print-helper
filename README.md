# qr-print-helper
## CLI版の実行方法
### 1. uv(またはpython)のインストール
Windows
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

macOSまたはLinux
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. 仮想環境作成・依存関係のインストール
uv
```
uv sync
```

python
```
python -m venv .venv
pip install -r requirements.txt
```

### 3. 仮想環境有効化
Windows
```
source .\.venv\Scripts\activate.ps1
```

macOSまたはLinux
```
source ./.venv/bin/activate
```

### 4. png形式のQRコードをimages/ディレクトリに保存
ファイル名がQRコードの上に表示されます。注文番号にするのがオススメです

ディレクトリは変更できるようにします(まだ)

### 5. コマンド実行
コマンドを実行することでカレントディレクトリに `labels.pdf`が出力されます。
```
python core\layout.py
```

PDFのファイル名は変更できるようにします(まだ)
