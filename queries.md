Make sure you download the starter code and run the following:

```sh
  psql < movies.sql
  psql movies_db
```

In markdown, you can place a code block inside of three backticks (```) followed by the syntax highlighting you want, for example

```sh

SELECT \* FROM users;

```

Using the `movies_db` database, write the correct SQL queries for each of these tasks:

1.  The title of every movie.
    ```sh 
    SELECT * FROM movies;
    ```

2.  All information on the G-rated movies.
    ```sh 
    SELECT * FROM movies WHERE rating = 'G'
    ```

3.  The title and release year of every movie, ordered with the
    oldest movie first.
    ```sh
    SELECT title,release_year FROM movies ORDER BY release_year;
    ```

4.  All information on the 5 longest movies.
    ```sh
    SELECT * FROM movies ORDER BY runtime desc LIMIT 5;
    ```

5.  A query that returns the columns of `rating` and `total`, tabulating the
    total number of G, PG, PG-13, and R-rated movies.
    ```sh
    SELECT rating,COUNT(*) as total FROM movies GROUP BY rating;
    ```

6.  A table with columns of `release_year` and `average_runtime`,
    tabulating the average runtime by year for every movie in the database. The data should be in reverse chronological order (i.e. the most recent year should be first).
    ```sh
    SELECT release_year,COUNT(*),AVG(runtime) as average_runtime FROM movies GROUP BY release_year ORDER BY release_year
    ```

7.  The movie title and studio name for every movie in the
    database.
    ```sh
    SELECT m.title,s.name FROM movies m JOIN studios s ON m.studio_id = s.id;
    ```

8.  The star first name, star last name, and movie title for every
    matching movie and star pair in the database.
    ```sh
    SELECT s.first_name,s.last_name,m.title FROM roles r JOIN stars s ON r.star_id = s.id JOIN movies m ON r.movie_id = m.id;
    ```
    
9.  The first and last names of every star who has been in a G-rated movie. The first and last name should appear only once for each star, even if they are in several G-rated movies. *IMPORTANT NOTE*: it's possible that there can be two *different* actors with the same name, so make sure your solution accounts for that.
    ```sh
    SELECT s.first_name,s.last_name,m.rating FROM roles r JOIN stars s ON r.star_id = s.id JOIN movies m ON r.movie_id = m.id WHERE m.rating = 'G';
    ```

10. The first and last names of every star along with the number
    of movies they have been in, in descending order by the number of movies. (Similar to #9, make sure
    that two different actors with the same name are considered separately).
    ```sh 
    SELECT s.first_name,s.last_name,COUNT(*) as total_movies FROM roles r JOIN stars s ON r.star_id = s.id JOIN movies m ON r.movie_id = m.id GROUP BY s.id,s.first_name,s.last_name ORDER BY total_movies desc
    ```

### The rest of these are bonuses

11. The title of every movie along with the number of stars in
    that movie, in descending order by the number of stars.
    ```sh
    SELECT m.title,COUNT(*) as total_actors FROM roles r JOIN movies m ON r.movie_id = m.id GROUP BY m.title ORDER BY total_actors;
    ```

12. The first name, last name, and average runtime of the five
    stars whose movies have the longest average.
    ```sh
    SELECT s.first_name,s.last_name,AVG(m.runtime) as averge FROM roles r JOIN stars s ON r.star_id = s.id JOIN movies m ON m.id = r.movie_id GROUP BY s.first_name,s.last_name ORDER BY averge desc LIMIT 5;
    ```

13. The first name, last name, and average runtime of the five
    stars whose movies have the longest average, among stars who have more than one movie in the database.
    ```sh
    SELECT s.first_name,s.last_name,COUNT(*) as total,AVG(m.runtime) as averge FROM roles r JOIN stars s ON s.id = r.star_id JOIN movies m ON m.id = r.movie_id GROUP BY s.first_name,s.last_name ORDER BY total desc,averge desc LIMIT 5;
    ```
14. The titles of all movies that don't feature any stars in our
    database.
    ```sh
    SELECT m.title,r.id as id FROM roles r RIGHT JOIN movies m ON m.id = r.movie_id ORDER BY id desc LIMIT 25;
    ```

15. The first and last names of all stars that don't appear in any movies in our database.
    ```sh
    SELECT s.last_name,s.first_name,r.id FROM roles r RIGHT JOIN stars s ON s.id = r.star_id ORDER BY r.id desc LIMIT 10;
    ```

16. The first names, last names, and titles corresponding to every
    role in the database, along with every movie title that doesn't have a star, and the first and last names of every star not in a movie.
    ```sh
    SELECT s.first_name,s.last_name,m.title FROM roles r FULL JOIN movies m ON m.id = r.movie_id FULL JOIN stars s ON s.id = r.star_id;
    ```