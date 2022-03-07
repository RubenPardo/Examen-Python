from operator import contains
from pickle import LIST
import random;


def choose_secret(filename):
    """Dado un nombre de fichero, esta función devuelve una palabra aleatoria de este fichero transformada a mayúsculas.
    Args:
      filename: El nombre del fichero. Ej. "palabras_reduced.txt"
    Returns:
      secret: Palabra elegida aleatoriamente del fichero transformada a mayúsculas. Ej. "CREMA"
    """
    palabras = []

    # abrir fichero en modo lectura
    f = open(filename,"r")

    # leer linea por linea
    linea = f.readline()

    while linea!="":
        # por cada linea quitar el salto de linea
        palabras.append(linea[:len(linea)-1].upper())
        linea = f.readline()
    f.close()

    if len(palabras) < 1:
      raise ValueError("choose_secret Error: No hay palabras en el fichero")
  
    return random.choice(palabras)

    
def compare_words(word, secret):
    """Dadas dos palabras en mayúsculas (word y secret), esta función calcula las posiciones de las letras de word que aparecen en la misma posición en secret, y las posiciones de las letras de word que aparecen en secret pero en una posición distinta.
    Args:
      word: Una palabra. Ej. "CAMPO"
      secret: Una palabra. Ej. "CREMA"
    Returns:
      same_position: Lista de posiciones de word cuyas letras coinciden en la misma posición en secret. En el caso anterior: [0]
      same_letter: Lista de posiciones de word cuyas letras están en secret pero en posiciones distintas. En el caso anterior: [1,2]
    """

    if len(word) != len(secret):
      raise ValueError("compare_words Error: Las palabras no tienen el mismo tamaño")

    same_position = []
    same_letter = []

    cont = 0
    for letra in word:
      if letra == secret[cont]:
        # la letra esta en la misma posicion
        same_position.append(cont)
        
      elif letra in secret:
        # la letra esta en el secret
        same_letter.append(cont)
      cont+=1
    return same_position, same_letter


def print_word(word,same_position, same_letter):
    """Dada una palabra, una lista same_position y otra lista same_letter, esta función creará un string donde aparezcan en mayúsculas las letras de la palabra que ocupen las posiciones de same_position, en minúsculas las letras de la palabra que ocupen las posiciones de same_letter y un guión (-) en el resto de posiciones
    Args:
      word: Una palabra. Ej. "CAMPO"
      same_letter_position: Lista de posiciones. Ej. [0]
      same_letter: Lista de posiciones. Ej. [1,2]
    Returns:
      transformed: La palabra aplicando las transformaciones. En el caso anterior: "Cam--"
    """
   
 
    # control de excepciones ---------
    if type(same_position) != list or type(same_letter) != list:
      raise ValueError("print_word Error: same_position y same_letter deben ser listas")

    for valor in same_position:
      if valor >= len(word):
        raise ValueError("print_word Error: hay un valor superior a la palabra en same_position")
      elif valor < 0:
        raise ValueError("print_word Error: hay un valor negativo en same_position")

    for valor in same_letter:
      if valor >= len(word):
        raise ValueError("print_word Error: hay un valor superior a la palabra en same_letter")
      elif valor < 0:
        raise ValueError("print_word Error: hay un valor negativo en same_letter")

    # funcionalidad ---------
    transformed = ""
    cont = 0
    for letra in word:
      if cont in same_letter:
        transformed = transformed + letra.lower()
      elif cont in same_position:
        transformed = transformed + letra.upper()
      else:
        transformed = transformed + "-"
      cont+=1
    return transformed
    
def choose_secret_advanced(filename):
    """Dado un nombre de fichero, esta función filtra solo las palabras de 5 letras que no tienen acentos (á,é,í,ó,ú). De estas palabras, la función devuelve una lista de 15 aleatorias no repetidas y una de estas 15, se selecciona aleatoriamente como palabra secret.
    Args:
      filename: El nombre del fichero. Ej. "palabras_extended.txt"
    Returns:
      selected: Lista de 15 palabras aleatorias no repetidas que tienen 5 letras y no tienen acentos
      secret: Palabra elegida aleatoriamente de la lista de 15 seleccionadas transformada a mayúsculas
    """
    palabras = []
    selected = []
    
    # abrir fichero en modo lectura
    f = open(filename,"r")

    # leer linea por linea
    linea = f.readline()

    while linea!="":
        # por cada linea quitar el salto de linea
        palabras.append(linea[:len(linea)-1].upper())
        linea = f.readline()
    f.close()
    
    for palabra in palabras:
      print(palabra)
      print("ó" in palabra)

    # solo las de 5 letras y sin acentos
    palabras = list(filter(lambda x: len(x) == 5 ,palabras))

    # control de excepciones ----------------------
    if len(palabras) < 15:
      raise ValueError("choose_secret_advanced Error: no hay 15 palabras de 5 letras sin acentos")

    #seleccionar 15 sin repeticion
    for i in range(0,15):
      palabra = random.choice(palabras)
      palabras.remove(palabra)
      selected.append(palabra)

    # devolver las 15 y una aleatoria de estas
    return selected, random.choice(selected)
 
def check_valid_word(selected):
    """Dada una lista de palabras, esta función pregunta al usuario que introduzca una palabra hasta que introduzca una que esté en la lista. Esta palabra es la que devolverá la función.
    Args:
      selected: Lista de palabras.
    Returns:
      word: Palabra introducida por el usuario que está en la lista.
    """
    valid = True
    word = ""
    while valid:
      word = input("Introduce una palabra: ")
      if word in selected:
        valid = False

    return word

if __name__ == "__main__":
    try:
      selected,secret=choose_secret_advanced("palabras_extended.txt")
      print(selected)
      print("Palabra a adivinar: "+secret)#Debug: esto es para que sepas la palabra que debes adivinar
      for repeticiones in range(0,6):
          #word = input("Introduce una nueva palabra: ")
          word = check_valid_word(selected)
          same_position, same_letter = compare_words(word,secret)
          resultado=print_word(word,same_position,same_letter)
          print(resultado)
          if word == secret:
              print("HAS GANADO!!")
              exit()
      print("LO SIENTO, NO LA HAS ADIVINIDADO. LA PALABRA ERA "+secret)   
    except ValueError as e:
      print(str(e))

