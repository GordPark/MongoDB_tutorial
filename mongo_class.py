from pymongo import MongoClient

class MongoDB_CRUD:
    def __init__(self):
        # MongoDB 인스턴스에 연결
        # client = MongoClient('mongodb://localhost:27017/') # 테스트 할때는 아이디 비번 안넣음
        self.client = MongoClient('mongodb://likelion:1234@hanslab.org:27117/')

    def mong_create(self):
        # 데이터베이스 선택 (없으면 새로 생성됨)
        db = self.client['tutorial_db_prg']

        # 컬렉션 선택 (없으면 새로 생성됨)
        self.collection = db['tutorial_collection']       
        return self.collection

    def mong_insert(self,key1,val1, key2,val2,key3, val3):
        document = {key1:val1,key2:val2,key3:val3}
        self.collection.insert_one(document)
        
    
    def mong_find(self,key,value):
        query = {key:value}
        documents = self.collection.find(query)
        for doc in documents:
            print(doc)

    def mong_all_find(self):
        for doc in self.collection.find():
            print(doc)

    def mong_update(self,key1,val1,key2,val2):
        self.collection.update_one(
            {key1:val1}, # 조건
            {"$set":{key2:val2}} # 변경할 내용
        )

    def mong_delete(self,key1,val1):
        self.collection.delete_one({key1:val1})

col = MongoDB_CRUD()
col.mong_create()
# col.mong_insert("name","John Doe","age",30,"city","Manhattan")
# col.mong_find("name","John Doe")
# col.mong_update("name","John Doe","city","Texas")
col.mong_delete("name","John Doe")
col.mong_all_find()



