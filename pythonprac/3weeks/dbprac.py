# mongoDB 연결하기
from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://sparta:test@cluster0.0mtn7sx.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)      # 주소 넣기
db = client.dbsparta

# doc = {
#     'name': '영수',
#     'age': 24
# }

# doc = {
#     'name': '영희',
#     'age': 30
# }
# db.users.insert_one(doc)

# doc = {
#     'name': '철수',
#     'age': 20
# }
# db.users.insert_one(doc)

## 모든 데이터 한번에 보기
# all_users = list(db.users.find({},{'_id':False}))
# # find({}) find뒤에 중괄호가 빈칸이면 아무 조건이 없는것 _id 값이 붙어서 출력됨
# # {'_id':False} _id를 보지 않겠다라는 의미

# for a in all_users: 
#     print(a['name'][1])

# # 데이터 하나만 가져오기
# user = db.users.find_one({})
# print(user)

# # 조작하기
# db.users.update_one({'name':'영수'},{'$set':{'age':19}})

# # 지우기
# db.users.delete_one({'name': '영수'})

#최종 정리
# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
all_users = list(db.users.find({},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})