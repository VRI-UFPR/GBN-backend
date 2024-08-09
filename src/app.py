from models.jornal import Jornal
from models.exemplar import Exemplar
from models.pagina import Pagina
from models.texto_ocr import TextoOcr
from models.texto_correcao_manual import TextoCorrecaoManual

from database.database import engine, create_db_and_tables

def main():
    create_db_and_tables()
    print("Tabelas criadas")

if __name__ == "__main__":
    main()