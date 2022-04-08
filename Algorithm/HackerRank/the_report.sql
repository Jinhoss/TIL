SELECT
    CASE
        WHEN g.grade < 8 then NULL
        ELSE s.name
    end,
    g.grade,
    s.marks

FROM students as s join grades as g on s.marks between g.min_mark and g.max_mark
ORDER BY
    g.grade desc,
    s.name,
    s.marks
