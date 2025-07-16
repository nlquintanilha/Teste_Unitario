def traduzir_codon(codon):
    codon = codon.upper()
    tabela = {
        'ATG':'Met',
        'TGG': 'Trp',
        'TAA': 'Stop',
        'TAG': 'Stop',
        'TGA': 'Stop'
    }

    return tabela.get(codon,'X')

