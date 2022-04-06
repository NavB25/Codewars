SELECT DATE(created_at) as date, COUNT(*) as count, CAST(SUM(COUNT(*)) OVER (ORDER BY DATE(created_at)) as int) as total FROM posts
GROUP BY date
