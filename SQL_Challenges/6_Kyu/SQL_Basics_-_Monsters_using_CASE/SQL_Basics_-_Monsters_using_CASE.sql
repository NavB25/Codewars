SELECT t.id,heads,b.legs,arms,b.tails,
  CASE 
    WHEN heads > arms OR b.tails > b.legs OR heads > arms AND b.tails > b.legs THEN 'BEAST'
    ELSE 'WEIRDO'
  END AS species 
FROM top_half t
JOIN bottom_half b ON t.id = b.id
ORDER BY species
