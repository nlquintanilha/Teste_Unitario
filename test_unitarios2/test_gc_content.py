from gc_content import calcular_gc_content

def test_calcular_gc_content():
    seq = "AGCTATAG"
    resultado = calcular_gc_content(seq)
    assert round(resultado, 2) == 37.5
