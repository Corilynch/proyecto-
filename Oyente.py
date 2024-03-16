from Usuario import Usuario

class Oyente (Usuario):
    def __init__(self, nombre, correo, tipo, id, username):
        super().__init__(nombre, correo, tipo, id, username)
        self.lista_de_playlist = []
        
    def mostrar(self):
        print(f'''
         nombre: {self.nombre}
         correo: {self.correo}
         tipo: {self.tipo}
         id: {self.id}
         username: {self.username}
         list_de_playlist: {self.lista_de_playlist}
         ''')
        
        
        