print('==========INTERSECCION DE CONJUNTO==========')
def interseccion():
    conjuntoA = {'Luis', 'Roy', 'Lucy', 'Bichenso', 'Ciro', 'Diego'}
    conjuntoB = {'Hafid', 'Frank', 'Alina', 'Oscar', 'Luis', 'Ciro'}
    conjuntoC = {'Nelsi', 'Melba', 'Sebastian', 'Susan', 'Ederson', 'Ciro'}

    interseccion_conjuntoAB = conjuntoA.intersection(conjuntoB)
    interseccion_conjuntoABC = interseccion_conjuntoAB.intersection(conjuntoC)

    print('la interseccion del conjuntoA, conjuntoB y el conjuntoC es: \n', interseccion_conjuntoABC)

interseccion()