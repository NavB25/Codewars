SELECT pokemon_name, (str*multiplier) modifiedStrength, element FROM pokemon
JOIN multipliers ON multipliers.id=pokemon.element_id
WHERE (str*multiplier) >= 40
ORDER BY (str*multiplier) DESC
