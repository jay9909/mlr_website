# Parse Args
declare -A flags
declare -A booleans
args=()

while [ "$1" ];
do
    arg=$1
    if [ "${1:0:1}" == "-" ]
    then
      shift
      rev=$(echo "$arg" | rev)
      if [ -z "$1" ] || [ "${1:0:1}" == "-" ] || [ "${rev:0:1}" == ":" ]
      then
        bool=$(echo ${arg:1} | sed s/://g)
        booleans[$bool]=true
      else
        value=$1
        flags[${arg:1}]=$value
        shift
    fi
    else
      args+=("$arg")
      shift
   fi
done

export GOOGLE_APPLICATION_CREDENTIALS="dev_secret_manager_auth_key.json"

# Serving Env Variables

# Database Connection Env Variables
export DB_SOCKET_DIR=cloudsql/major-league-redditball-327:us-east4:redditball-db
export CLOUD_SQL_CONNECTION_NAME=major-league-redditball-327:us-east4:redditball-db
export DB_USER=devserver
export FLASK_SECRET_KEY_SECRET=projects/822174088809/secrets/flask_secret_key/versions/latest
export DB_PWD_SECRET=projects/822174088809/secrets/redditball-sql-instance-devserver-password/versions/latest
export DB_NAME=redditball_dev

# Discord App Env Variables
export DISCORD_APP_NAME=mlr_website_dev
export DISCORD_CLIENT_ID_SECRET=projects/822174088809/secrets/discord-client-id/versions/latest
export DISCORD_APP_PUBLIC_KEY=fb10416585e9d29491ac037e281d1fec798ba59d0ae5663fd2b994fbb19df358
export DISCORD_CLIENT_SECRET_SECRET=projects/822174088809/secrets/discord-client-secret/versions/latest


# Run the dev server if boolean flag "-s" was passed in.
if [ "${booleans['s']}" ] ; then
  export FLASK_APP=wsgi.py
  export FLASK_ENV=development
  export HOST=0.0.0.0
  export PORT=8080

  flask run

# Run a python file directly, provided as an argument to "-t"
elif [ "${flags['t']}" ] ; then
  python3 "${flags['t']}"
fi
