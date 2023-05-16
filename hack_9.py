"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():

    result = [1,2,3]
    salida = []
    i = 0
    while i < len(result):
        salida.append(result[i])
        if i < len(result):
            salida.append('@')
        i += 1
    print(salida)        

    return salida