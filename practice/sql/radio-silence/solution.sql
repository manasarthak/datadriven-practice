with gaps as (
              select repo_name,
              julianday(commit_at)-julianday(lag(commit_at) over
                        (partition by repo_name order by commit_at))
              as gap_days
              from repo_commits),
              repos as (
                        select repo_name,
                                max(gap_days) as longest_silence,
                                count(gap_days) as gap_count
                        from gaps
                        group by repo_name
                        having count(gap_days)>31
                        )
select row_number() over (order by longest_silence desc) as silence_rank,
      repo_name,
      longest_silence 
from repos
order by longest_silence desc;
