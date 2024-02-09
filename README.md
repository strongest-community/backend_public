# backend
## 開発wiki
### poetryの設定
- vscodeでdockerが読み込まれずにimport errorの下線が出る場合がある
```
pip install poetry
```
```
poetry install
```
その後、エラー箇所から「別のインタープリターを選択」からpoetryのインタープリターを選択する

### 青色の下線が出る場合の対処法
- 前提
    - 以下の二つの拡張機能がインストールされていること
        - [workspace default settings](https://marketplace.visualstudio.com/items?itemName=dangmai.workspace-default-settings)
        - [Cspell](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
```
.vscode/settings.json
```
に該当の単語が入っていることを確認する。

### branchを切る
ー新規ブランチの作成
```
git switch -c <branch_name>
```
- ブランチの確認
```
git branch
```

### ブランチの切り替え
```
git switch <branch_name>
```

### 最新版の取得(main)
```
git pull origin main
```

### ブランチに最新版を適応
```
git switch main
git pull origin main
git switch <branch_name>
git merge main
```

## 実行方法
ー前提
    - dockerがインストールされていること
        - [docker](https://www.docker.com/products/docker-desktop)

```
docker-compose up
```
[swagger](http://localhost:8000/docs)
