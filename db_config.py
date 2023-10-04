import os
import datetime
import logging
from playhouse.db_url import connect
from dotenv import load_dotenv
from peewee import Model, IntegerField, CharField, TextField, TimestampField

# .envの読み込み
load_dotenv()

# ①実行したSQLをログで出力する設定
logger = logging.getLogger("peewee")
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

# ②データベースへの接続設定
# db = SqliteDatabase("peewee_db.sqlite")  # SQLite固定の場合
db = connect(os.environ.get("DATABASE"))  # 環境変数に合わせて変更する場合
# db = connect(os.environ.get("DATABASE") or "sqlite:///peewee_db.sqlite")  # 環境変数が無い場合にデフォルト値として値を設定することも可能

# 接続NGの場合はメッセージを表示
if not db.connect():
    print("接続NG")
    exit()

# ③メッセージのモデル
class User(Model):

    id = IntegerField(primary_key=True)  # idは自動で追加されるが明示
    Company_Name = CharField()
    Department = CharField()
    name = CharField()
    email_address =  CharField()
    telephone_number =  CharField()

    class Meta:
        database = db
        table_name = "User"

class DXTool(Model):

    tool_id = IntegerField(primary_key=True)  # ツールIDは自動で追加されるが明示
    tool_name = CharField()  # ツール名
    tool_attribute = CharField()  # ツール属性
    tool_url = CharField()  # ツールURL

    class Meta:
        database = db
        table_name = "dx_tools"


# 既存のテーブルと新しく追加するテーブルを作成
db.create_tables([User, DXTool])