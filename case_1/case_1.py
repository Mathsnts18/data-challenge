# %%

import sqlalchemy
import mysql.connector
import pandas as pd

eng = sqlalchemy.create_engine('mysql+mysqlconnector://looqbox-challenge:looq-challenge@35.199.115.174/looqbox-challenge')

#%%
def retrieve_data(product_code:int=None, store_code:int=None, date:list=None)->pd.DataFrame:
    """ Docstring criada com apoio de IA
    Busca dados de vendas de produtos com base nos filtros fornecidos.

    A função constrói uma consulta SQL dinamicamente conforme os parâmetros
    passados e retorna os resultados em um DataFrame do Pandas.

    Args:
        product_code (int, optional): Código identificador do produto.
            Defaults to None.
        store_code (int, optional): Código identificador da loja.
            Defaults to None.
        date (list, optional): Lista de datas (formato ISO)
            para filtrar as vendas (`IN`). Defaults to None. Ex.: '2019-01-01'

    Returns:
        pd.DataFrame: DataFrame contendo todas as colunas da tabela
        `data_product_sales` que atendem aos critérios de filtragem.
    """

    params = []

    query = """
    SELECT *
    FROM data_product_sales t1
    WHERE 1=1
    """

    if product_code:
        query += " AND t1.PRODUCT_CODE = %s"
        params.append(product_code)

    if store_code:
        query += " AND t1.STORE_CODE = %s"
        params.append(store_code)

    if date:
        data_placeholder = ", ".join(["%s"] * len(date)) #AI
        query += f" AND t1.DATE IN ({data_placeholder})" 
        params.extend(date)

    df = pd.read_sql(query, eng, params=tuple(params))
    return df