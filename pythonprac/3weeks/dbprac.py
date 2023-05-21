# pymongo를 통해서 mongodb 접속하기
from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:<test>@cluster0.qp2tpln.mongodb.net/?retryWrites=true&w=majority')      # monbodb 주소 입력
db = client.dbsparta