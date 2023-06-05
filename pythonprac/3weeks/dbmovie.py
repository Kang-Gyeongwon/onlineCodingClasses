from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://sparta:test@cluster0.0mtn7sx.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)  
db = client.dbsparta

# # 극장판 짱구는 못말려: 동물소환 닌자 배꼽수비대 평점 가져오기
# movie = db.movies.find_one({'title':'극장판 짱구는 못말려: 동물소환 닌자 배꼽수비대'})
# print(movie['star'])

# # 극장판 짱구는 못말려: 동물소환 닌자 배꼽수비대 평점과 같은 평점의 영화 제목들 가져오기
# target_star = movie['star']
# movies = list(db.movies.find({'star': target_star},{'_id':False}))
# for a in movies:
#     print(a["title"])

# 극장판 짱구는 못말려: 동물소환 닌자 배꼽수비대 영화의 평점을 0으로 만들기
db.movies.update_one({'title':'극장판 짱구는 못말려: 동물소환 닌자 배꼽수비대'},{'$set':{'star':0}})
