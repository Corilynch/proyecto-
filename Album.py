class Album():
    
    def __init__(self, nombre, descripcion, portada, fecha_de_publicacion, genero_predomiante, id, artista):
        self.nombre = nombre 
        self.descripcion = descripcion
        self.portada = portada
        self.fecha_de_publicacion = fecha_de_publicacion
        self.genero_predominante = genero_predomiante
        self.id = id
        self.artista = artista 
        self.tracklist = []
        self.veces_escuchas = 0
        
    def mostrar(self):
        print (f'''
         nombre:{self.nombre}
         descripcion:{self.descripcion}
         portada:{self.portada}
         fecha_de_pulicacion:{self.fecha_de_publicacion}
         genero_predominante:{self.genero_predominante}
         id:{self.id}
         artista:{self.artista}
         tracklist:{self.tracklist}
         ''')

