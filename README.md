# How to setup, run and use person API

- https//...render.com is the base url for the api, To make request(CRUD)
user needs to add the necessary path.

- For CREATE operation, add /api to the base url i.e.
  https//...render.com/api - This creates a person

- For READ operation, add /api/user_id to the base url i.e.
  https//...render.com/api/user|_id - This returns a single person, without 
				      user_id it returns list of persons

- For UPDATE operation, add /api/user_id to the base url and the name to be update to the body of the method i.e.
  https//...render.com/api - This updates a single person

- For DELETE operation, add /api/user_id to the base url i.e.
  https//...render.com/api - This creates a person

[UML LINK]
