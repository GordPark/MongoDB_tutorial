from pymongo import MongoClient

# MongoDB 인스턴스에 연결
# client = MongoClient('mongodb://localhost:27017/') # 테스트 할때는 아이디 비번 안넣음
client = MongoClient('mongodb://likelion:1234@hanslab.org:27117/')

# 데이터베이스 선택 (없으면 새로 생성됨)
db = client['tutorial_db_prg']

# 컬렉션 선택 (없으면 새로 생성됨)
collection = db['tutorial_collection']

client.list_database_names()

# 새 문서 생성 및 삽입
document = {"name": "John Doe", "age": 30, "city": "New York"}
collection.insert_one(document)

# 모든 문서 조회
for doc in collection.find():
    print(doc)

# 특정 조건에 맞는 문서 조회
query = {"city": "New York"}
documents = collection.find(query)
for doc in documents:
    print(doc)
