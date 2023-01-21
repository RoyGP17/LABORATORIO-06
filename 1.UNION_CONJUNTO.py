print('==========UNION DE CONJUNTO==========')
def union():
    conjuntoA = {'Luis', 'Roy', 'Lucy', 'Bichenso', 'Ciro', 'Diego'}
    conjuntoB = {'Hafid', 'Frank', 'Alina', 'Oscar', 'Luis', 'Ciro'}
    conjuntoC = {'Nelsi', 'Melba', 'Sebastian', 'Susan', 'Ederson'}

    union_conjuntoAB = conjuntoA.union(conjuntoB)
    union_conjuntoABC = union_conjuntoAB.union(conjuntoC)

    print('la union del conjuntoA, conjuntoB y el conjuntoC es: \n', union_conjuntoABC)

union()