
import requests
from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required

from libs.auditory import Auditory
from sodapy import Socrata

class TruckList(Resource):
    @jwt_required
    def get(self):
        try:
            params = request.args

            client = Socrata("data.sfgov.org", None)
            trucks = client.get("rqzj-sfat", limit=200, where=f"within_box(location, {params.get('lat1')}, {params.get('long1')}, {params.get('lat2')}, {params.get('long2')})")
            
            return {"trucks":trucks}

        except Exception as e:
            Auditory.log_error("WebApi", "Truck", "TruckList", str(e))
            return {"message": "Error when fetching trucks"}, 500
