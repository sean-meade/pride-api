from flask_restx import fields

from .extensions import api

class MyDateFormat(fields.Raw):
    def format(self, value):
        return value.strftime('%Y-%m-%d')

event_model = api.model("Pride Historical Event", {
    "id": fields.Integer,
    "event": fields.String,
    'date': MyDateFormat,
    "description": fields.String,
    "lat": fields.String,
    "long": fields.String
})

event_input_model = api.model("EventInput", {
    "event": fields.String,
    'date': fields.String,
    "description": fields.String,
    "lat": fields.String,
    "long": fields.String,
})