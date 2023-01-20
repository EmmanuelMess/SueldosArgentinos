#!/bin/sh

# Start the first process
python /app/manage.py livereload &

# Start the second process
python /app/manage.py runserver 0.0.0.0:8000 &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?
