SELECT c.customer_id, c.email, COUNT(p.payment_id) as payments_count, CAST(SUM(p.amount) AS FLOAT) as total_amount FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
GROUP BY c.customer_id
ORDER BY SUM(p.amount) DESC
LIMIT 10
