print('==========DIFERENCIA DE CONJUNTO==========')
def diferencia():
    conjuntoA = {'Luis', 'Roy', 'Lucy', 'Bichenso', 'Ciro', 'Diego'}
    conjuntoB = {'Hafid', 'Frank', 'Alina', 'Oscar', 'Luis', 'Ciro'}

    diferencia_conjuntoAB = conjuntoA.difference(conjuntoB)
    diferencia_conjuntoBA = conjuntoB.difference(conjuntoA)

    print('la diferencia del conjuntoA y el conjuntoB es: \n', diferencia_conjuntoAB)
    print()
    print('la diferencia del conjuntoB y el conjuntoA es: \n', diferencia_conjuntoBA)

diferencia()