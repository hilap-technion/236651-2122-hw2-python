import ast
import itertools
from functools import partial
import AstMakers

def nodeHeight(node):
    if type(node) == ast.Constant or type(node) == ast.Name:
        return 0
    maxChildHeight = max((nodeHeight(child) for child in ast.iter_child_nodes(node)),
                   default = 0)
    return 1 + maxChildHeight

def Enumerator(constants: list[int], variables: list[str], contexts: list[dict]):
    functionsByArity = [
        [partial(AstMakers.makeIntVariable, name=varname) for varname in variables] + \
        [partial(AstMakers.makeIntLiteral, v=constval) for constval in constants], #arity 0
        [AstMakers.makeUminus], # arity 1
        [AstMakers.makeAddition,AstMakers.makeSubtraction,AstMakers.makeMult,AstMakers.makeFloorDiv,AstMakers.makeMod] # arity 2
    ]
    previousLevelPrograms = []
    currentLevelPrograms = []
    arity = 0
    height = 0
    while(True):
        for f in functionsByArity[arity]:
            children = [[]]
            if arity == 0: pass # [[]] is good
            elif arity == 1:
                children = map(lambda p: [p], filter(lambda p: nodeHeight(p) == height - 1,previousLevelPrograms))
            else:
                children = filter(lambda ps: any(nodeHeight(p) == height - 1 for p in ps),
                       itertools.product(previousLevelPrograms,previousLevelPrograms))
            for cs in children:
                p = f(children=cs,contexts=contexts)
                currentLevelPrograms.append(p)
                try:
                    yield p
                except GeneratorExit:
                    return
        arity += 1
        if (arity == 1 or arity > 2):
            arity = 1
            previousLevelPrograms += currentLevelPrograms
            currentLevelPrograms = []
            height += 1
