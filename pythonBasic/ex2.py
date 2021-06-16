
def g(l):
    for item in l:
        yield item
    while True:
        yield None


def zip_longest(*lists):
    gens = [g(l) for l in lists]
    for _ in range(max(map(len, lists))):
        yield tuple(next(g) for g in gens)


def make_pair(a1, a2):
    return list(zip_longest(a1, a2))
