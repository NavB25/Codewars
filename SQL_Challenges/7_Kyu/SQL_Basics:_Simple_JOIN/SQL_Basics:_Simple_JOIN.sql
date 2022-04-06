SELECT p.id,p.name,p.isbn,p.price,p.company_id,c.name as company_name FROM products p
JOIN companies c ON p.company_id = c.id
