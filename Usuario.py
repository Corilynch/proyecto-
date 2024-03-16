class Usuario():
    
    #Constructor
    def __init__(self, nombre, correo, tipo, id, username):
        self.nombre = nombre
        self.correo = correo
        self.tipo = tipo
        self.id = id
        self.username = username
    
    
    #Metodos
    def mostrar(self):
        print(f'''
         nombre: {self.nombre}
         correo: {self.correo}
         tipo: {self.tipo}
         id: {self.id}
         username: {self.username}
         ''')
        
        
        
    