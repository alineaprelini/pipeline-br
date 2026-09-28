from ingestion.client import buscar_dados


def test_buscar_dados_ibge():
    dados = buscar_dados("https://servicodados.ibge.gov.br/api/v1/localidades/estados")
    assert len(dados) == 27