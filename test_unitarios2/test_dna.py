from dna import contar_nucleotidos

def test_contar_nucleotidos():
    seq = "ATCGATCG"
    resultado = contar_nucleotidos(seq)
    assert resultado == {'A': 2, 'T': 2, 'C': 2, 'G': 2}

    