from startapp.model.baseModel import db


def createuser():
    try:
        db.drop_all()
        db.create_all()
        return 1
    except:
        return -1


def getall(model):
    return model.query.all()


def insertone(model):
    try:
        db.session.add(model)
        db.session.commit()
        return 1
    except:
        return -1
