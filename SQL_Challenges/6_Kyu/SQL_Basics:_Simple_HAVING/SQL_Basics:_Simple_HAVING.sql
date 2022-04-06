SELECT age,COUNT(age) as total_people FROM people
GROUP by age
HAVING COUNT(age) >= 10
