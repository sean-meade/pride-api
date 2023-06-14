from flask_restx import Resource, Namespace 

from .api_models import event_model
from .extensions import db
from .models import Event

ns = Namespace("api")

@ns.route("/hello")
class Hello(Resource):
    def get(self):
        return {"hello": "restx"}

@ns.route("/events")
class EventsListAPI(Resource):
    # marshall is to return the format defined in event_model
    @ns.marshal_list_with(event_model)
    def get(self):
        return Event.query.all()

