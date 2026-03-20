---
name: pr-release
description: 「本リリース」と言われたら使うスキル。developブランチからmainブランチへのPRを作成する。
---

# PR Release Skill

developブランチ → mainブランチへのPR作成を行う。マージは人間が行う。

---

### Step 1: 事前確認

```bash
gh auth status

# develop→main のPRが既に存在する場合はエラーになるので確認
gh pr list --base main --head develop
```

既存PRがあれば、そのURLをユーザーに伝えて止まる。

### Step 2: mainに未反映の仮リリースPRを自動収集

mainにまだマージされていない仮リリース（develop向けPR）のタイトルを収集する：

```bash
# mainにマージされた最新のPRのマージ日時を取得
LAST_RELEASE_DATE=$(gh pr list --base main --state merged --limit 1 --json mergedAt \
  | jq -r '.[0].mergedAt // empty')

# それ以降にdevelopにマージされたPRを取得
if [ -n "$LAST_RELEASE_DATE" ]; then
  gh pr list --base develop --state merged --json title,mergedAt \
    | jq -r --arg since "$LAST_RELEASE_DATE" \
      '[.[] | select(.mergedAt > $since)] | sort_by(.mergedAt) | .[] | "- " + .title'
else
  gh pr list --base develop --state merged --json title,mergedAt \
    | jq -r 'sort_by(.mergedAt) | .[] | "- " + .title'
fi
```

取得したタイトルでPR説明文を自動生成し、ユーザーに確認してもらう：

```
## リリース内容
- <仮リリース1のタイトル>
- <仮リリース2のタイトル>
- ...
```

### Step 3: PR作成（ユーザー入力なし）

```bash
BODY="## リリース内容
- <自動生成した箇条書き>"

gh pr create \
  --base main \
  --head develop \
  --title "Release: $(date +%Y-%m-%d)" \
  --body "$BODY"

gh pr view --json url -q .url
```

マージはしない。URLをユーザーに伝えて完了。

トラブル発生時は `references/troubleshooting.md` を参照。
