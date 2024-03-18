from ingredientes import vegetales, proteicos, masa

class Pizza: 
  def __init__(self):
    self.vegetales_1 = None
    self.vegetales_2 = None
    self.proteico = None
    self.masa = None
    self.es_valida = False

  def validar_elemento(elemento, valores):
    return elemento in valores

  def pedido(self):
    self.proteico = input("Ingresasr Ingrediente Proteico: ")
    self.vegetales_1 = input("Ingrese el primer ingrediente vegetal: ")
    self.vegetales_2 = input("Ingrese el segundo ingrediente vegetal: ")
    self.masa = input("Ingrese el tipo de masa (tradicional/delgada: ")
    self.es_valida = self.validar_pedido()

  def validar_pedido(self):
    ingredientes = [self.proteico, self.vegetales_1, self.vegetales_2]
    if (ingredientes.count(None) == 0) and \
       (ingredientes.count("") == 0) and \
       (ingredientes.count(" ") == 0) and \
       (len(set(ingredientes)) == 3) and \
       all(ingrediente in proteicos for ingrediente in [self.proteico]) and \
       all(ingrediente in vegetales for ingrediente in [self.vegetales_1, self.vegetales_2]) and \
       self.masa in masa:
        return True
    else:
        return False
    
  @classmethod
  def validar_clase(cls):
    pizza_dummy = cls()  
    pizza_dummy.pedido() 
    return pizza_dummy.es_valida