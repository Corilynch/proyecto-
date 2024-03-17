class Cancion():
    
    def __init__ (self, id , nombre, duracion, link):
        self.nombre = nombre  
        self.duracion = duracion 
        self.likes = 0
        self.id = id 
        self.link = link 
        self.veces_escuchas = 0
        
    def mostrar(self):
        print (f'''
        nombre: {self.nombre}
        duracion: {self.duracion}
        likes: {self.likes}
        id: {self.id}
        link: {self.link}
        ''')
   