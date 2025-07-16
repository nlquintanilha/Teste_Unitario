def contar_nucleotidos(seq):
    
    """
    contar quantas vezes cada nucleotídeo aparece na sequência de DNA. 
    """

    contagem = {
        'A': seq.upper().count('A'),
        'T': seq.upper().count('T'),        
        'C': seq.upper().count('C'),
        'G': seq.upper().count('G')

        #seq.upper() garante que a sequência estará toda em maiúsculas (evita erro se o usuário digitar em minúsculo).

        #.count('A') conta quantas vezes o caractere 'A' aparece.

    }   
    return contagem
