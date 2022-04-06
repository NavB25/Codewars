SELECT
  CASE
    WHEN SUM(number1) % 2 != 0
      THEN min(number1)
    ELSE max(number1)
  END AS number1,
  CASE
    WHEN SUM(number2) % 2 != 0 
      THEN min(number2)
    ELSE max(number2)
  END AS number2
FROM numbers
