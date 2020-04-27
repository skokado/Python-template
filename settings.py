import os
from dotenv import load_dotenv


"""dotenv(.env) による設定値読み込み"""
load_dotenv(verbose=True)

env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path)

# SECRET_KEY = os.environ['SECRET_KEY']
"""
ここで定義した設定値を他のモジュールから読み込む

>>> import settings
>>> SECRET_KEY = settings.SECRET_KEY

or:
>>> from settings import SECERET_KEY
"""

