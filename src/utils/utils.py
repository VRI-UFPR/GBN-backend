import dotenv
import os

dotenv.load_dotenv()

def get_prox_pagina():
    with open(os.getenv("ID_FILE_LOCATION"), 'r') as file:
        prox_pagina = file.read()
    
    with open(os.getenv("ID_FILE_LOCATION"), 'w') as file:
        if int(prox_pagina) < 18:
            prox_pagina = str(int(prox_pagina) + 1)
        else:
            prox_pagina = "0"

        with open(os.getenv("ID_FILE_LOCATION"), 'w') as file:
            file.write(prox_pagina)

    return prox_pagina