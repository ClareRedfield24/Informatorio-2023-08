# Clase Usuario
# atributos: id, nombre, apellido, teléfono, username, email, contraseña, fecha de 
# registro, avatar, estado, online
# métodos: login(), registrar()


from datetime import datetime
class Usuario:
    def __init__ (self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.username = username
        self.email = email
        self.contraseña = contraseña
        self.fecha_registro = datetime.now()
        self.avatar = None
        self.estado = "Activo"
        self.online = False

    def login(self):
        self.online= True
        return f"Bienvenido/a! {self.nombre} has iniciado sesion correctamente"
    
    def registrar(self):
        return f"Hola! {self.nombre} te has registrado correctamente!"
    

    

    

