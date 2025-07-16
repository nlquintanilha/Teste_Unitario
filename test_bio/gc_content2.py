def calcular_gc_content(seq):
    seq = seq.upper()  #padroniza em maiúscula
    if len(seq) == 0:
        raise ValueError("A sequencia está vazia.")
    
    # Verifica se só há caracteres válidos

    for base in seq: 
        if base not in "ATGC":
            raise ValueError(f"Caractere inválido encontrado: {base}")
        
    gc = seq.count('G')  + seq.count('C')
    return (gc / len(seq)) * 100