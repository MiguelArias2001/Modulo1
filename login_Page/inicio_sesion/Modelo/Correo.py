import smtplib
import configparser as configdb
import random

class Correo:

    _instance = None

    def __init__(self):
        if Correo._instance != None:
            raise Exception("La clase ya esta en uso")
        else:
            config = configdb.ConfigParser()
            Correo._instance = self
            config.read('Modulo1/login_Page/inicio_sesion/Modelo/config.ini')
            mail = config['smtp']
            self._smtp_server = mail['server']
            self._smtp_port = mail['port']
            self._smtp_user = mail['user']
            self._smtp_password = mail['password']
            self._numero = None

    @staticmethod 
    def get_instance():
        if Correo._instance == None:
            Correo()
        return Correo._instance

    def recuperacion(self, correo: str):
        subject = 'Recuperacion de Contrasena'
        num = random.randint(1000,9999)
        body = 'Hola, '+correo+"\nLe escribimos para informarle que hemos recibido su solicitud de recuperacion de contrasena para su cuenta. Para poder completar el proceso de recuperacion, le pedimos que ingrese el siguiente codigo de seguridad de cuatro digitos en la pagina de recuperacion de contrasena: "+str(num)+". \nPor favor, ingrese este codigo en el campo correspondiente en la pagina de recuperacion de contrasena y siga las instrucciones para restablecer su contrasena. Si no ha solicitado una recuperacion de contrasena, por favor ignore este mensaje."
        message = f'Subject: {subject}\n\n{body}'

        # Envío del correo electrónico
        with smtplib.SMTP(self._smtp_server, int(self._smtp_port)) as server:
            server.starttls()
            server.login(self._smtp_user, self._smtp_password)
            server.sendmail(self._smtp_user, correo, message)
        self._numero = num
        print(num)
        return num

    def validacion(self, codigo):
        if self._numero == codigo:
            print("Existe "+str(self._numero)+"")
            return True
        else:
            print("No Existe "+str(self._numero)+"")
            return False
        
    def to_string(self):
        return print("Numero Aleatorio es: "+str(self._numero)+"")