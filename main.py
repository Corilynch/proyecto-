from Usuario import Usuario
from Album import Album
from Cancion import Cancion
from Artista import Artista
from Oyente import Oyente
from Playlist import Playlist
import requests


def Apis(lista_playlist, lista_album, lista_cancion, lista_usuarios):
    info_usuarios = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json')
    
    for usuario in info_usuarios:
        if usuario["type"] == 'musician':
            usuario_nuevo = Artista(usuario["name"], usuario["email"], usuario["type"], usuario["id"], usuario["username"])
        else:
            usuario_nuevo = Oyente(usuario["name"], usuario["email"], usuario["type"], usuario["id"], usuario["username"])
            
        lista_usuarios.append(usuario_nuevo)
       
    
    #info_playlists = #api
    
    
    
    for playlist in info_playlists:
        playlist_nuevo = Playlist(playlist["id"], playlist["name"], playlist["description"], playlist["creator"], playlist["tracks"])
        lista_playlist.append(playlist)
    
    #info_albums = #api
    
    for albums in info_albums:
        albums_nuevo = Album (["name"], albums["description"], albums["cover"], albums["published"], albums["genre"],albums["id"],  albums["artist"])
        for cancion in albums["tracklist"]:
            cancion_nuevo = Cancion (cancion["id"], cancion["name"], cancion["duration"], cancion["link"])
            albums_nuevo.tracklist.append(cancion_nuevo)
            lista_cancion.append(cancion_nuevo)
            
        lista_album.append(albums)
        
#Esta es la funcion que gestiona el perfil
def gestion_perfil(lista_usuarios):
    print ('''
            1. Registrar nuevos usuarios
            2. Buscar perfiles
            3. Cambiar informacion personal
            4. Borrar datos de la cuenta''')
    opcion = input("Ingresa el numero de la gestion que deseas: ")
    
    if opcion == "1":
      id = uuid.uuid4()
      Nombre= input ("ingresa tu nombre y apellido")
      correo= input ("ingresa tu correo")
      usuario= input("ingresa tu nombre de ususario")
      tipo= input ("ingrese su tipo de usuario: 1.oyente, 2.artista")
      if tipo == "1":
        tipo = 'listener'
        nuevo_usuario= Oyente(Nombre, correo, tipo, id, usuario)
        lista_usuarios.append(nuevo_usuario)
      elif tipo == "2":
        tipo = 'musician'
        nuevo_artista = Artista(Nombre, correo, tipo,id, usuario)
        lista_usuarios.append(nuevo_artista)
      print ("Su cuenta en Metrotify ha sido creada con éxito")
      
      
    elif opcion == "2":
      buscar = input ('Qué nombre deseas buscar?')
      for usuario in lista_usuarios:
        if usuario.nombre == buscar:
          usuario.mostrar()
          
    elif opcion == "3":
      alerta= 0
      buscar = input ('Ingresa el Username de la persona a la que deseas cambiarle la información')
      for usuario in lista_usuarios:
        if usuario.usarname == buscar:
          print (''' 
          1. Cambiar nombre
          2. Cambiar correo elctrónico
          3. Cambiar username ''')
          
          cambio= input ('Que informacion deseas cambiar?')
          if cambio== "1":
            nuevo_nombre = input('ingresa tu nuevo nombre')
            usuario.nombre = nuevo_nombre
            print ('se ha cambiado tu nombre')
          elif cambio == "2":
            nuevo_correo = input ('ingresa tu nuevo correo')
            usuario.correo = nuevo_correo
            print ('se ha cambiado tu correo')
          elif cambio== "3":
            nuevo_username=  input ('ingresa tu nuevo username')
            usuario.username = nuevo_username
            print ('se ha cambiado tu username')
          alerta = 1
      if alerta == 0:
        print ('Este usuario no se encuentra dentro de la base de datos')    
    
    elif opcion == "4":
      alerta= 0
      buscar = input ('Ingresa el Username de la persona a la que deseas eliminar')
      for usuario in lista_usuarios:
        if usuario.usarname == buscar:
          lista_usuarios.remove(usuario)
          print ('Usuario eleiminado')
          alerta = 1
      if alerta == 0:
        print ('Este usuario no se encuentra dentro de la base de datos')    
    
#Esta es la funcion que gestiona la musican
def gestion_musica(lista_usuarios, lista_cancion, lista_album, lista_playlist):
  usuario_actual=''
  buscar = input ('Ingresa el Username de la persona  que desea entrar a la gestión musical')
  for usuario in lista_usuarios:
    if usuario.usarname == buscar:
      usuario_actual = usuario
  
  if usuario_actual == "musician":
    print('''
        1. Crea un Album
        2. Escuchar musica
        3. Crear playlist
        4. Buscador''')
    opcion = input("Ingresa el numero de la gestion que deseas: ")
    
    if opcion == '1':
      nombre = input ('ingresa el nombre de tu album')
      descripcion= input ('ingresa la descricion de tu album')
      portada= ('ingresa la portada de tu album (link)')
      fecha_de_publicación = input ('ingresa la fecha de publicación tu album')
      género = input ('ingresa el género tu album')
      artista = usuario_actual.id
      id = uuid.uuid4()
      nuevo_album = Album(nombre, descripcion, portada, fecha_de_publicación, género, id, artista)
      
      print ('Se ha creado un nuvo album')
      while True:
        print("Ingrese la informacion de la cancion a agregar")
        id = uuid.uuid4()
        nombre = input ('ingrese el nombre de la cancion')
        duracion = input ('ingrese la duracion de la cancion')
        link = input ('ingrse el link de la cancion')
        nueva_cancion = Cancion (id, nombre, duracion, link)
        lista_cancion.append(nueva_cancion)
        nuevo_album.tracklist.append(nueva_cancion)
        print ('Se ha agredado una nueva cancion')
        
        otra_cancion = input ('''quieres agregar una otra cancion?
                              1.si 
                              2.no
                              ''')
        
        if otra_cancion ==  "2":
          break
      
      lista_album.append(nuevo_album)
      print ('Tu álbum ha sido creado con éxito')
      
    elif opcion== '2':
      print ('''
      1. Buscar el álbum 
      2. Buscar canciones 
      3. Acceder a las canciones entrando al perfil del músico
      4. Escuchar la canción a través de una playlist. ''')
      
      #falta sumarle a las reproducciones 
      if opcion == '1':
        buscar_album= input ('ingresa el nombre del album')
        for album in lista_album:
          if album.nombre == buscar_album:
            print ('estas escuchando el album')
      
      elif opcion== '2':
        buscar_cancion= input ('ingresa el nombre de la cancion')
        for cancion in lista_cancion:
          if cancion.nombre == buscar_cancion:
            print ('estas escuchando la cancion')
            
      elif opcion == '3':
        #se busca el perfil
        buscar_perfil = input ('ingresa el perfil de la persona')
        for usuario in lista_usuarios:
          if usuario.nombre == buscar_perfil:
            print ('Has encontrado el perfil')
           
           # Muestra los albunes del perfil selecciado 
            contador = 0
            for album in lista_album:
              if album.artista == usuario.id:
                print(contador+1, album.nombre)
                contador = contador +1
              
            opcion_album = input ('ingresa el album que sea usar ')
            # selecciona un albun de la lista mostrada 
            album_escogido =""
            contador = 0
            for album in lista_album:
              if album.artista == usuario.id:
                if contador == int(opcion_album)-1:
                  album_escogido = album
                contador = contador +1
             
            
            for i, cancion in enumerate(album_escogido.tracklist):
                print(i+1, cancion.nombre)
            
            opcion_cancion= input ('ingrese la cancion que desea escuchar')
            
            album_escogido.tracklist[int( opcion_cancion)-1]
            print ('estas escuchando la cancion')
       
      elif opcion == '4':
        for i, playlist in enumerate (lista_playlist):
            print(i+1, playlist.nombre)
              
        opcion_playlist = input ('ingresa la playlist que sea usar ')
            # selecciona una playlist 
            
        playlist_escogida = lista_playlist[int(opcion_playlist)-1]
             
            
        for i, cancion in enumerate(playlist.escogidatracks):
            print(i+1, cancion.nombre)
        
        opcion_cancion= input ('ingrese la cancion que desea escuchar')
        
        playlist_escogida.tracks[int( opcion_cancion)-1]
        print ('estas escuchando la cancion')   
            
    #crear playlist
    elif opcion == '3':
      id= uuid.uuid4()
      nombre = input ('ingresa el nombre de la playlist')
      descripcion= input ('ingresa la descripcion de la playlist(link)')
      creador = usuario_actual.id
      tracks=[]
      
      while True:
        for i, cancion in enumerate (lista_cancion):
          print (i+1, cancion.nombre)
          
        selecion_cancion= input ('seleciona la cancion que deseas escuchar')
        cancion_escogida = lista_cancion[int(selecion_cancion)-1]
        tracks.append(cancion_escogida) 
        
        print ('Se ha agredado una nueva cancion')
        
        otra_cancion = input ('''quieres agregar una otra cancion?
                              1.si 
                              2.no
                              ''')
        
        if otra_cancion ==  "2":
          break
      
      nueva_playlist = Playlist(id, nombre, descripcion, creador,tracks)
      lista_playlist.append(nueva_playlist)
      print ('Tu playlist ha sido creado con éxito')
 
    elif opcion== '4':
      print ('''
            1. Nombre del músico
            2. Nombre del álbum
            3. Nombre de la canción
            4. Nombre de la playlist
             ''')
      opcion = input('seleccione el elemento que desea buscar')
      if opcion== '1':
          buscar_perfil= input ('ingrese el nombre del perfil')
          for usuario in lista_usuarios:
            if usuario.tipo == 'musicion':
              if usuario.nombre == buscar_perfil:
                  usuario.mostrar()
                  
      if opcion == '2':
        buscar_album= input ('selecciona el nombre del album')
        for album in lista_album:
          if album.nombre == buscar_album:
            album.mostrar()
        
      if opcion == '3':
          buscar_cancion= input ('ingresa el nombre de la cancion')
          for cancion in lista_cancion:
              if cancion.nombre == buscar_cancion:
                cancion.mostrar()
                
      if opcion == '4':
        buscar_playlist= input ('selecciona el nombre de la playlist')
        for playlist in lista_playlist:
          if playlist.nombre == buscar_playlist:
            playlist.mostrar()
        
  else:
    print('''
        1. Escuchar musica
        2. Crear playlist
        3. Buscador''')
    
    opcion = input("Ingresa el numero de la gestion que deseas: ")
    if opcion== '1':
      print ('''
      1. Buscar el álbum 
      2. Buscar canciones 
      3. Acceder a las canciones entrando al perfil del músico
      4. Escuchar la canción a través de una playlist. ''')
      
      #falta sumarle a las reproducciones 
      if opcion == '1':
        buscar_album= input ('ingresa el nombre del album')
        for album in lista_album:
          if album.nombre == buscar_album:
            print ('estas escuchando el album')
      
      elif opcion== '2':
        buscar_cancion= input ('ingresa el nombre de la cancion')
        for cancion in lista_cancion:
          if cancion.nombre == buscar_cancion:
            print ('estas escuchando la cancion')
            
      elif opcion == '3':
        #se busca el perfil
        buscar_perfil = input ('ingresa el perfil de la persona')
        for usuario in lista_usuarios:
          if usuario.nombre == buscar_perfil:
            print ('Has encontrado el perfil')
           
           # Muestra los albunes del perfil selecciado 
            contador = 0
            for album in lista_album:
              if album.artista == usuario.id:
                print(contador+1, album.nombre)
                contador = contador +1
              
            opcion_album = input ('ingresa el album que sea usar ')
            # selecciona un albun de la lista mostrada 
            album_escogido =""
            contador = 0
            for album in lista_album:
              if album.artista == usuario.id:
                if contador == int(opcion_album)-1:
                  album_escogido = album
                contador = contador +1
             
            
            for i, cancion in enumerate(album_escogido.tracklist):
                print(i+1, cancion.nombre)
            
            opcion_cancion= input ('ingrese la cancion que desea escuchar')
            
            album_escogido.tracklist[int( opcion_cancion)-1]
            print ('estas escuchando la cancion')
       
      elif opcion == '4':
        for i, playlist in enumerate (lista_playlist):
            print(i+1, playlist.nombre)
              
        opcion_playlist = input ('ingresa la playlist que sea usar ')
            # selecciona una playlist 
            
        playlist_escogida = lista_playlist[int(opcion_playlist)-1]
             
            
        for i, cancion in enumerate(playlist.escogidatracks):
            print(i+1, cancion.nombre)
        
        opcion_cancion= input ('ingrese la cancion que desea escuchar')
        
        playlist_escogida.tracks[int( opcion_cancion)-1]
        print ('estas escuchando la cancion')   
            
      #crear playlist
    elif opcion == '2':
      id= uuid.uuid4()
      nombre = input ('ingresa el nombre de la playlist')
      descripcion= input ('ingresa la descripcion de la playlist(link)')
      creador = usuario_actual.id
      tracks=[]
      
      while True:
        for i, cancion in enumerate (lista_cancion):
          print (i+1, cancion.nombre)
          
        selecion_cancion= input ('seleciona la cancion que deseas escuchar')
        cancion_escogida = lista_cancion[int(selecion_cancion)-1]
        tracks.append(cancion_escogida) 
        
        print ('Se ha agredado una nueva cancion')
        
        otra_cancion = input ('''quieres agregar una otra cancion?
                              1.si 
                              2.no
                              ''')
        
        if otra_cancion ==  "2":
          break
      
      nueva_playlist = Playlist(id, nombre, descripcion, creador,tracks)
      lista_playlist.append(nueva_playlist)
      print ('Tu playlist ha sido creado con éxito')
 
    elif opcion== '3':
      print ('''
            1. Nombre del músico
            2. Nombre del álbum
            3. Nombre de la canción
            4. Nombre de la playlist
             ''')
      opcion = input('seleccione el elemento que desea buscar')
      if opcion== '1':
          buscar_perfil= input ('ingrese el nombre del perfil')
          for usuario in lista_usuarios:
            if usuario.tipo == 'musicion':
              if usuario.nombre == buscar_perfil:
                  usuario.mostrar()
                  
      if opcion == '2':
        buscar_album= input ('selecciona el nombre del album')
        for album in lista_album:
          if album.nombre == buscar_album:
            album.mostrar()
        
      if opcion == '3':
          buscar_cancion= input ('ingresa el nombre de la cancion')
          for cancion in lista_cancion:
              if cancion.nombre == buscar_cancion:
                cancion.mostrar()
                
      if opcion == '4':
        buscar_playlist= input ('selecciona el nombre de la playlist')
        for playlist in lista_playlist:
          if playlist.nombre == buscar_playlist:
            playlist.mostrar()
        
    
#Esta es la funcion que gestiona las interacciones 
def gestion_interaciones(lista_usuarios, lista_cancion,lista_album, lista_playlist):
    usuario_actual=''
    buscar = input ('Ingresa el Username de la persona  que desea entrar a la gestión de interaciones')
    for usuario in lista_usuarios:
        if usuario.usarname == buscar:
          usuario_actual = usuario
          
    print('''
          1. Darle like al perfil de un musico
          2. Darle like a una cancion
          3. Darle like a un album 
          4. Darle like a una playlist
          ''')
    opcion = input("Ingresa el numero de la gestion que deseas: ")
    
    if opcion == '1':
      buscar_perfil= input ('ingrese el nombre del perfil')
      for usuario in lista_usuarios:
          if usuario.tipo == 'musicion':
            if usuario.nombre == buscar_perfil:
                usuario.mostrar()
                print ('le has dado like')
                
    elif opcion == '2':
      buscar_cancion= input ('ingresa el nombre de la cancion')
      for cancion in lista_cancion:
        if cancion.nombre == buscar_cancion:
          cancion.mostrar()
          print ('le has dado like')
          
    elif opcion == "3":
      buscar_album= input ('selecciona el nombre del album')
      for album in lista_album:
          if album.nombre == buscar_album:
            album.mostrar()
            print ('le has dado like')
            
    elif opcion == '4':
        buscar_playlist= input ('selecciona el nombre de la playlist')
        for playlist in lista_playlist:
          if playlist.nombre == buscar_playlist:
            playlist.mostrar()
            print ('le has dado like')
        

#Esta es la funcion que gestiona los inidcadores 
def gestion_indicadores():
    print('''
          1. Generar informes
          2. Realizar graficos ''')
    opcion = input("Ingresa el numero de la gestion que deseas: ")
    if opcion == '1':
        print ('''
               a. Top 5 de músicos con mayor cantidad de streams
               b. Top 5 de álbumes con mayor cantidad de streams
               c. Top 5 de canciones con mayor cantidad de streams
               d. Top 5 de escuchas con mayor cantidad de streams
               ''')
        opcion = input("Ingresa el numero de la opcion que deseas: ")
    else:
        pass
    

#Esta es mi funcion principal
def main():
    
    lista_playlist = []
    lista_album = []
    lista_cancion = []
    lista_usuarios = []
    
    #Apis(lista_playlist, lista_album, lista_cancion, lista_usuarios) 
    
    
    url = 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json'
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    print(data)
    
    print('Bienvenido a Metrotify,selecciona un modulo:')

    while True:
        print('''
        1. Gestion de perfil 
        2. Gestion de musica
        3. Gestion de intecciones 
        4. Indicadores 
        5. Cerrar programa 
            ''')
        Inicio= input("Ingresa el numero de la gestion que deseas: ")
        
        if Inicio == '1': 
            print("Gestion de perfil")
            gestion_perfil(lista_usuarios)
        elif Inicio == '2':
            print('Gestion de musica')
            gestion_musica()
        elif Inicio == '3':
            print('gestion de interacciones')
            gestion_interaciones()
        elif Inicio == '4':
            print("Indicadores")
            gestion_indicadores()
        elif Inicio == '5':
            print('Hasta luego')
            break
        else: 
            print ('dato ivalido')

main()
  



