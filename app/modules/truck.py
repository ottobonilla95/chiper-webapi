from flask import Blueprint
from flask_restful import Api
from resources.truck import (
    TruckList,
    )

# Create bluepirnt
truck_module = Blueprint('truck', __name__)
api = Api(truck_module)

# Add resources
api.add_resource(TruckList, '/')



