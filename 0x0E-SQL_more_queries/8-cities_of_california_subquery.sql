-- Script that lists all the cities of California in the database hbtn_0d_usa
-- The states table contains only one record where name = California
-- Results must be sorted in ascending order by cities.id


SELECT id, name FROM cities
WHERE states_id = (SELECT id FROM states WHERE name = 'california')
ORDER BY id ASC;
