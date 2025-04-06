#!/bin/sh

set -e

host="$MONGO_HOST"
port="$MONGO_PORT"

echo "Waiting for MongoDB at $host:$port..."

while ! nc -z "$host" "$port"; do
  sleep 1
done

echo "MongoDB is ready!"

exec "$@"
