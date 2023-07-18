from unittest import result
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
        self._SQL_VIEWS_USER = "SELECT * FROM Vista_usuarios"
        #Busqueda de usuario
        self._SQL_SEARCH_USER_NAME = "CALL Search_Name(%s)"
        self._SQL_SEARCH_USER_CODE = "CALL Search_Code(%s)"
        self._SQL_SEARCH_USER_FILTER = "CALL View_Active(%s,%s)"
        #Archivos
        self._SQL_REGISTER = "CALL Registro_contador()"
        self._SQL_GRAPHER = "SELECT * FROM Registro_usuarios"
        self._SQL_ARCHIVE_VIEW = "SELECT * FROM Vista_Archivos"
        self._SQL_ARCHIVE = "CALL INSERT_DATA(%s,%s,%s,%s)"
        self._SQL_ARCHIVE_FILTER = "CALL Revisar_leido(%s)"
        self._SQL_ARCHIVE_UPDATE = "CALL Update_archivo(%s,%s)"
        self._SQL_ARCHIVE_DELETE = "CALL Delete_data(%s)"
    
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
            print(result)
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
        
    def view_users(self, usuario: Usuario):
        result = self.db.execute_querys(self._SQL_VIEWS_USER, ()) #type: ignore
        print("El resultado es "+str(result))
        usuarios = []
        if result is not None:
            for row in result:
                codigo, nombre, correo, fecha_creacion, activo = row #type: ignore
                usuario = Usuario(codigo, nombre, correo, "")
                usuario.set_fecha(fecha_creacion)
                usuario.set_activo(activo)
                usuarios.append(usuario)
        
        return usuarios
    
    def search_users_name(self, usuario: Usuario):
        result = self.db.execute_querys(self._SQL_SEARCH_USER_NAME, (usuario.get_nombre(),)) #type: ignore
        print("El resultado es "+str(result))
        usuarios = []
        if result is not None:
            for row in result:
                codigo, nombre, correo, fecha_creacion, activo = row #type: ignore
                usuario = Usuario(codigo, nombre, correo, "")
                usuario.set_fecha(fecha_creacion)
                usuario.set_activo(activo)
                usuarios.append(usuario)
        
        return usuarios
    
    def search_users_code(self, usuario: Usuario):
        result = self.db.execute_querys(self._SQL_SEARCH_USER_CODE, (usuario.get_codigo(),)) #type: ignore
        print("El resultado es "+str(result))
        usuarios = []
        if result is not None:
            for row in result:
                codigo, nombre, correo, fecha_creacion, activo = row #type: ignore
                usuario = Usuario(codigo, nombre, correo, "")
                usuario.set_fecha(fecha_creacion)
                usuario.set_activo(activo)
                usuarios.append(usuario)
        
        return usuarios

    def search_users_filter(self, Activo: int, Filtro: int):
        result = self.db.execute_querys(self._SQL_SEARCH_USER_FILTER, (Activo,Filtro)) #type: ignore
        print("El resultado es "+str(result))
        usuarios = []
        if result is not None:
            for row in result:
                codigo, nombre, correo, fecha_creacion, activo = row #type: ignore
                usuario = Usuario(codigo, nombre, correo, "")
                usuario.set_fecha(fecha_creacion)
                usuario.set_activo(activo)
                usuarios.append(usuario)
        
        return usuarios
    
    def Register(self):
        result = self.db.execute_query(self._SQL_REGISTER,()) #type: ignore
        Registros = []
        if result is not None:
            activo, inactivo, archivo, foro = result #type: ignore
            Registros = [activo,inactivo,archivo,foro]
        return Registros
    
    def Grafico(self):
        result = self.db.execute_querys(self._SQL_GRAPHER,()) #type: ignore
        Datos = []
        if result is not None:
            for row in result:
                mes, cant = row
                Datos.append({'Mes': mes, 'Visitas': cant})
        return Datos
    
    def Insertar_archivo(self, Nombre: str, Descripcion: str, Archivo, Codigo: int):
        result = self.db.execute_query(self._SQL_ARCHIVE,(Nombre,Descripcion,Archivo,Codigo)) #type: ignore
        return print(result)
    
    def Ver_archivo(self):
        result = self.db.execute_querys(self._SQL_ARCHIVE_VIEW, ()) #type: ignore
        print("El resultado es "+str(result))
        archivo = []
        if result is not None:
            for row in result:
                ID_a, Nombre, Descripcion, leido = row
                arc= {"id":ID_a, "Nombre":Nombre,"descripcion":Descripcion, "leido":leido}
                archivo.append(arc)
        
        return archivo
    
    def Actualizar_Archivo(self,codigo: int,opc: int):
        result=self.db.execute_query(self._SQL_ARCHIVE_UPDATE,(opc,codigo,)) #type: ignore
        return print(result)
    
    def Filtro_Archivo(self, opc: int):
        result = self.db.execute_querys(self._SQL_ARCHIVE_FILTER,(opc,)) #type: ignore
        print("El resultado es "+str(result))
        archivo = []
        if result is not None:
            for row in result:
                ID_a, Nombre, Descripcion, leido = row #type: ignore
                arc= {"id":ID_a, "Nombre":Nombre,"descripcion":Descripcion, "leido":leido}
                archivo.append(arc)
        return archivo
    
    def Eliminar_archivo(self, cod: int):
        result = self.db.execute_query(self._SQL_ARCHIVE_DELETE,(cod,)) #type: ignore
        return print(result)