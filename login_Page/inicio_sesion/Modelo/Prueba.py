from Correo import Correo

c = Correo()

correo = c.get_instance()
correo.to_string()
correo2 = c.get_instance()
correo2.to_string()
correo.recuperacion("cherlock2001@gmail.com")
correo.to_string()
codigo: int
codigo = int(input("Digite el codigo"))
correo2.to_string()
print(correo2.validacion(codigo))