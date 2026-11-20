with helper as (
select user_id, count(session_id) as session_count
from user_sessions
group by user_id
)
select username, session_count
from users join helper
on users.user_id=helper.user_id
where session_count>=3
order by session_count desc
