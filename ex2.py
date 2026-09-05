titulo = "Cálculo no carrinho de compras"
descricao = "Um cliente comprou dois lanches, cada um por: "
cont = " e recebeu um desconto de: "
pergunta = "Quanto ele gastou?"
resposta = "Ele gastou: "
preco = 22.00
quantidade = 2
desconto = 5.00

subtotal = preco * quantidade
valor_final = subtotal - desconto

# .2f formata os valores com 2 casas decimais
print(f"""
{titulo}
{descricao}R$ {preco:.2f}{cont}R$ {desconto:.2f}
{pergunta}
{resposta}R$ {valor_final:.2f}
""")