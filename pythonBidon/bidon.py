class Bidon:
    zaz = 'je suis un pro du python'

    def __init__(self, txt, num=42,  *args, **kwargs):
        self.txt = txt
        self.num = num
        for key, value in kwargs.items():
            setattr(self, key, value)
    pass


def var2listsort(*args):
    arr = []
    largs = len(args)
    if largs > 1:
        arr.append(args[0])
        for v in range(1, largs):
            i = 0
            l = len(arr)
            while i != l:
                m = (i + l) // 2
                if args[v] <= arr[m]:
                    l = m
                else:
                    i = m+1
            arr.insert(i, args[v])
    return arr
