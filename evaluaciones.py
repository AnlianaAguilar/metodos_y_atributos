from pizza import Pizza
from ingredientes import vegetales, proteicos, masa

print("Atributos de clase de la Pizza:")
print("Ingredientes cárnicos:", proteicos)
print("Ingredientes vegetales:", vegetales)
print("Tipos de masa:", masa)

print("¿La salsa de tomate está presente en la lista?")
print(Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))


mi_pizza = Pizza()
mi_pizza.pedido()

print("Ingredientes de la pizza:")
print("Ingrediente proteico:", mi_pizza.proteico)
print("Ingredientes vegetales:", mi_pizza.vegetales_1, "y", mi_pizza.vegetales_2)
print("Tipo de masa:", mi_pizza.masa)
print("¿Es una pizza válida?", mi_pizza.es_valida)


print("¿La clase Pizza es una pizza válida?", Pizza().validar_clase())