with helper as (
select upper(method) as method,latency
from api_calls
where latency is not null),
helper2 as (
select method,latency,
        row_number() over( partition by method order by latency) as rnk
from helper)
select method,round(avg(latency)::numeric,2) as fastest_five_avg
from helper2
where rnk<6
group by method
