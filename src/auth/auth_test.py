import jwt
import dotenv
import os
from datetime import datetime, timedelta

dotenv.load_dotenv()

SECRET_KEY = os.getenv("PRIVATE_KEY") 
ALGORITHM = "HS256"

# Create a payload with username and email
payload = {
    "username": "john_doe",
    "email": "john@example.com",
    "exp": datetime.utcnow() + timedelta(minutes=30)  # Token expires in 30 minutes
}

# Generate the token
token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
print(token)
