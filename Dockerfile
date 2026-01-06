# ベースイメージとしてPythonの公式イメージを使用
FROM python:3.13-slim

# 作業ディレクトリを/appに設定
WORKDIR /app

# requirements.txtをコンテナにコピー
COPY requirements.txt .

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# スクリプトをコンテナにコピー
COPY ./path2csv ./path2csv
COPY ./path2csv_setup ./path2csv_setup

# コンテナ起動時のデフォルトコマンド
ENTRYPOINT ["python", "-m"]

# メタデータの追加
LABEL org.opencontainers.image.source="https://github.com/bteam-toku/path2csv_develop.git"
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.opencontainers.image.description="フォルダ・ファイルリスト出力（Dockerコンテナ）"