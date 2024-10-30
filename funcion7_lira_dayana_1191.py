print(" ")#espacio
print("Lira Hernandez Dayana Yamileth 1191")#datos del realizador
print(" ")#espacio
#8 la función recibirá un diccionario de argumentos
#y podrá acceder a los elementos en consecuencia
def my_function(**kid):#define la funcion
    print("His last name is " + kid["lname"])#imprime apellido dado
my_function(fname = "Sofia", lname = "Nolasco")#indica apellido 
print(" ")#espacio
