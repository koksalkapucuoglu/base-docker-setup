# Base Docker Setup for Django with Celery

This project is a Django application integrated with Celery for task management. It includes:
- A MongoDB database
- Redis for Celery task queue(trigger task with admin panel action)
- Docker support for containerized deployment

## Running the Project

### Using Docker
1. Rename `.env_comp` to `.env` and configure the environment variables.
2. Build and start the containers:
   ```bash
   make build
   make run
   ```
3. Access the application at `http://localhost:8000`.
4. Migrate after to create MongoDB user:
    ```bash
   make migrate
   ```

### Creating a MongoDB User
1. Enter the MongoDB container:
   ```bash
   docker exec -it mongo_db_base mongosh
   ```
2. Switch to the admin database:
   ```bash
   use admin
   ```
3. Create a new user with the required roles():
   ```bash
   db.createUser({
       user: "root",
       pwd: "example_password",
       roles: [
           { role: "root", db: "admin" }
       ]
   })
   ```
4. Exit the MongoDB shell:
   ```bash
   exit
   ```
5. Check connection on MongoDB Compass or any MongoDB Viewer
  - connect **mongodb://root:example_password@localhost:27018/mydatabase?authSource=admin**
  
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
3. Start the MongoDB and Redis services manually.
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
- Ensure the database and Redis configurations match your environment if you are working with a virtual environment.
- Use the Django admin panel to manage `NumberPair` objects and trigger Celery tasks.
