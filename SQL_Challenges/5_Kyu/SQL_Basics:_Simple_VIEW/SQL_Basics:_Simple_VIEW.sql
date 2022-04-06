CREATE VIEW MEMBERS_APPROVED_FOR_VOUCHER AS
SELECT m.id,m.name,m.email,SUM(p.price) as total_spending FROM sales s
JOIN departments d ON s.department_id = d.id
JOIN products p ON s.product_id = p.id
JOIN members m ON s.member_id = m.id
WHERE department_id IN (SELECT d.id FROM sales s
                        JOIN departments d ON s.department_id = d.id
                        JOIN products p ON s.product_id = p.id
                        GROUP BY d.id
                        HAVING SUM(p.price) > 10000) 
GROUP BY m.id
HAVING SUM(p.price) >= 1000
ORDER BY m.id ASC
