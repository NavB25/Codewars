SELECT CAST(created_at AS DATE) as day, description, COUNT(*) FROM events
GROUP BY day,description,name
HAVING name = 'trained'
