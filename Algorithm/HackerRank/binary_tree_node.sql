SELECT N, (
CASE WHEN P IS NULL then 'Root'
WHEN N NOT IN (SELECT DISTINCT P FROM BST WHERE P IS NOT NULL) THEN 'Leaf'
ELSE 'Inner' end
) as nodeType
FROM BST
ORDER BY N