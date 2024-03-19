# Escreva um programa na linguagem de programação de sua preferência que receba um byte e calcule o seu código de Hamming. 
# Evolua o programa anterior, simulando falhas e encontrando formas de correção das falhas.

#Cálculo de bits de paridade com base nos dados
def calcular_paridade(data):
    paridade_bits = [0] * (len(data) + 1) 
    for i in range(len(data)): 
        for j in range(len(paridade_bits)):
            if (i+1) & (1 << j):  
                paridade_bits[j] ^= data[i]  
    return paridade_bits

#Adiciona os bits de paridade aos dados originais
def add_paridade(data):
    paridade_bits = calcular_paridade(data)
    for i in range(len(paridade_bits) - 1, -1, -1):
        data.insert(2**i - 1, paridade_bits[i])
    return data

#Cria uma falha invertendo um bit aleatório
def simular_erro(data):
    import random
    bit_to_flip = random.randint(0, len(data) - 1)
    data[bit_to_flip] ^= 1  # Inverte o bit
    return data

#Corrige o problema
def corrigir_erro(data):
    paridade_bits = calcular_paridade(data)
    error_index = 0
    for i in range(len(paridade_bits)):
        error_index += paridade_bits[i] * (2**i)
    if error_index != 0:  
        data[error_index - 1] ^= 1  
    return data

#Função Principal
def main():
    byte = int(input("Digite um byte (0-255): "))
    byte_bits = [int(bit) for bit in bin(byte)[2:].zfill(8)] 
    codigo_hamming = add_paridade(byte_bits)
    print("Byte com código de Hamming:", codigo_hamming)
    
    codigo_hamming_com_erro = simular_erro(codigo_hamming)
    print("Byte com erro:", codigo_hamming_com_erro)
    
    byte_corrigido = corrigir_erro(codigo_hamming_com_erro)
    print("Byte corrigido:", byte_corrigido)

if __name__ == "__main__":
    main()
