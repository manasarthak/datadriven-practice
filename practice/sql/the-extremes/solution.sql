with helper as (select svc_name, sum(amount) as tot
from cloud_costs
where amount>0
group by svc_name),
ranked as (
select svc_name, tot,
row_number() over (order by tot desc) as rank_high,
row_number() over (order by tot) as rank_low
from helper
)

select svc_name, tot
from ranked
where rank_high<=3 or rank_low <=3
order by tot
