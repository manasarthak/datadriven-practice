with helper as(select tbl_name,
        sum(case when passed then 0 else 1 end) as failed_checks,
        count(distinct case when not passed then rule end) as distinct_rules,
        avg(fail_pct) as avg_fail_pct
from dq_checks
group by tbl_name)
select tbl_name,failed_checks,distinct_rules, avg_fail_pct
from helper 
where avg_fail_pct>30
order by avg_fail_pct desc
