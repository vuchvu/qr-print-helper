# トラブルシューティング

## jq が未インストールの場合

`jq` コマンドが使えない場合は、以下で代替する：

```bash
gh pr list --base develop --state merged --json title,mergedAt
```

出力されたJSONを手動で確認してPR本文を作成する。

## リポジトリ名の確認

```bash
gh repo view --json nameWithOwner
```

## develop→main の既存PRが既にある場合

```bash
gh pr list --base main --head develop
```

既存PRのURLをユーザーに伝えて、そちらを更新するか確認する。
