# Introduction
## Person API Documentation
Base URL:	[https://hngxtask-7wst.onrender.com](https://hngxtask-7wst.onrender.com)

* Schemes
### HTTPS

### person - Everything about person's api endpoints
<br>
- POST  /api 	- add a new person to database i.e. https://hngxtask-7wst.onrender.com/api  <br>
Parameter <br>
body - This is a required field	Person that needs to be added to the database <br>
	 Example value (name must be a string) <br>
	{
   	 "name": "Mark Essien" 
  	} <br>
	Parameter content type - application/json <br>
Response <br>
	{
    "id": "00c7bdcc-226e-4052-8333-ddab11ef00aa", <br>
    "name": "Mark Essien" 
    } <br>
Code <br>
200	-	OK <br>
406	-	Not Acceptable <br>

<br>
- GET /api/user_id	- Returns a single person <br>
Parameter <br>
user_id *reqired <br>
	example request <br>
	/api/278fvmv-dkj3jd-dkkm4m4  <br>

Response <br>
Code	Description <br>
200	OK  <br>

  {
   "id": "278fvmv-dkj3jd-dkkm4m4" 
   "name": "Mark Essien"
  }
  <br>
400	Invalid ID <br>
404	person not found <br>


- PUT /api/user_id	- Updates a person <br>
Parameter <br>
user_id and name *reqired <br>
	example request <br>
	/api/278fvmv-dkj3jd-dkkm4m4 <br>
Body <br>
	{ 
   	 "name": "Onyeka_embedded" 
  	} <br>
	Parameter content type - application/json <br>
Response <br>
Code	Description <br>
200	successful <br>

  {
   "id": "278fvmv-dkj3jd-dkkm4m4" <br>
   "name": "Onyeka_embedded" 
  } 
  <br>
400	Invalid ID <br>
404	person not found <br>


- DELETE /api/user_id	- Deletes a single person <br>
Parameter <br>
user_id *reqired <br>
	example request <br>
	/api/278fvmv-dkj3jd-dkkm4m4 <br>
Response <br>
Code	Description <br>
200	successful  <br>
{
  "status": "Updated"
} <br>

404	person not found <br>

<br>
- GET /api		- Returns list of all persons <br>

Response <br>
Code	Description <br>
200	successful <br>

  {
   "id": "278fvmv-dkj3jd-dkkm4m4"
   "name": "Mark Essien"
  }, <br>
  {
   "id": "278fvmv-dkj3jd-dkkm4m4"
   "name": "Mark Essien"
  }, <br>
  {
   "id": "278fvmv-dkj3jd-dkkm4m4"
   "name": "Mark Essien"
  } <br>


404	person not found <br>	


