# 貢献ガイド

qr-print-helper への貢献に興味を持っていただきありがとうございます！

## Issue

バグ報告・機能要望は [Issues](https://github.com/vuchvu/qr-print-helper/issues) からお願いします。テンプレートに沿って記入してください。

大きな変更（新機能の追加、既存動作の変更など）は、実装を始める前に Issue で相談してもらえると手戻りを防げます。

## 開発環境のセットアップ

[uv](https://docs.astral.sh/uv/) を使います。

```sh
git clone https://github.com/vuchvu/qr-print-helper
cd qr-print-helper
uv sync
```

### テスト

```sh
uv run pytest
```

### Lint

```sh
uv run ruff check .
```

## Pull Request

### ブランチ

- ベースブランチは **`develop`** です（`main` ではありません）
- `develop` から作業ブランチを作成し、変更内容に合わせたプレフィックスを付けてください
  - 機能追加: `feat/xxx`
  - バグ修正: `fix/xxx`
  - ドキュメント: `docs/xxx`

### コミットメッセージ

[Conventional Commits](https://www.conventionalcommits.org/ja/) に従い、日本語で記述してください。

```
feat: 新機能の説明
fix: バグ修正の説明
docs: ドキュメントの説明
refactor: リファクタリング
chore: その他の変更
```

コミットメッセージは git-cliff によるリリースノートの自動生成に使われます。

### PRタイトル

PRタイトルも Conventional Commits 形式でお願いします。`develop` へは squash merge されるため、PRタイトルがコミットメッセージとなり、そのままリリースノートに掲載されます。

### 送る前のチェック

CI では自動テストが実行されないため、ローカルで以下が通ることを確認してください。

```sh
uv run pytest
uv run ruff check .
```

### ラベルについて

`major` / `minor` / `patch` ラベルは develop→main のリリースPR専用です。コントリビュータが付ける必要はありません。

## リリースフロー（参考）

リリースはメンテナが行います。

1. develop→main の PR にバージョンラベル（`major` / `minor` / `patch`）を付けてマージ
2. GitHub Actions がバージョンバンプ・タグ付け・ビルド・リリースを自動で実行
