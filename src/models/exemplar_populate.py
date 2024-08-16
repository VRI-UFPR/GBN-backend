from sqlmodel import Session
from src.models.exemplar import Exemplar
import os
import cv2

DATA_PATH = "/home/pedro/src/GBN/training-GBNv1/training-GBNv1"

def populate_gemeindebote(engine) -> None:
    with Session(engine) as session:
        exemplar = Exemplar(
            jornal_id=1,
            num_paginas=24,
            ano_publicacao=1936,
            idioma_predominante="Alemão",
            metadados="3850 x 5480",
        )
        session.add(exemplar)
    
        session.commit()

# def populate_jugendfreund(engine) -> None:
#     with Session(engine) as session:
#         for item in os.listdir(DATA_PATH + "/DerJugendfreund"):
#             imagem = cv2.imread(DATA_PATH + "/DerJugendfreund/" + item)
#             altura, largura, _ = imagem.shape
#             ano = item.split("_")[1]
#             mes = item.split("_")[2]
#             last_month = 0
#             last_year = 0

#             if ano != last_year and mes != last_month:
#                 last_month = mes
#                 last_year = ano

#                 exemplar = Exemplar(
#                     jornal_id=2,
#                     num_paginas=18,
#                     ano_publicacao=ano,
#                     idioma_predominante="Alemão",
#                     metadados=f"{altura} x {largura}",
#                 )

#                 session.add(exemplar)
#     session.commit()

# def populate_pioner(engine) -> None:
#     with Session(engine) as session:
#         for item in os.listdir(DATA_PATH + "/DerPioner"):
#             ano = item.split("_")[1][:5]
#             mes = item.split("_")[1][5:10]
#             last_month = 0
#             last_year = 0
#             if ano != last_year and mes != last_month:
#                 last_month = mes
#                 last_year = ano
#                 exemplar = Exemplar(
#                     jornal_id=3,
#                     num_paginas=22,
#                     ano_publicacao=ano,
#                     idioma_predominante="Alemão/Português",
#                     metadados="7100 x 10590",
#                 )
#                 session.add(exemplar)
#     session.commit()


# def populate_sandwirt(engine) -> None:
#     with Session(engine) as session:
#         for item in os.listdir(DATA_PATH + "/DerSandwirt"):
#             exemplar = Exemplar(
#                 jornal_id=4,
#                 num_paginas=22,
#                 ano_publicacao=item.split("_")[1],
#                 idioma_predominante="Alemão",
#                 metadados="4250 x 6020",
#             )
#             session.add(exemplar)
#     session.commit()

# def populate_kirchenblatt(engine) -> None:
#     with Session(engine) as session:
#         for item in os.listdir(DATA_PATH + "/EvangelisschLutherischesKirchenblatt"):
#             exemplar = Exemplar(
#                 jornal_id=5,
#                 num_paginas=22,
#                 ano_publicacao=item.split("_")[1][:5],
#                 idioma_predominante="Alemão",
#                 metadados="2590 x 3690",
#             )
#             session.add(exemplar)
#     session.commit()

# def populate_kolonie_zeitung(engine) -> None:
#     with Session(engine) as session:
#         for item in os.listdir(DATA_PATH + "/KolonieZeitung"):
#             imagem = cv2.imread(DATA_PATH + "/KolonieZeitung/" + item)
#             altura, largura, _ = imagem.shape
#             exemplar = Exemplar(
#                 jornal_id=6,
#                 num_paginas=16,
#                 ano_publicacao=item[7:12],
#                 idioma_predominante="Alemão",
#                 metadados=f"{altura} x {largura}",
#             )
#             session.add(exemplar)
#     session.commit()

# def populate_gemeindeblatt(engine) -> None:
#     with Session(engine) as session:
#         for item in os.listdir(DATA_PATH + "/Gemeindeblatt"):
#             exemplar = Exemplar(
#                 jornal_id=7,
#                 num_paginas=16,
#                 ano_publicacao=item.split("_")[1],
#                 idioma_predominante="Alemão",
#                 metadados="2590 x 3690",
#             )
#             session.add(exemplar)
#     session.commit()

# def populate_Heimatbote(engine) -> None
#     with Session(engine) as session:
#         exemplar = Exemplar(
#             jornal_id=8,
#             num_paginas=14,
#             ano_publicacao=1936,
#             idioma_predominante="Alemão",
#             metadados="3850 x 5480",
#         )
#         session.add(exemplar)
#         session.commit()

# def populate_exemplar(engine) -> None:
#     populate_gemeindebote(engine)
#     populate_jugendfreund(engine)
#     populate_pioner(engine)
#     populate_sandwirt(engine)
#     populate_kirchenblatt(engine)
#     populate_kolonie_zeitung(engine)
#     populate_gemeindeblatt(engine)