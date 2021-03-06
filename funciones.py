from calendar import c
import random

def encontrar_menores(diccionario,letra):
    """Dado un diccionario de palabras, y una letra, esta función devuelve la lista de palabras que empiezan por una letra que alfabéticamente está antes que la indicada.
    Args:
      diccionario
      letra
    Returns:
      resultado: ej. ['AUNQUE','ABINAR']
    """
    # el error se daba porque se inicializa el array  que se devuelve cada vez que se añade una palabra, por lo que
    # el resultado solo era la ultima palabra
    # el array debe estar fuera del bucle, local a nivel de funcion no del if
    resultado=[]
    for clave in diccionario:
        for palabra in diccionario[clave]:
            if palabra[0] < letra:
                resultado.append(palabra)
    return resultado

def add_client(clients_list,nif,name,address,phone,email):
    """Dado un diccionario de clientes y datos de un nuevo cliente, esta función inserta estos datos como un nuevo cliente.
    Args:
      diccionario
      nif
      name 
      address
      phone
      email
    """
    # se estaba poniendo dentro del valor del diccionario una estructura que no esperaba el test
    # el test esperaba Nif -> {name:"",---} se le estaba devolviendo Nif -> {Nif:{name:"",---}}
    # se soluciono cambiando la estrcutura
    clients_list[nif] = {'name': name,
              'address': address,
              'phone': phone,
              'email': email
        
    }

def repartir_cartas(cartas_iniciales,repeticiones):
    """Dada una baraja de cartas iniciales y un número de repeticiones, esta función selecciona 5 cartas aleatorias de esta baraja y las mete en un diccionario llamado combinaciones. El proceso se repite tantas veces como repeticiones se indiquen.
    Args:
      cartas_iniciales
      repeticiones
    Returns:
      combinaciones: ej. {'repeticion1': ['contable', 'alguacil', 'asesino', 'cardenal', 'obispo']}
    """    
    combinaciones={}
    for i in range(1,repeticiones+1):
        # el error se daba al igualar el array cartas_aleatorias con cartas_iniciales, 
        # no se estaba copiando el array sino igualando la referencia, por lo que al borrar en una
        # se borraba en la otra y no se reiniciaban las cartas 
        # La solucion es copiar el array en vez de igualarlo
        cartas_aleatorias = []
        cartas_aleatorias = cartas_iniciales.copy() 
        combinaciones["repeticion"+str(i)]=[]
        for j in range(0,5):
            print(cartas_aleatorias)
            carta=random.choice(cartas_aleatorias)
            combinaciones["repeticion"+str(i)].append(carta)
            cartas_aleatorias.remove(carta)

    print(combinaciones)
    return combinaciones

    
