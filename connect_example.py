from pymodm import connect, MongoModel, fields


connect("mongodb+srv://akong1399:Vdn46h45@bme547.nynrw.mongodb.net/"
        "health_db?retryWrites=true&w=majority")


class User(MongoModel):
    name = fields.CharField()


x = User(name="David")
x.save()