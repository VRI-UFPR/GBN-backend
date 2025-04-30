# import jwt
# import dotenv
# import os
# from datetime import datetime, timedelta

# dotenv.load_dotenv()

# # print the actual path of the folder


# with open("jwtRS256.key") as file:
#     SECRET_KEY = file.read()

# ALGORITHM = "RS256"

# # Create a payload with username and email
# payload = {
#     "username": "edsaibert",
#     "email": "eduardasaibert@ufpr.br",
#     "exp": datetime.utcnow() + timedelta(minutes=30)  # Token expires in 30 minutes
# }

# # Generate the token
# token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
# print(token)