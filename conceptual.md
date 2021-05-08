### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
  <br /> 
  popular,powerful,Python-base ORM(object-relational-mapping),
  it's translation service between OOP in our server language and relation data in our database

- What is the difference between SQL and PostgreSQL?
  <br /> 
  SQL is Structure query language,a human readable language for querying,
  PostgreSQL as an ORDBMS(object relational database management system)

- In `psql`, how do you connect to a database?
  <br /> 
  runs command "/c database_name"

- What is the difference between `HAVING` and `WHERE`?
  <br /> 
  "WHERE" is like a condition when query a data,"HAVING" it's often combine with "GROUP By" it's a condition of "GROUP BY"

- What is the difference between an `INNER` and `OUTER` join?
  <br /> 
  "INNER" join it's default join method when we join with two related table,which join any data that is relative to each other."OUTER" join have left join and right join,
  left join means join any related data includes the columns table on the left side.right join will includes any columns on the right side.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
  <br /> 
  "OUTER" join have left join and right join,
  left join means join any related data includes the columns table on the left side.right join will includes any columns on the right side.

- What is an ORM? What do they do?
  <br /> 
  it's stands for Object Relational Mapping,it's translate server between specific server language and database.allow to manages database via the servers 

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
  <br /> 
  Using AJAX is MAKING HTTP requests via the front end or the client,using requests in making the HTTP requests via the backend.

- What is CSRF? What is the purpose of the CSRF token?
  <br /> 
  it's for Cross Site Request Forgery,it's purpose is prevent hacker for submit a forgery 
  data.

- What is the purpose of `form.hidden_tag()`?
  <br /> 
  hidden CSRF token when submission a form with WTForms
  