#!/bin/sh

set -e

host="$POSTGRES_HOST"
port="$POSTGRES_PORT"

echo "Waiting for database at $host:$port..."

while ! nc -z "$host" "$port"; do
  sleep 1
done

echo "Database is ready!"

exec "$@"
