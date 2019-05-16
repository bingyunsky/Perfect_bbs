import os

DEBUG = True

DB_URI = "mysql+pymysql://root:vince120611@localhost:3306/perfect_bbs?charset=utf8"

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRANK_MODIFICATIONS = True
SOLALCHEMY_COMMIT_TEARDOWN = True

SECRET_KEY = os.urandom(24)
CMS_USER_ID = 'abcdefg'  # 随便写一值，这样session更加安全
