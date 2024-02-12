# backend

## 制作物概要

### 概要

- 2024/02/10, 11 に開催された[Qiita Hackathon](https://qiita.com/official-campaigns/hackathon/2024-first)の予選でチーム史上最強コミュニティが作成した web アプリケーションの backend です。
- デートプラン共有アプリ「Couple Canvas」を作成しました。当アプリフロントエンド実装は[こちら](https://github.com/strongest-community/web_public)のリポジトリから確認できます.

### 発表資料

- 当日発表資料
  - [PDF](https://drive.google.com/file/d/1YkphcnxUufjyx4-JaE6nSClMftS8uctG/view?usp=sharing) 
- デモ動画
  - [Youtube](https://www.youtube.com/watch?v=1wJBQkTx-Pk)

### 技術スタック

- 開発言語
  - Python
- フレームワーク
  - fastapi
  - uvicorn
  - sqlalchemy
  - aiomysql
  - python-dotenv
  - python-jose
  - passlib
  - bcrypt
  - python-multipart
- ER 図
  - [ER 図(draw.io に遷移します)](https://drive.google.com/file/d/1HYJkTjVxm52Y9ErDmMvKgxeTnKLuwX4v/view?usp=sharing)

## 実行方法

- docker desktop がインストールされていることを前提とします。
- `docker-compose build`
- `docker-compose up`
- 必要に応じて新しいターミナルで以下を実行
  - `docker-compose run --entrypoint "poetry install --no-root" app`
    - 依存関係のインストール
  - `docker-compose exec app poetry run python -m api.migrate_db`
    - DB の migrate と seed の挿入
- [swagger](http://localhost:8000/docs)
- [エントリーポイント](http://localhost:8000/)
