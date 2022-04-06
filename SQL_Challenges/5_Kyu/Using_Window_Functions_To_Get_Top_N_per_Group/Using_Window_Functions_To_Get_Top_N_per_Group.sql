SELECT category_id, category, title, views, post_id FROM   
  
    (SELECT c.id as category_id, c.category, p.title, 
  
    SUM(p.views) OVER(PARTITION BY p.title) as views,
  
    p.id as post_id,
  
    rank() OVER(PARTITION BY c.category ORDER BY views DESC) as view_rnk,
     
    rank() OVER(PARTITION BY views ORDER BY p.id ASC) as post_rnk
  
    FROM categories c
  
    LEFT JOIN posts p ON c.id = p.category_id
  
    ORDER BY c.category ASC, views DESC, p.id ASC) x
  
WHERE x.view_rnk < 3 AND x.post_rnk !=3
