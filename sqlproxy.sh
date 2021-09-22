export DB_SOCKET_DIR=cloudsql
cloud_sql_proxy -credential_file=cloud_sql_proxy_auth_key.json -dir=$DB_SOCKET_DIR -instances=major-league-redditball-327:us-east4:redditball-db

