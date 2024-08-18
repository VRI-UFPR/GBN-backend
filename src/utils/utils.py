import dotenv
import os

dotenv.load_dotenv()

def get_prox_pagina():
    with open(os.getenv("ID_FILE_LOCATION"), 'r') as file:
        prox_pagina = file.read()
    
    with open(os.getenv("ID_FILE_LOCATION"), 'w') as file:
        file.write(str(int(prox_pagina) + 1))

    return prox_pagina