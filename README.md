# qr-print-helper
## ウィンドウで確認しながらの実行方法(GUI版)

まだmac未対応です…すみません。

### インストーラーを使う方法

1. インストーラーのダウンロード

[最新リリースページ](https://github.com/vuchvu/qr-print-helper/releases/latest)から、`qr-print-helper-v0.2.2-installer.exe`をダウンロードする

2. インストールの実行

インストーラーを実行する

「**WindowsによってPCが保護されました**」と表示されたら、

![インストール手順1](https://github.com/user-attachments/assets/3aa2a423-425c-4c31-bd59-1c605ec3129)

「詳細情報」をクリックして「**実行**」ボタンを押す

![インストール手順2](https://github.com/user-attachments/assets/c04966a5-cc20-4c04-b548-b208d917b9e9)

この後は画面に従ってインストールを進める

3. PDFの生成

ソフトを実行すると、こんな画面が出る

![画面表示](https://github.com/user-attachments/assets/b401317f-6e06-4766-b7ff-3f5cfc1588e3)

`images`フォルダにPNG形式のQRコードを保存して、「**PDF生成**」ボタンを押すとPDFが生成される！


## CLI版の実行方法
### uvを使う方法

git cloneが不要です！

1. uvをインストールする

Windowsの場合
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

macOSまたはLinuxの場合
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. png形式のQRコードを`images`ディレクトリに保存する

ファイル名がQRコードの上に表示されます。注文番号にするのがオススメです

Windowsの場合
```
mkdir images
cp \path\to\qr-image.png .\images
```

macOSまたはLinuxの場合
```
mkdir images
cp /path/to/qr-image.png ./images
```

デフォルトのディレクトリ名(`images`)はオプションで変更できます

4. コマンドを実行する
```
uvx qr-print-helper@git+https://github.com/vuchvu/qr-print-helper create
```

デフォルト設定は以下のオプションで上書きできます

|オプション |内容                        |デフォルト  |
|-----------|----------------------------|------------|
|--input-dir|QR画像を保存するディレクトリ|`images`    |
|--output   |出力PDFファイル名           |`labels.pdf`|
|--col      |1ページあたりの列数         |2           |
|--row      |1ページあたりの行数         |3           |

何度も実行する場合はツールとしてインストールすると便利です
```
uv tool install qr-print-helper@git+https://github.com/vuchvu/qr-print-helper
```

### pythonを使う場合

1. リポジトリをクローンする
```
git clone https://github.com/vuchvu/qr-print-helper
```

2. pythonをインストールする

3. 仮想環境作成・依存関係のインストールをする

Windowsの場合
```
python -m venv .venv
.\venv\Scripts\activate.ps1
pip install -r requirements.txt
```

macOSまたはLinuxの場合
```
python -m venv .venv
.\venv\bin\activate
pip install -r requirements.txt
```

4. png形式のQRコードを`images`ディレクトリに保存する

ファイル名がqrコードの上に表示されます。注文番号にするのがオススメです

デフォルトのディレクトリ名(`images`)はオプションで変更できます

5. コマンドを実行する
オプション等はuvを使って実行する場合と同様です
```
python cli.py create
```

