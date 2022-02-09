<h1>Title: Restaurant</h1>

<p>This is just the beginning to a great database. Currently I just have one table called Employees. There are
multiple APIs to communicate with the server by using Django's built in ORM. 
</p>

<h3>Tools Used:</h3>
<p>The tools used in this project were Django, Django ORM, Docker Compose, PostgreSQL, Github, Deployed to Amazon AWS (since deleted) using nginx and EC2</p>

endpoint paths, methods, perameters 

| Table     |   Description    |     Path      |   Method  |  Parameter                                                     |
| --------- | ---------------- | ------------- |  -------  | -------------------------------------------------------------- |
| EMPLOYEES | adds a new input |      ''       |    POST   | name(str), email(str), phone_number(int), clock_in_number(int) |
| EMPLOYEES | shows an id      |   '<int:id>'  |    GET    | -------------------------------------------------------------- |
| EMPLOYEES | deletes an id    |   '<int:id>'  |    DEL    | -------------------------------------------------------------- |
| EMPLOYEES | updates an id    |   '<int:id>'  | PUT/PATCH | name(str), email(str), phone_number(int), clock_in_number(int) |

# restaurant_api
# restaurant_api

