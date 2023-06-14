from flask_restx import fields

from .extensions import api

class MyDateFormat(fields.Raw):
    def format(self, value):
        return value.strftime('%Y-%m-%d')

event_model = api.model("Pride Historical Event", {
    "id": fields.Integer,
    "event": fields.String,
    'date': MyDateFormat,
    "event_description": fields.String
})