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

@ns.route("/events/<int:year>")
class EventByYear(Resource):

    @ns.marshal_list_with(event_model)
    def get(self, year):
        all_events = Event.query.all()
        events_this_year = []
        for event in all_events:
            print(str(event.date)[:4])
            if str(event.date)[:4] == str(year):
                events_this_year.append(event)

        return events_this_year
