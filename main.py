from peewee import *

db = PostgresqlDatabase('porsche', user='brandonneves',
                        password='12345', host='localhost', port=5432)

db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Vehicle(BaseModel):
    name = CharField()
    price = CharField()
    type = CharField()
    acceleration = CharField()
    power = CharField()


db.drop_tables(Vehicle)
db.create_tables([Vehicle])

nineeleven = Vehicle(name="Nineeleven", price="101200",
                     type="coupe", acceleration="4.0", power="379")
nineeleven.save()

cayman = Vehicle(name="Cayman", price="60500", type="coupe",
                 acceleration="4.9", power="300")
cayman.save()

cayenne = Vehicle(name="Cayenne", price="69000",
                  type="suv", acceleration="5.9", power="335")
cayenne.save()

macan = Vehicle(name="Macan", price="54900",
                     type="suv", acceleration="6.0", power="261")
macan.save()

panamera = Vehicle(name="Panamera", price="88400",
                   type="sedan", acceleration="5.3", power="325")
panamera.save()

taycan = Vehicle(name="Taycan", price="82700",
                 type="sedan", acceleration="5.1", power="402")
taycan.save()
