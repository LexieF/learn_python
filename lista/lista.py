class MinhaLista(list):
    def append(self, *args):
        self.extend(args)

ml = MinhaLista()
ml.append(1,2,3,4,5,6,7,8,9)
print(ml)

