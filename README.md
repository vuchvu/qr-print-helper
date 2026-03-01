# qr-print-helper

![GitHub release (latest by date)](https://img.shields.io/github/v/release/vuchvu/qr-print-helper)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/vuchvu/qr-print-helper/deploy.yml)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/vuchvu/qr-print-helper)
![GitHub License](https://img.shields.io/github/license/vuchvu/qr-print-helper)

## ウィンドウで確認しながらの実行方法(GUI版)

### インストーラーを使う方法

> [!NOTE]
> Windows では、署名されていないインストーラーを実行する際にセキュリティ警告が表示されることがあります。

#### インストール

1. [最新リリースページ](https://github.com/vuchvu/qr-print-helper/releases/latest)から `qr-print-helper-vx.x.x-installer.exe` をダウンロードする

2. インストーラーをダブルクリックして実行する

3. 「**WindowsによってPCが保護されました**」と表示されたら「**詳細情報**」をクリックする

    ![インストール手順1](https://github.com/user-attachments/assets/3aa2a423-425c-4c31-bd59-1c605ec31296)

4. 「**実行**」ボタンを押す

    ![インストール手順2](https://github.com/user-attachments/assets/c04966a5-cc20-4c04-b548-b208d917b9e9)

5. 画面に従ってインストールを進める

#### 起動

1. スタートメニューまたはデスクトップのショートカットからアプリを起動する

2. GUI画面が表示される

    ![画面表示](https://github.com/user-attachments/assets/b401317f-6e06-4766-b7ff-3f5cfc1588e3)

    `images` フォルダにPNG形式のQRコードを保存して、「**PDF生成**」ボタンを押すとPDFが生成される

    ファイル名がQRコードの上に表示されます。注文番号にするのがオススメです

#### 終了時

ウィンドウを閉じるとアプリは終了します。

### zipファイルを使う方法

> [!NOTE]
> Windows では、署名されていないバイナリを実行する際にセキュリティ警告が表示されることがあります。初回のみ「**詳細情報**」→「**実行**」で起動できます。

#### 初回起動

1. 解凍したzipから出てきた実行ファイルをダブルクリックする

2. 「**WindowsによってPCが保護されました**」と表示されたら「**詳細情報**」→「**実行**」をクリックする

3. GUI画面が表示される

#### 2回目以降の起動

1. 実行ファイルをダブルクリックする

2. GUI画面が表示される

#### 終了時

ウィンドウを閉じるとアプリは終了します。

### macOS版の実行方法

> [!NOTE]
> macOS では、署名されていないバイナリを実行する際にセキュリティ警告が表示されます。

#### 初回起動

1. 解凍したzipから出てきたバイナリをダブルクリックする

    ![バイナリ](https://github.com/user-attachments/assets/5f94bae5-491d-45f7-ace5-e21de2e9ff16)

2. セキュリティ警告が表示されるので「**完了**」をクリックして閉じる

    ![セキュリティ警告1](https://github.com/user-attachments/assets/60051822-b87f-4f30-b25c-b879a7b240e5)

3. 「**システム設定**」の「**プライバシーとセキュリティ**」を開いて下へスクロールし、「**このまま開く**」をクリックする

    ![プライバシーとセキュリティ](https://github.com/user-attachments/assets/e8816e7f-7ff6-498a-b967-d471750a21aa)

4. 再度セキュリティ警告が表示されるので「**このまま開く**」をクリックする

    ![セキュリティ警告2](https://github.com/user-attachments/assets/1b7f148a-2a13-4c9f-a52b-ca26f04e9348)

5. 認証を求められるので実施する

    ![認証](https://github.com/user-attachments/assets/aa47b377-f386-4f18-a9a0-9b4480e16da3)

6. ターミナル.app が開きプログラムが起動する

    ![ターミナル](https://github.com/user-attachments/assets/cabe858e-2b77-4e11-82f0-6344f589f822)

7. フォルダへのアクセス権を求められたら許可する

    ![アクセス権](https://github.com/user-attachments/assets/ce581454-9067-41a5-885a-75087bea0537)

8. ターミナルとは別ウィンドウでGUI画面が表示される。このとき `~/images` フォルダが自動的に作成される

    ![GUI画面](https://github.com/user-attachments/assets/944d852f-ec81-4247-8c25-05782ab955ad)

#### 2回目以降の起動

1. 解凍したzipから出てきたバイナリをダブルクリックする
2. ターミナル.app が開きプログラムが起動する
3. GUI画面が表示される

#### 終了時

ウィンドウを閉じるとアプリは終了しますが、起動時に開いたターミナル.app はそのまま残ります。不要であれば手動で閉じてください。

![終了後のターミナル](https://github.com/user-attachments/assets/fc534e8b-e508-46c5-9ab0-2693dd131e5b)

## CLI版の実行方法

### uvを使う方法

git cloneが不要です！

1. uvをインストールする

    Windowsの場合

    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

    macOSまたはLinuxの場合

    ```sh
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

2. png形式のQRコードを`images`ディレクトリに保存する

    ファイル名がQRコードの上に表示されます。注文番号にするのがオススメです

    Windowsの場合

    ```powershell
    mkdir images
    cp \path\to\qr-image.png .\images
    ```

    macOSまたはLinuxの場合

    ```sh
    mkdir images
    cp /path/to/qr-image.png ./images
    ```

    デフォルトのディレクトリ名(`images`)はオプションで変更できます

3. コマンドを実行する

    ```sh
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

    ```sh
    uv tool install qr-print-helper@git+https://github.com/vuchvu/qr-print-helper
    ```

### pythonを使う場合

1. リポジトリをクローンする

    ```sh
    git clone https://github.com/vuchvu/qr-print-helper
    ```

2. pythonをインストールする

3. 仮想環境作成・依存関係のインストールをする

    Windowsの場合

    ```powershell
    python -m venv .venv
    .\venv\Scripts\activate.ps1
    pip install -r requirements.txt
    ```

    macOSまたはLinuxの場合

    ```sh
    python -m venv .venv
    ./venv/bin/activate
    pip install -r requirements.txt
    ```

4. png形式のQRコードを`images`ディレクトリに保存する

    ファイル名がqrコードの上に表示されます。注文番号にするのがオススメです

    デフォルトのディレクトリ名(`images`)はオプションで変更できます

5. コマンドを実行する

    オプション等はuvを使って実行する場合と同様です

    ```sh
    python cli.py create
    ```

## 貢献者

協力していただきありがとうございます！

[![contrib.rocks](https://contrib.rocks/image?repo=vuchvu/qr-print-helper)](https://github.com/vuchvu/qr-print-helper/graphs/contributors)

Made with [contrib.rocks](https://contrib.rocks).
