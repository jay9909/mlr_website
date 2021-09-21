export DB_SOCKET_DIR=cloudsql
cloud_sql_proxy -dir=$DB_SOCKET_DIR -instances=major-league-redditball-327:us-east4:redditball-db

