#!/bin/sh
# wait-for-postgres.sh
status=1
while [ $status -gt 0 ]
do
  PG_URL="postgresql://$DB_USER:$DB_PASSWORD@$DB_HOST:$DB_PORT/$DB_NAME"
  # echo $PG_URL
  
  psql $PG_URL -c "\q" > /dev/null 2>&1
  status=$?
  sleep 1
  echo "db host : $DB_HOST"
  echo "db port : $DB_PORT" 
  echo "Postgres is unavailable - sleeping"
done
echo "Postgres is up - executing command"
