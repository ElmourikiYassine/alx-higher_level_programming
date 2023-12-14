-- Select cities of California using JOIN
SELECT cities.id AS id, cities.name AS name, states.name AS name
FROM cities JOIN states.id = cities.state_id
ORDER BY id ASC;
