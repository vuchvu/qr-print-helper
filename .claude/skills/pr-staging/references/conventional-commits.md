# Conventional Commits 形式

## prefix一覧

| prefix      | 用途             |
| ----------- | ---------------- |
| `feat:`     | 新機能           |
| `fix:`      | バグ修正         |
| `docs:`     | ドキュメント     |
| `refactor:` | リファクタリング |
| `chore:`    | その他の変更     |

スコープがある場合は `feat(scope): message` の形式。

## 修正方法

直前のコミットを修正：

```bash
git commit --amend
```

複数コミットをまとめて修正：

```bash
git rebase -i origin/develop
```
