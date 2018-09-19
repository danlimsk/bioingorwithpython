### Example 10-7: Simple SELECT statements in SQL

SELECT Name, Prototype FROM Enzyme LIMIT 5
SELECT * FROM Organism LIMIT 4 OFFSET 6
SELECT * FROM Organism
         ORDER BY Genus, Species, Subspecies
         LIMIT 4 OFFSET 6
SELECT COUNT(*) FROM Organism
