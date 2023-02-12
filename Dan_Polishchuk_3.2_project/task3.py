
from sqlite3 import connect

sqlite_path = "C:\\Uni_tasks\\Dan_Polishchuk_3.2_project\\sql_lab.db"

conn = connect(sqlite_path)
cur = conn.cursor()


def query(request, description):
    cur.execute(request)
    rows = cur.fetchall()
    print(description, ":\n", *rows, "\n")


query("""SELECT Title FROM Movies""",
      "1. Title of each movie")

query("""SELECT Title,Director,Year FROM Movies""",
      "2. Director and year of each file")

query("""SELECT * FROM Movies""",
      "3. Info about each movie")

query("""SELECT * FROM Movies WHERE Id="6" """,
      "4. Film with id = 6")

query("""SELECT * FROM Movies WHERE Year BETWEEN 2000 AND 2010""",
      "5. Movies released between 2000 and 2010")

query("""SELECT * FROM Movies WHERE Year IN (2006,2088,2010)""",
      "6. Movies released in 2006, 2010, 2088")

query("""SELECT Title,Director,Year FROM Movies WHERE Year NOT BETWEEN 2010 AND 2013""",
      "7. Movies released before 2010")

query("""SELECT * FROM Movies WHERE Title LIKE "Toy Story%" """,
      "8. All 'Toy Story' movies")

query("""SELECT * FROM Movies WHERE Title LIKE "Toy Story _" """,
      "9. 2 of 3 'Toy Story' movies found in a different way")

query("""SELECT Title,Director FROM Movies WHERE Director LIKE "John Lasseter" """,
      "10. Movies made by John Lasseter")

query("""SELECT Title,Director FROM Movies WHERE Director NOT LIKE "John Lasseter" """,
      "11. Movies not made by John Lasseter")

query("""SELECT Title FROM Movies WHERE Title LIKE "WALL-%" """,
      "12. All WALL- movies")

query("""SELECT DISTINCT Director FROM Movies ORDER BY Director """,
      "13. List of directors in alphabetical order without duplication")

query("""SELECT Title,Year FROM Movies ORDER BY Year DESC LIMIT 4""",
      "14. The newest 4 movies")

query("""SELECT Title FROM Movies ORDER BY Title ASC LIMIT 5""",
      "15. 5 first movies in alphabetical order")

query("""SELECT Title FROM Movies ORDER BY Title ASC LIMIT 5 OFFSET 5""",
      "16. The next 5")

query("""SELECT Title,Domestic_sales, International_sales FROM Movies 
      INNER JOIN Boxoffice ON Movies.Id = Boxoffice.Movie_id""",
      "17-18. International and Domestic sales of each movie")

query("""SELECT Title, Rating FROM Movies 
      INNER JOIN Boxoffice ON Movies.Id = Boxoffice.Movie_id ORDER BY Rating DESC""",
      "19. Movie ratings in descending order")

query("""SELECT Building_names,Name,Role FROM Buildings 
      LEFT OUTER JOIN Employees ON Buildings.building_names = Employees.Building""",
      "20. List of buildings and people who live there and their professions")

query("""SELECT Building,Name,Role FROM Employees WHERE Building LIKE "" """,
      "21. list of people and their specialties that are not attached to houses")

query("""SELECT Title,Domestic_sales + International_sales FROM Movies
      LEFT OUTER JOIN Boxoffice ON Movies.Id = Boxoffice.Movie_id""",
      "22. Movies and their total box offices")