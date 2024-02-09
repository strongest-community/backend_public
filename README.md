# backend
## 開発wiki
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
