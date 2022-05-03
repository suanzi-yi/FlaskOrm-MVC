from startapp.repository.userDao import createuser,getall,insertone

def create_user():
    return createuser()

def insert_one(model):
    return insertone(model)

def get_all(model):
    return  getall(model)