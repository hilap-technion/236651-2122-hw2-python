import ast

def makeIntLiteral(v: int, children: list, contexts: list):
    lit = ast.Constant(value=v)
    lit.values = [v for ctx in contexts]
    return lit

def makeIntVariable(name: str, children:list, contexts: list):
    var = ast.Name(id=name, ctx=ast.Load())
    var.values = [ctx[name] for ctx in contexts]
    return var

def makeAddition(children: list, contexts: list):
    add = ast.BinOp(children[0],ast.Add(),children[1])
    add.values = [sum(cs) for cs in zip(children[0].values,children[1].values)]
    return add

def makeSubtraction(children: list, contexts: list):
    sub = ast.BinOp(children[0], ast.Sub(), children[1])
    sub.values = [cs[0] - cs[1] for cs in zip(children[0].values,children[1].values)]
    return sub

def makeUminus(children: list, contexts: list):
    uminus = ast.UnaryOp(ast.USub(),children[0])
    uminus.values = [-x for x in children[0].values]
    return uminus

def makeMult(children: list, contexts: list):
    mult = ast.BinOp(children[0], ast.Mult(), children[1])
    mult.values = [cs[0] * cs[1] for cs in zip(children[0].values,children[1].values)]
    return mult

def makeFloorDiv(children: list, contexts: list):
    div = ast.BinOp(children[0], ast.FloorDiv(), children[1])
    div.values = [cs[0] // cs[1] for cs in zip(children[0].values,children[1].values)]
    return div

def makeMod(children: list, contexts: list):
    mod = ast.BinOp(children[0], ast.Mod(), children[1])
    mod.values = [cs[0] % cs[1] for cs in zip(children[0].values,children[1].values)]
    return mod
