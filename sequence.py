from graphviz import Digraph

def prefix(s, *_, **kwargs):
    proper = kwargs.get('proper', True)

    n = len(s)
    if not proper:
        n += 1

    for l in range(n):
        yield s[:l]

def suffix(s, *_, **kwargs):
    proper = kwargs.get('proper', True)

    n = len(s)
    if not proper:
        n += 1

    yield ''
    for l in range(1, n):
        yield s[-l:]

def gen_graph(*bins, **kwargs):
    fmt = kwargs.get('format', 'svg')

    pset = dict()
    nodes = dict()
    idx = 0
    for binary in bins:
        for pfx in  prefix(binary):
            if pfx not in pset:
                nodes[idx] = pfx
                pset[pfx] = idx
                idx += 1

    automaton = Digraph(engine='dot', format=fmt)

    for idx, pfx in nodes.items():
        automaton.node(str(idx), pfx or 'x')

    for x, pfx in nodes.items():
        pfx = nodes[x]
        c0 = pfx + '0'
        c1 = pfx + '1'

        out0 = int(c0 in bins)
        out1 = int(c1 in bins)

        z0 = None
        for p in suffix(c0, proper=False):
            if p in pset:
                z0 = pset[p]

        automaton.edge(str(x), str(z0), label=f'0/{out0}')

        z1 = None
        for p in suffix(c1, proper=False):
            if p in pset:
                z1 = pset[p]

        automaton.edge(str(x), str(z1), label=f'1/{out1}')

    return automaton.pipe().decode('utf-8')

