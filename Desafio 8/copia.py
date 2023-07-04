class Usuario:
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.username = username
        self.email = email
        self.contraseña = contraseña
        self.fecha_registro = fecha_registro
        self.avatar = avatar
        self.estado = estado
        self.online = online

    def login(self):
        self.online = True
        print("Inicio de sesión exitoso.")

    def registrar(self):
        print("Registro exitoso.")


class Publico(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online)
        self.es_publico = True

    def comentar(self):
        print("Comentario realizado.")


class Colaborador(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online)
        self.es_colaborador = True

    def comentar(self):
        print("Comentario realizado.")

    def publicar(self):
        print("Artículo publicado.")


class Articulo:
    def __init__(self, id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado):
        self.id = id
        self.id_usuario = id_usuario
        self.titulo = titulo
        self.resumen = resumen
        self.contenido = contenido
        self.fecha_publicacion = fecha_publicacion
        self.imagen = imagen
        self.estado = estado


class Comentario:
    def __init__(self, id, id_articulo, id_usuario, contenido, fecha_hora, estado):
        self.id = id
        self.id_articulo = id_articulo
        self.id_usuario = id_usuario
        self.contenido = contenido
        self.fecha_hora = fecha_hora
        self.estado = estado


def menu_principal():
    usuarios_registrados = []

    while True:
        print("\n=== Menú Principal ===")
        print("1. Registrarse")
        print("2. Iniciar Sesión")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id = input("Ingrese su ID: ")
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            telefono = input("Ingrese su teléfono: ")
            username = input("Ingrese su nombre de usuario: ")
            email = input("Ingrese su email: ")
            contraseña = input("Ingrese su contraseña: ")
            fecha_registro = input("Ingrese la fecha de registro: ")
            avatar = input("Ingrese su avatar: ")
            estado = input("Ingrese su estado: ")
            online = False

            nuevo_usuario = Usuario(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online)
            usuarios_registrados.append(nuevo_usuario)
            nuevo_usuario.registrar()

        elif opcion == "2":
            username = input("Ingrese su nombre de usuario: ")
            contraseña = input("Ingrese su contraseña: ")

            usuario_encontrado = None
            for usuario in usuarios_registrados:
                if usuario.username == username and usuario.contraseña == contraseña:
                    usuario_encontrado = usuario
                    break

            if usuario_encontrado:
                usuario_encontrado.login()
                if isinstance(usuario_encontrado, Publico):
                    accion_publico(usuario_encontrado)
                elif isinstance(usuario_encontrado, Colaborador):
                    accion_colaborador(usuario_encontrado)
            else:
                print("Nombre de usuario o contraseña incorrectos.")

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Inténtalo de nuevo.")


def accion_publico(usuario):
    while True:
        print("\n=== Acciones de Usuario Público ===")
        print("1. Comentar")
        print("2. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            usuario.comentar()

        elif opcion == "2":
            print("Cerrando sesión de Usuario Público...")
            break

        else:
            print("Opción inválida. Inténtalo de nuevo.")


def accion_colaborador(usuario):
    while True:
        print("\n=== Acciones de Usuario Colaborador ===")
        print("1. Comentar")
        print("2. Publicar artículo")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            usuario.comentar()

        elif opcion == "2":
            usuario.publicar()

        elif opcion == "3":
            print("Cerrando sesión de Usuario Colaborador...")
            break

        else:
            print("Opción inválida. Inténtalo de nuevo.")


# Ejecutar el programa
menu_principal()
