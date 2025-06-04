import mysql.connector 

database = mysql.connector.connect( # LLAMAMOS AL FUNCION CONNECT PARA CONECTARNOS
    host = "127.0.0.1",
    port = 3306,
    ssl_disabled = True,
    user ='root', #USUARIO QUE USAMOS NOSOTROS
    password ='my-secret-pw', #CONTRASEÑA CON LA QUE NOS CONECTAMOS
    database='hospital'
) 