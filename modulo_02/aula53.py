# generator function
def gen():
    for n in range(1, 10):
        yield n


g = gen()

for v in g:
    print(v)
