from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('porsche', user='postgres',
                        password='12345', host='localhost', port=5423)


class BaseModel(Model):
    class Meta:
        database = db


class Vehicle(BaseModel):
    name = CharField()
    price = CharField()
    type = CharField()
    acceleration = CharField()
    power = CharField()


db.connect()
db.drop_tables([Vehicle])
db.create_tables([Vehicle])

app = Flask(__name__)


@app.route('/vehicle/', methods=['GET', 'POST'])
@app.route('/vehicle/<id>', methods=['GET', 'PUT', 'DELETE'])
def endpoint(id=None):
    if request.method == 'GET':
        if id:
            return jsonify(model_to_dict(Vehicle.get(Vehicle.id == id)))
        else:
            vehicleList = []
            for vehicle in Vehicle.select():
                vehicleList.append(model_to_dict(Vehicle))
            return jsonify(vehicleList)

    if request.method == 'POST':
        new_vehicle = dict_to_model(Vehicle, request.get_json())
        new_vehicle.save()
        return jsonify({"success": True})

    if request.method == 'DELETE':
        return 'DELETE request'


app.run(debug=True, port=5432)
