# Introduction
## Person API Documentation
Base URL:	[https://person.api.render.com](https://person.api.render.com)

* Schemes
### HTTPS

### person - Everything about person's api endpoints

* <p style="color:green;">POST</p> /api 	- add a new person to database <br>
Parameter <br>
body - This is a required field	Person that needs to be added to the database <br>
	 Example value (name must be a string) <br>
	{
   	 "name": "Mark Essien"
  	} <br>
	Parameter content type - application/json <br>
Response <br>
	{
    "id": "00c7bdcc-226e-4052-8333-ddab11ef00aa",
    "name": "Mark Essien"
    }
Code
200	-	OK
406	-	Not Acceptable


* GET /api/user_id	- Returns a single person
Parameter
user_id *reqired
	example request
	/api/278fvmv-dkj3jd-dkkm4m4

Response
Code	Description
200	OK 
{
  {
   "id": "278fvmv-dkj3jd-dkkm4m4"
   "name": "Mark Essien"
  }
  "status": "available"
}
400	Invalid ID
404	person not found


- PUT /api/user_id	- Updates a person
Parameter
user_id and name *reqired
	example request
	/api/278fvmv-dkj3jd-dkkm4m4
Body
	{
   	 "name": "Onyeka_embedded"
  	}
	Parameter content type - application/json
Response
Code	Description
200	successful 
{
  {
   "id": "278fvmv-dkj3jd-dkkm4m4"
   "name": "Onyeka_embedded"
  }
  "status": "Updated"
}
400	Invalid ID
404	person not found


- DELETE /api/user_id	- Deletes a single person
Parameter
user_id *reqired
	example request
	/api/278fvmv-dkj3jd-dkkm4m4
Response
Code	Description
200	successful 
{
  "status": "Updated"
}

404	person not found


- GET /api		- Returns list of all persons

Response
Code	Description
200	successful 
[
  {
   "id": "278fvmv-dkj3jd-dkkm4m4"
   "name": "Mark Essien"
  },
  {
   "id": "278fvmv-dkj3jd-dkkm4m4"
   "name": "Mark Essien"
  },
  {
   "id": "278fvmv-dkj3jd-dkkm4m4"
   "name": "Mark Essien"
  },
]
404	person not found	


