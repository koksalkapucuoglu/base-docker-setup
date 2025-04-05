# Base Docker Setup for Django with Celery

This project is a Django application integrated with Celery for task management. It includes:
- A PostgreSQL database
- Redis for Celery task queue(trigger task with admin panel action)
- Docker support for containerized deployment

## Running the Project

### Using Docker
1. Rename .env_comp with .env
2. Build and start the containers:
   ```bash
   make build
   make migrate
   make run
   ```
3. Access the application at `http://localhost:8000`.

### Using a Virtual Environment
1. Create and activate a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate  
   # On Windows: .\env\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the PostgreSQL and Redis services manually.
4. Start the Celery worker:
   ```bash
   celery -A core worker -l INFO
   ```
5. Run the Django development server:
   ```bash
   python manage.py runserver
   ```
6. Access the application at `http://localhost:8000`.

## Notes
- Ensure the database and Redis configurations match your environment if you are working with virtual enviroment.
- Use the Django admin panel to manage `NumberPair` objects and trigger Celery tasks.
