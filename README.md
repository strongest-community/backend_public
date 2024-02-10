# backend

## 実行方法

- `.venv`と`poetry.lock`を削除する
- `docker-compose build`
- `docker-compose up`
- 新しいターミナルで以下を実行
  - `docker-compose run --entrypoint "poetry install --no-root" app`
  - `docker-compose exec app poetry run python -m api.migrate_db`
- [swagger](http://localhost:8000/docs)
- [エントリーポイント](http://localhost:8000/)

## DB の概要

[ER 図](https://drive.google.com/file/d/1HYJkTjVxm52Y9ErDmMvKgxeTnKLuwX4v/view?usp=sharing)

<details><summary>ER図</summary>

```
mysql> show tables;
+-----------------------+
| Tables_in_demo        |
+-----------------------+
| places                |
| plan_comment_relation |
| plan_like_relation    |
| plans                 |
| users                 |
+-----------------------+
5 rows in set (0.01 sec)

mysql> DESCRIBE tasks;
ERROR 1146 (42S02): Table 'demo.tasks' doesn't exist
mysql> describe places;
+---------+---------------+------+-----+---------+----------------+
| Field   | Type          | Null | Key | Default | Extra          |
+---------+---------------+------+-----+---------+----------------+
| id      | int           | NO   | PRI | NULL    | auto_increment |
| plan_id | int           | YES  | MUL | NULL    |                |
| url     | varchar(1024) | YES  |     | NULL    |                |
+---------+---------------+------+-----+---------+----------------+
3 rows in set (0.01 sec)

mysql> describe plan_comment_relation;
+---------+--------------+------+-----+---------+----------------+
| Field   | Type         | Null | Key | Default | Extra          |
+---------+--------------+------+-----+---------+----------------+
| id      | int          | NO   | PRI | NULL    | auto_increment |
| user_id | int          | YES  | MUL | NULL    |                |
| plan_id | int          | YES  | MUL | NULL    |                |
| comment | varchar(140) | YES  |     | NULL    |                |
+---------+--------------+------+-----+---------+----------------+
4 rows in set (0.01 sec)

mysql> describe plan_like_relation;
+---------+------+------+-----+---------+----------------+
| Field   | Type | Null | Key | Default | Extra          |
+---------+------+------+-----+---------+----------------+
| id      | int  | NO   | PRI | NULL    | auto_increment |
| user_id | int  | YES  | MUL | NULL    |                |
| plan_id | int  | YES  | MUL | NULL    |                |
+---------+------+------+-----+---------+----------------+
3 rows in set (0.00 sec)

mysql> describe plans;
+-------------+--------------+------+-----+---------+----------------+
| Field       | Type         | Null | Key | Default | Extra          |
+-------------+--------------+------+-----+---------+----------------+
| id          | int          | NO   | PRI | NULL    | auto_increment |
| description | varchar(512) | YES  |     | NULL    |                |
| budget      | int          | YES  |     | NULL    |                |
| situation   | varchar(256) | YES  |     | NULL    |                |
| with_whom   | varchar(256) | YES  |     | NULL    |                |
+-------------+--------------+------+-----+---------+----------------+
5 rows in set (0.00 sec)

mysql> describe users;
+-------+--------------+------+-----+---------+----------------+
| Field | Type         | Null | Key | Default | Extra          |
+-------+--------------+------+-----+---------+----------------+
| id    | int          | NO   | PRI | NULL    | auto_increment |
| name  | varchar(20)  | YES  |     | NULL    |                |
| mail  | varchar(128) | YES  |     | NULL    |                |
+-------+--------------+------+-----+---------+----------------+
3 rows in set (0.00 sec)

mysql>
```

</details>

## 開発 wiki

### poetry の設定

- vscode で docker が読み込まれずに import error の下線が出る場合がある

```
pip install poetry
```

```
poetry install
```

その後、エラー箇所から「別のインタープリターを選択」から poetry のインタープリターを選択する

### 青色の下線が出る場合の対処法

- 前提
  - 以下の二つの拡張機能がインストールされていること
    - [workspace default settings](https://marketplace.visualstudio.com/items?itemName=dangmai.workspace-default-settings)
    - [Cspell](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)

```
.vscode/settings.json
```

に該当の単語が入っていることを確認する。

### branch を切る

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

ー前提 - docker がインストールされていること - [docker](https://www.docker.com/products/docker-desktop)

```
docker-compose up
```

[swagger](http://localhost:8000/docs)
