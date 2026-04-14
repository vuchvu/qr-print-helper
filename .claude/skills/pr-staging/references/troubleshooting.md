# トラブルシューティング

## gh が未認証の場合

```bash
gh auth login
```

## developブランチへの同一PRが既に存在する場合

```bash
gh pr list --base develop --head $(git branch --show-current)
```

既存PRのURLをユーザーに伝えて、そちらを更新するか確認する。

## squash merge 後にブランチ削除が失敗した場合

```bash
git branch -d <branch-name>
git push origin --delete <branch-name>
```

## origin/develop が存在しない場合

```bash
git fetch origin develop
```

fetchしてから再試行する。
