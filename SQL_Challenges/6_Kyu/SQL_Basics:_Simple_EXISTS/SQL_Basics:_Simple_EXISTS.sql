SELECT d.id, d.name FROM departments d
JOIN sales s ON d.id = s.department_id
WHERE EXISTS (SELECT price FROM departments WHERE price > 98)
GROUP BY d.id
ORDER by d.id ASC
