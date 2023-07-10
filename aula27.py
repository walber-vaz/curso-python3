# como o loop for funcionar no Python por baixo dos panos
# iterável -> iter() __iter__
# next()

nome = iter('Walber')  # __iter__()
# print(next(nome))  # __next__()
# print(next(nome))
# print(next(nome))
# print(next(nome))
# print(next(nome))
# print(next(nome))
# # print(next(nome))  # StopIteration


# fazendo o loop for funcionar por baixo dos panos
def _for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


_for([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
