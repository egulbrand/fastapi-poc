# fastapi-poc

To test:
Make sure to create a .env file with the values "DB_URL", "DB_URL" for connecting to MongoDB
Also add a value for "AUTH_SECRET_KEY" for the token creation

Then run the command
uvicorn main:app --reload --env-file .env
