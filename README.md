# pride-api
API to request information, location, and time for historical pride related events throughout history. Used for hackaton project https://github.com/vanderpatrick/Hackteam-6

This API services the Out & About website.

Using flask_restx it implements swagger to make it easier to interact with. It's hosted on render and is the go between fir a postgresql database (also hosted on render) and the Out and About website.

#### Database Models

A PostgreSQL database hosted on render.com was used to hold the data collected for pride events.

##### Pride Event Model

A model describing a pride-related event that happen across the world.

| Key        | Name        | Type    | Extra Info                |
| ---------- | ----------- | ------- | ------------------------- |
| PrimaryKey | id          | Integer | Unique id                 |
|            | event       | String  | Title of Event            |
|            | date        | Date    | Date event happened       |
|            | country     | String  | Country event happened in |
|            | region      | String  | Region event happened in  |
|            | description | String  | Description of event       |
|            | image_link  | String  | Link to related image     |
|            | lat         | String  |                           |
|            | long        | String  |                           |

##### Contact Event Model

A model describing the information provided through the contact form

| Key        | Name        | Type    | Extra Info                |
| ---------- | ----------- | ------- | ------------------------- |
| PrimaryKey | id          | Integer |                           |
|            | email       | String  | email of contact          |
|            | country     | String  | Country event happened in |
|            | description | String  | Description of even       |

#### API for pride events

An API was built using Flask and flask_restx to handle different queries between the website and the database. It was hosted as a Web Service on render.com. The queries and url paths are explained below.

BASE_URL = https://pride-api.onrender.com

##### Get all events

Type of HTTP request: `GET`

URL: {BASE_URL}/api/events

On a successful request it returns a status of `200` and all the events in the database as a list:

```
[
  {
    "id": 0,
    "event": "string",
    "date": "string",
    "country": "string",
    "region": "string",
    "description": "string",
    "image_link": "string",
    "lat": "string",
    "long": "string"
  },
  .
  .
  .
]
```

##### Add an event

Type of HTTP request: `POST`

URL: {BASE_URL}/api/events

Package sent with `POST` request:

```
{
  "event": "string",
  "date": "string", // in the format of '%Y-%m-%d'
  "country": "string",
  "region": "string",
  "description": "string",
  "image_link": "string",
  "lat": "string",
  "long": "string"
}
```

On a successful request it returns `200` and the newly added event with an `id`:

```
{
  "id": 0,
  "event": "string",
  "date": "string",
  "country": "string",
  "region": "string",
  "description": "string",
  "image_link": "string",
  "lat": "string",
  "long": "string"
}
```

##### Edit an existing event in the database

Type of HTTP request: `PUT`

URL: {BASE_URL}//api/events/{id}

Where `id` is the id of the event you want to edit.

Package sent with `PUT` request:

```
{
  "event": "string",
  "date": "string",
  "country": "string",
  "region": "string",
  "description": "string",
  "image_link": "string",
  "lat": "string",
  "long": "string"
}

```

Returns with status `200` and the event you just edited:

```
{
  "id": 0,
  "event": "string",
  "date": "string",
  "country": "string",
  "region": "string",
  "description": "string",
  "image_link": "string",
  "lat": "string",
  "long": "string"
}
```

##### Delete an existing event from the database

Type of HTTP request: DELETE

URL: {BASE_URL}//api/events/{id}

Where `id` is the id of the event you want to delete.

##### Search events by country

Type of HTTP request: `GET`

URL: {BASE_URL}/api/events/{country}

Where `country` is the name of the country you are searching for (currently case sensitive).

On a successful request it returns a status of `200` and all the events in the database with that country name:

```
[
  {
    "id": 0,
    "event": "string",
    "date": "string",
    "country": "string",
    "region": "string",
    "description": "string",
    "image_link": "string",
    "lat": "string",
    "long": "string"
  },
  .
  .
  .
]
```

##### Get all contact form submissions

Type of HTTP request: `GET`

URL: {BASE_URL}/api/contacts

On a successful request it returns a status of `200` and all the contact form submissions in the database as a list:

```
[
  {
    "id": 0,
    "email": "string",
    "country": "string",
    "description": "string"
  },
  .
  .
  .
]
```

##### Add contact form submission to database

Type of HTTP request: `POST`

URL: {BASE_URL}/api/contacts

The package provided with the request:

```
{
  "email": "string",
  "country": "string",
  "description": "string"
}
```

On a successful request it returns a status of `200` and the newly added contact with an `id`:

```
{
  "id": 0,
  "email": "string",
  "country": "string",
  "description": "string"
}
```

Future improvements:

- Better error handling. Debugging during the hackathon was difficult and more strict handling and error messages would have helped immensely.
- Value handling. Currently most if not all values are strings. I would like to give each field an appropriate type.
