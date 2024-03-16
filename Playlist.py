class Playlist ():
    
    def __init__(self, id, name, descripcion, creador, tracks):
        self.id = id
        self.name = name
        self.descripcion = descripcion
        self.creador = creador
        self.tracks = tracks
        
    def mostrar (self):
        print(f'''
        id: {self.id}
        nombre: {self.name}
        descipcion: {self.descripcion}
        creador: {self.creador}
        tracks: {self.creador}
        ''')
    
    
    
