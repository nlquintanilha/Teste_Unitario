from gc_content2 import calcular_gc_content

def main():
    print("Cálculo de GC Content")
    seq = input("Digite uma sequencia de DNA (ex: ATGCGC):")

    try:
        gc = calcular_gc_content(seq)
        print(f"O GC content da sequência é: {gc:.2f}%")
    except ValueError as e:
        print(f"Erro:{e}")

if __name__ == "__main__":
    main ()   