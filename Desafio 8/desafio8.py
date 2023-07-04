# Crear las siguientes clases con sus atributos y métodos.

# Clase Usuario
## atributos: id, nombre, apellido, teléfono, username, email, contraseña, fecha de registro, avatar, estado, online

from datetime import datetime
class Usuario:
    def __init__ (self, id, nombre, apellido, telefono, username, email, contraseña, estado):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.username = username
        self.email = email
        self.contraseña = contraseña
        self.fecha_registro = datetime.now()
        self.avatar = None
        self.estado = estado
        self.online = False #Clau
        
### Metodos login(), registrar()
    def login(self, username, contraseña): 
        if username == self.username and contraseña == self.contraseña:
            self.online == True
            return f"Bienvenido/a! {self.nombre} has iniciado sesion correctamente" #Euge
        else:
            return f"Usuario o contraseña incorrectos"
    
    
    def registrar(self):
        return f"Hola! {self.nombre} te has registrado correctamente!" #Clau

    
    def cambiar_estado(self, estado):
        self.estado = estado

# Clase Publico(Usuario)
## atributo: es_publico
class Publico(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña)
        self.es_publico = True
        
    ### métodos: comentar(), registrar() -> se define en Usuario por lo que entendi(?
    def comentar(self):
        if self.online == True:
            return f"El usuario {self.nombre} realizo un comentario"
        else:
            return f"Inicia sesion para realizar un comentario publico"
        #Euge

# clase Colaborador(Usuario)
## atributos: es_colaborador
class Colaborador(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña)
        self.es_colaborador= True
### métodos: registrar(), comentar(), publicar()
    def Comentar(self):
        if self.online == True:
            return f"El Colaborador {self.nombre} ha realizado un comentario"
        else:
            return f"Debe iniciar sesion para realizar un comentario"
        
    def Publicar(self):
        if self.online == True:
            return f"El colaborador {self.nombre} ha realizado la publicacion de un articulo"
        else:
            return f"Debe registrarse o iniciar sesion para realizar una publicacion"

# clase Articulo
## id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado
class Articulo:
    def __init__(self, id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado):
        self.id = id
        self.id_usuario = id_usuario
        self.titulo = titulo
        self.resumen = resumen
        self.contenido = contenido
        self.fecha_publicacion = fecha_publicacion
        self.imagen = imagen
        self.estado = estado #Euge


# clase Comentario
## id, id_articulo, id_usuario, contenido, fecha_hora, estado
class Comentario:
    def __init__(self, id, id_articulo, id_usuario, contenido):
        self.id = id
        self.id_articulo = id_articulo
        self.id_usuario = id_usuario
        self.contenido = contenido
        self.fecha_hora = datetime.now() #no la espesifico arriba para que de esta forma tome la fecha y hora en la que se ejecuta
        self.estado = "activo"

    def mostrar_atributos(self):
        fecha_hora_formateada = self.fecha_hora.strftime("%Y-%m-%d %H:%M")
        print("id de comentario: ", self.id)
        print("id de articulo: ", self.id_articulo)
        print("id de usuario: ", self.id_usuario)
        print("comentario: ", self.contenido)
        print("fecha y hora del comentario: ", fecha_hora_formateada)
        print("estado: ", self.estado)

    def cambiar_estado(self, nuevo_estado): #para cambiar de estado de arctivo a inactivo
        self.estado = nuevo_estado   #lo hizo julian


#prueba
# mi_comentario = Comentario(1, 1, 1, "este codigo esta masomenos echo, con el resto del codigo de mis compañeros quedaria mas completo")
# mi_comentario.mostrar_atributos()



#Código para elegir entre registrar usuarios o hacer login (si ya está registrado). Una vez registrado y 
#logueado, código que permita comentar al Publico y además publicar al Colaborador

usuarios= []
usuario = None
while True:
    print("\n----¡Bienvenido/a!----\n")
    print("¿Que desea realizar?\n")
    print("1.Registrar usuario")
    print("2.Iniciar sesion")
    print("3.Salir")

    opcion = input("\nIngrese una opcion: ")

    if opcion == "1":
        nombre = input("Ingresa tu nombre: ")
        apellido = input("Ingresa tu apellido: ")
        telefono = input("Ingresa tu teléfono: ")
        username = input("Ingresa tu username: ")
        email = input("Ingresa tu email: ")
        contraseña = input("Ingresa tu contraseña: ")
        estado ="Activo"
        usuario = Usuario(len(usuarios) + 1, nombre, apellido, telefono, username, email, contraseña)
        usuarios.append(usuario)   
        if usuario.estado == "Inactivo":
            print(f"\n{usuario.registrar()}\n")
            usuario.cambiar_estado("Activo")
        else:
            print("Ya te has registrado anteriormente")


    elif opcion == "2":
            if usuario is not None:
                if not usuario.online:
                    username= input("Ingrese su usuario: ")
                    contraseña=input("Ingrese su contraseña: ")
                    print(f"\n{usuario.login(username, contraseña)}\n")

                else:
                    print("Ya has iniciado sesion")
            else:
                print("Debes registrate primero")

    elif opcion == "3":
        break
    else:
        print("Opcion invalida. Ingrese un numero valido")
