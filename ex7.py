#7
filmes = ["The Perks of Being a Wallflower", "IT"] #a
jogos = ["Undertale", "DOOM"]
livros = ["The Book Thief", "Toy Story"]
esporte = ["Baseball", "Volleyball", "Basketball", "Cricket"]

listas = [filmes, jogos, livros, esporte] #b
print("b) Lista de listas: ")
print(listas) 
print("-------------------------------------------------------------------------------------------------------")
print("c) Mostrar livro 0 (The Book Thief):") #c
print(listas[2][0])
print("-------------------------------------------------------------------------------------------------------")
del listas[3][1]#d
print("d) Deletar Volleyball de esportes e mostrar: ")
print(listas[3])
print("-------------------------------------------------------------------------------------------------------")
disciplinas = ["Português", "Matemática", "Inglês"]#e
listas.append(disciplinas)
print("e) Adicionar a lista disciplinas à lista de listas: ")
print(listas)
print("-------------------------------------------------------------------------------------------------------")
