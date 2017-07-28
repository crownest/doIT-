# TOKEN

Method: POST

URL: http://doit.unicrow.com/api-auth/login/

Header:
~~~~
Accept application/json

Content-Type application/json
~~~~

Body:
~~~~
{
  "email": "*",
  "password": "*"
}
~~~~

Sample Request:
~~~~
  curl --request POST \
  --url http://doit.unicrow.com/api-auth/login/ \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --data '{
    "email": "*",
    "password": "*"
  }'
~~~~

Response:
~~~~
{
  "auth_token": "91f4def1bee0d16730aef26879de74d10b7cad96"
}
~~~~

# TASKS

Method: GET

URL: http://doit.unicrow.com/api/v1/tasks/

Header:
~~~~
Authorization TOKEN 91f4def1bee0d16730aef26879de74d10b7cad96
~~~~

Sample Request:
~~~~
curl --request GET \
 --url http://doit.unicrow.com/api/v1/tasks/ \
 --header 'authorization: Token 91f4def1bee0d16730aef26879de74d10b7cad96'
~~~~

Response:
~~~~
[
   {
       "id": 1,
       "user": 1,
       "title": "sdfghjk"
   }
]
~~~~

# TASKS DETAIL

Method: GET

URL: http://doit.unicrow.com/api/v1/tasks/1

Header:
~~~~
Authorization TOKEN 5f9675e15afff2a957e481dbec0a47339ac2f4ea
~~~~

Sample Request:
~~~~
curl --request GET \
 --url http://doit.unicrow.com/api/v1/tasks/1 \
 --header 'authorization: Token 5f9675e15afff2a957e481dbec0a47339ac2f4ea'
~~~~

Response:
~~~~
{
   "id": 1,
   "user": 1,
   "title": "adsafa",
   "description": "afasfasfasfas",
   "reminders": [
       {
           "id": 1,
           "date": "2017-07-25T16:27:18Z"
       }
   ]
}
~~~~
