def inserir(*args):
    print(args)
    for a in args:
        print(a)

def inserirChave(**kwargs):
    for key, value in kwargs.items():
        print(key+': '+value)
        #print(nome, idade)
    print(kwargs)


#inserir('Fabio', 29, 'Railma', 29)

inserirChave(nome='fabio', idade='29')

