from inicio_sesion.Modelo.Connetion import Connection
from inicio_sesion.Modelo.Usuario import Usuario

class UsuarioDTO:
    
    def __init__(self):
        self.db = Connection.get_instance()
        self._SQL_CREATE_USER = "CALL crear_usuario(%s,%s,%s,%s)"
        self._SQL_DELETE_USER = "CALL Delete_Account(%s)"
        self._SQL_UPDATE_USER = "CALL Update_Profile(%s,%s,%s,%s)"
        self._SQL_VALIDATE_USER = "CALL inicio_sesion(%s,%s)"
        self._SQL_SEARCH_USER = "CALL Search_user(%s,%s)"
        self._SQL_SELECT_USER = "SELECT Nombre, Correo, Contrasena FROM usuarios WHERE codigo = %s AND Activo = 1"
        self._SQL_EXIST_USER = "CALL User_exist(%s)"
        self._SQL_UPDATE_PASSWORD = "CALL Update_pass(%s,%s)"
    
    def create_user(self, usuario: Usuario):
        result = self.db.execute_query(self._SQL_CREATE_USER,(usuario.get_codigo(),usuario.get_nombre(),usuario.get_email(),usuario.get_password())) # type: ignore
        return print(result)
    
    def update_user(self, usuario: Usuario):
        return self.db.execute_query(self._SQL_UPDATE_USER,(usuario.get_nombre(),usuario.get_email(),usuario.get_codigo(),usuario.get_password())) # type: ignore
    
    def delete_user(self, usuario: Usuario):
        return self.db.execute_query(self._SQL_DELETE_USER,(usuario.get_codigo(),)) # type: ignore
    
    def search_user(self, usuario: Usuario):
        result = self.db.execute_query(self._SQL_VALIDATE_USER,(usuario.get_email(),usuario.get_password(),)) # type: ignore
        if result:
            return result
        else:
            return print("Error en correo: "+usuario.get_email()+", Password: "+usuario.get_password()+"")
    
    def User_exist(self, usuario: Usuario):
        id = self.db.execute_query(self._SQL_EXIST_USER,(usuario.get_email(),))# type: ignore
        if id[0] == 1: # type: ignore
            return True
        else:
            return False
    
    def update_pass(self, usuario: Usuario):
        mensaje = self.db.execute_query(self._SQL_UPDATE_PASSWORD,(usuario.get_password(),usuario.get_email(),))# type: ignore
        return print(mensaje)

    def select_user(self,usuario: Usuario):
        result = self.db.execute_query(self._SQL_SELECT_USER,(usuario.get_codigo(),))# type: ignore
        if result is not None:
            nombre, correo, contrasena = result
            user = Usuario(usuario.get_codigo(), nombre, correo, contrasena)
            return user
        else:
            return None
        
    def search_code(self, usuario: Usuario):
        result = self.db.execute_query(self._SQL_SEARCH_USER,(usuario.get_email(), usuario.get_password(), )) #type: ignore
        return result
    
    def charge_user(self, usuario: Usuario):
        result = self.db.execute_query(self._SQL_SELECT_USER,(usuario.get_codigo(),)) #type: ignore
        if result is not None:
            nombre, correo, contrasena = result
            user= Usuario(usuario.get_codigo(), nombre, correo, contrasena)
            return user
        else:
            return None