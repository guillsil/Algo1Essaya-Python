"""Se quiere modelar una sesión de Google Meet junto con sus usuarios.

Para esto se pide crear una clase Usuario con los siguientes métodos: - __init__(): Recibe el nombre y el mail del usuario. - __str__(): Devuelve una cadena indicando el nombre y mail del usuario.

Y la clase GoogleMeet: - __init__(): Recibe al creador de la sesión. - __str__(): Devuelve una cadena representando a los usuarios en la sesión y a los usuarios esperando a ser aceptados. - ingresar(): Recibe un usuario y lo deja en espera para que sea aceptado. Si ya se encuentra en la sesión o en espera, levanta excepciones con mensajes "Usuario ya se encuentra en la sesión" y "Usuario ya se encuentra en espera" respectivamente. - aceptar(): Recibe el mail de un usuario para aceptar a la sesión. Si no se encuentra en espera, levanta una excepción con mensaje "Usuario no se encuentra en espera". - eliminar(): Recibe el mail de un usuario para eliminar de la sesión o de espera. Si no se encuentra al usuario o se intenta eliminar al creador de la sesión, levanta una excepción con mensajes "Usuario no encontrado" y "No se puede eliminar al creador", respectivamente"""

class Usuario:
    def __init__(self, nombre, mail):
        self.nombre = nombre
        self.mail = mail
    def __str__(self):
        print(f"Nombre: {self.nombre} - Mail: {self.mail}")

class GoogleMeet:
    def __init__(self, creador):
        self.creador = creador
        self.usuarios = []
        self.espera = []
    def __str__(self):
        print(f"Usuarios en la sesión: {self.usuarios}")
        print(f"Usuarios en espera: {self.espera}")
    def ingresar(self, usuario):
        if usuario in self.usuarios:
            raise Exception("Usuario ya se encuentra en la sesión")
        elif usuario in self.espera:
            raise Exception("Usuario ya se encuentra en espera")
        else:
            self.espera.append(usuario)
    def aceptar(self, mail):
        if mail not in self.espera:
            raise Exception("Usuario no se encuentra en espera")
        else:
            self.usuarios.append(mail)
            self.espera.remove(mail) 
    def eliminar(self, mail):
        if mail == self.creador:
            raise Exception("No se puede eliminar al creador")
        elif mail not in self.usuarios and mail not in self.espera:
            raise Exception("Usuario no encontrado")
        elif mail in self.usuarios:
            self.usuarios.remove(mail)
        else:
            self.espera.remove(mail)
    