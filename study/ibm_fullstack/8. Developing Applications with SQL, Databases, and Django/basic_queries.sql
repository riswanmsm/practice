-- consider the below scenario
-- there is a table called FilmLocations
-- FilmLocations tables has columns as Title, ReleaseYear, Locations, FunFacts, ProductionCompany, Distributor, Director, Writer, Actor1, Actor2, Actor3
-- 1. Retrieve all records with all columns from the “FilmLocations” table.
SELECT * FROM FilmLocations;
-- 2. Retrieve the names of all films with director names and writer names.
SELECT Title, Director, Writer FROM FilmLocations;
-- 3. Retrieve the names of all films released in the 21st century and onwards (release years after 2001 including 2001), along with filming locations and release years.
SELECT Title, ReleaseYear, Locations FROM FilmLocations WHERE ReleaseYear>=2001;
-- 4. Retrieve the fun facts and filming locations of all films.
SELECT Locations, FunFacts FROM FilmLocations;
-- 5. Retrieve the names of all films released in the 20th century and before (release years before 2000 including 2000) that, along with filming locations and release years.
SELECT Title, ReleaseYear, Locations FROM FilmLocations WHERE ReleaseYear<=2000;
-- 6. Retrieve the names, production company names, filming locations, and release years of the films which are not written by James Cameron.
SELECT Title, ProductionCompany, Locations, ReleaseYear FROM FilmLocations WHERE Writer<>"James Cameron";

-- COUNT is used to Get the total number of rows according to the condition in a table
SELECT COUNT(*) FROM FilmLocations;
SELECT COUNT(ReleaseYear) FROM FilmLocations WHERE ReleaseYear >= 2002;

-- DISTINCT is used to remove duplicate values from a result set
SELECT DISTINCT Title FROM FilmLocations;
SELECT DISTINCT Title FROM FilmLocations WHERE ReleaseYear > 2000;

-- LIMIT is used for restricting the number of rows retrieved from the database
SELECT * FROM FilmLocations LIMIT 10;
SELECT DISTINCT Title FROM FilmLocations WHERE ReleaseYear > 2018 LIMIT 2;

-- consider the below table for queries follow that
/*
Instructor (
    ins_id:     unique identification number of the instructors,    
    lastname:   last name of the instructors,
    firstname:  first name of the instructors,
    city:       name of the cities where instructors are located,
    country:    two-letter country code of the countries where instructors are located
)
*/

-- create the table
CREATE table Instructor (
    ins_id int,    
    lastname varchar(250),
    firstname varchar(250),
    city varchar(250),
    country varchar(250)
);

-- insert into Instructor
INSERT INTO Instructor(ins_id, lastname, firstname, city, country) VALUES(4, 'Saha', 'Sandip', 'Edmonton', 'CA');
scott1234519
MTUxOTAtc2NvdHQx



