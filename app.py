## entrada
Aparelho_el = input("Insira o nome do aparelho: ")
Unidade_KW = float(input("Insira a potência do aparelho em Wats: "))
usoDiario = float(input("Insira o uso diário do aparelho em horas (apenas números inteiros): "))

## processamento
consumoMensal = (Unidade_KW * usoDiario * 30) / 1000
valorMensal = consumoMensal * 0.7

## saída

print("O aparelho:", Aparelho_el)
print("Consome:",round(consumoMensal, 0),"W por mês.")
print("O valor será de R$",round(valorMensal, 1),"ao final do mês.")
print("Obrigado por usar a calculadora.")

