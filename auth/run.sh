while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    echo "Waiting for PostgreSql to start..."
    sleep 1
done

echo "Migrate..."
alembic upgrade head

echo "Run server..."
uvicorn main:app --host 0.0.0.0 --port 8000