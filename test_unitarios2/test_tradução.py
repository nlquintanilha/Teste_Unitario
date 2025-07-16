from traducao import traduzir_codon

def test_traduzir_codon():
    assert traduzir_codon('ATG') =='Met'
    assert traduzir_codon('TGA') == 'Stop'
    assert traduzir_codon('CCC') == 'X'

    

