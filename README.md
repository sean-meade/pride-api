# pride-api
API to request information, location, and time for historical pride related events throughout history. Used for hackaton project https://github.com/vanderpatrick/Hackteam-6

This API services the Out & About website.

Using flask_restx it implements swagger to make it easier to interact with. It's hosted on render and is the go between fir a postgresql database (also hosted on render) and the Out and About website.

Future improvements:

- Better error handling. Debugging during the hackathon was difficult and more strict handling and error messages would have helped immensely.
- Value handling. Currently most if not all values are strings. I would like to give each field an appropriate type.
