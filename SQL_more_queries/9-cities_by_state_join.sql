-- a script that lists all cities contained in the
-- database hbtn_0d_usa.
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id
SELECT C.id, C.name, S.name 
FROM cities AS C
JOIN states AS S ON S.id = C.state_id
ORDER BY C.id;
