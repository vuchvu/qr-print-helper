# AGENTS.md

このプロジェクトでAIエージェントが作業する際のガイドラインです。

## ブランチ戦略

```
feature/xxx → develop → main
```

- 機能追加・修正は `feature/xxx` ブランチで作業し、`develop` へPRを出す
- `develop` → `main` へのマージでリリースが行われる

## PRラベル

| ラベル | 用途 |
|---|---|
| `major` / `minor` / `patch` | バージョンバンプの種別を指定（develop→main PRに付ける） |

バージョンバンプラベルがないと `tag.yml` がスキップされ、リリースされないので必ず付けること。

## コミットメッセージ

[Conventional Commits](https://www.conventionalcommits.org/) に従う。

```
feat: 新機能の説明
fix: バグ修正の説明
docs: ドキュメントの説明
ci: CI/CD の変更
refactor: リファクタリング
chore: その他の変更
```

git-cliff がコミットメッセージを元にリリースノートを自動生成する。

## リリースフロー

1. develop→main の PR に `major`/`minor`/`patch` ラベルを付けてマージ
2. `tag.yml` が自動でバージョンバンプ・コミット・タグ付け・プッシュを行う
3. タグプッシュをトリガーに `deploy.yml` がビルド・リリースを行う

**タグは手動で作成しない**（複数タグの同時プッシュによりワークフローが発火しない場合がある）。

## develop→main のマージ方法

`Merge commit` または `Rebase and merge` を使う。`Squash and merge` にすると個別のコミットメッセージが失われ、git-cliff のchangelogが正しく生成されない。
