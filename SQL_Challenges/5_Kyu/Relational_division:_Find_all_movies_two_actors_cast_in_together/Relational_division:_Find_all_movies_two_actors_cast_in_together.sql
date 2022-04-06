SELECT f.title FROM film f
JOIN film_actor fa ON f.film_id=fa.film_id
JOIN actor a ON fa.actor_id=a.actor_id
WHERE a.actor_id = 105 OR a.actor_id = 122
GROUP BY f.title
HAVING COUNT(f.film_id) > 1
ORDER BY f.title ASC
