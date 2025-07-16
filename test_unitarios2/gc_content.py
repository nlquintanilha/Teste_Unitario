def calcular_gc_content(seq):
    
    """
    Retorna a porcentagem de conteúdo GC na sequência de DNA.
    """

    seq = seq.upper()  # Garante que a sequência esteja em maiúsculas
    total = len(seq)
    if total == 0:
        return 0.0
    
    gc_count = seq.count('G') + seq.count('C')
    return (gc_count / total) * 100




