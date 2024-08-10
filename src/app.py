from models.jornal import Jornal
from models.exemplar import Exemplar
from models.pagina import Pagina
from models.texto_ocr import TextoOcr
from models.texto_correcao_manual import TextoCorrecaoManual

from database.database import get_engine, create_db_and_tables

def main():
    try:
        engine = get_engine()
        create_db_and_tables(engine=engine)
        print("Tabelas criadas")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()