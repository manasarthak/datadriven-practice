select count(*) as total_commits, count(distinct(lower(trim(author)))) as distinct_authors
from repo_commits
