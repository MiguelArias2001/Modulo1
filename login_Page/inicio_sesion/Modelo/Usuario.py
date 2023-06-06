class Usuario:
    def __init__(self, codigo, nombre, correo, contraseña):
        self.codigo = codigo
        self.nombre = nombre
        self.email = correo
        self.password = contraseña
        self.activo = None
        self.fecha = None

    def get_codigo(self):
        return self.codigo
    
    def get_nombre(self):
        return self.nombre
    
    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def set_codigo(self, codigo):
        self.codigo = codigo

    def set_nombre(self, nombre):
        self.nombre = nombre    
    
    def set_email(self, correo):
        self.email = correo

    def set_password(self, password):
        self.password = password

    def set_activo(self, activo):
        self.activo = activo

    def get_activo(self):
        return self.activo   
    
    def set_fecha(self, fecha):
        self.fecha = fecha

    def get_fecha(self):
        return self.fecha  

    def to_string(self):
        return "Usuario("+str(self.codigo)+", "+self.nombre+", "+self.email+", "+self.password+")"