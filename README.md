# docker_django

# Djangoの中身がわからない自分へ

## docker環境でのサーバ起動呪文
docker run --rm -v "$PWD":/code/ -p 8000:8000 my-django-app python manage.py runserver 0.0.0.0:8000


## 始め方
startproject コマンドでプロジェクトを作成
コマンド記入
startapp コマンドで必要なアプリを作成(アプリは複数作成可)
コマンド記入

### フレームワークの中身の流れ
1. ユーザーがURIでリクエストを送る
2. my_django/urls.pyのurlpatternsを参照してどこに飛ばすか決める。


### aopの中身について
#### migrations.py
データベースの設定に関連したフォルダ。
あまり触る必要はなし。
#### admin.py
管理画面に関する設定ファイル。
#### app.py
djangoのアプリケーション自体の設定ができるファイル
#### models.py
データベース操作のためのファイル。SQLを使わずクラスを使ってデータベースを管理できるようになるファイル
#### test.py
テストをするためのファイル。今は使わない。
#### views.py
実際の処理を書くファイル

### app作成後手順
1. setting.pyファイルのINSTALLED_APPSのリストに
アプリ名.app.アプリ名(最初大文字)configという文字列を追加
2. urls.pyにimport includeを追加、path関数


### djangoの処理の流れ
1. リクエストオブジェクトが作成される
2. url.pyを参照してパスに一致した処理を探す
3. その処理をrezuestオブジェクトを引数にして関数を呼び出す
4. 呼び出した関数で処理されたあとはhttpresponseオブジェクトを受け取る
5. 最後にhttpresponseオブジェクトをブラウザに返して描画されてユーザーに見れる