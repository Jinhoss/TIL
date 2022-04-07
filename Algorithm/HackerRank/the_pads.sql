SELECT CONCAT(Name,'(', substring(occupation, 1, 1), ')')
FROM OCCUPATIONS
ORDER BY Name, substring(occupation, 1, 1);

SELECT CONCAT('There are a total of ', COUNT(occupation), ' ',LOWER(occupation), 's.')
FROM OCCUPATIONS
GROUP BY occupation
ORDER BY COUNT(occupation), occupation;
