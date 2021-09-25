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
