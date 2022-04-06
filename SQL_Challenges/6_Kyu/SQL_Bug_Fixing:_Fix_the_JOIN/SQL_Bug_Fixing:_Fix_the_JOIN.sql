SELECT 
  j.job_title,
  CAST(CAST(SUM(j.salary) / COUNT(p) AS decimal(13,2)) AS float) as average_salary,
  COUNT(p) as total_people,
  CAST(CAST(SUM(j.salary) AS decimal(13,2)) AS float) as total_salary 
  FROM people p
    JOIN job j ON p.id=j.people_id
  GROUP BY j.job_title
  ORDER BY average_salary DESC
