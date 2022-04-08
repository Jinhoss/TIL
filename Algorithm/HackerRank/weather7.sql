select distinct city from station
where right(city, 1) in ('A', 'E', 'I', 'O', 'U')