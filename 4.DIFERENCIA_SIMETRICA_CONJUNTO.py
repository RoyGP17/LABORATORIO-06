print('==========DIFERENCIA SIMETRICA DE CONJUNTO==========')
def union():
    conjuntoA = {'Luis', 'Roy', 'Lucy', 'Bichenso', 'Ciro', 'Susan'}
    conjuntoB = {'Hafid', 'Susan', 'Alina', 'Oscar', 'Bichenso', 'Ciro'}

    diferencia_simetrica_conjuntoAB = conjuntoA.symmetric_difference(conjuntoB)

    print('la diferencia simetrica del conjuntoA, conjuntoB y el conjuntoC es: \n', diferencia_simetrica_conjuntoAB)

union()