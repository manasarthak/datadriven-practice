select log_id, lower(env_name)
from deploy_logs
where lower(status)='failed'
