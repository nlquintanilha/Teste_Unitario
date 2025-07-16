import pytest
from gc_content2 import calcular_gc_content

def test_gc_content_valido():
    seq = "AGCTATAG"
    resultado = calcular_gc_content(seq)
    assert round(resultado, 2) == 37.5

def test_gc_content_vazio():
    with pytest.raises(ValueError):
         calcular_gc_content("")

def test_gc_content_caractere_invalido():
    with pytest.raises(ValueError):
         calcular_gc_content("ATXBGC")