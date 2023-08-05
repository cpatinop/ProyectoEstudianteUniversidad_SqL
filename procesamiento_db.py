import mysql.connector  # De esta forma importo a mysql a mi proyecto

def Conexion_DB(): # Esta funcion es para conectarme a la base de datos que ya cree en mysql 
    mi_conexion = mysql.connector.connect(   # Lo primero es un objeto que me conecta con con el metodo connect
    host ="localhost",  # #Estos son datos de mi base datos
    user ="root",#Estos son datos de mi base datos
    password = "root",#Estos son datos de mi base datos
    database = "universidad"#Estos son datos de mi base datos, este databes que me estoy conectando
        )

    return mi_conexion

def Registrar_Alumno(nombre, apellidos, carrera, edad):
    mi_db = Conexion_DB()
    mi_cursor = mi_db.cursor()

    sql = """INSERT INTO estudiantes 
                (nombre, apellidos, carrera, edad)
            VALUES (%s, %s, %s, %s)"""

    valores = (nombre, apellidos, carrera, edad)

    #try: 
        #mi_cursor.execute(sql, valores)
    #except:
        #mi_db.rollback() 
        #retorno = 1 
    try:
        mi_cursor.execute(sql, valores)
    except Exception as e:
        mi_db.rollback()
        retorno = str(e)    
    else:
        mi_db.commit() 
        retorno = 0
    finally:     
        mi_db.close()
        return retorno

#resultado = Registrar_Alumno( "Camilo", "Patiño", "Ing Sistemas", 24)
#print (resultado) 

def Listar_Alumnos():
    mi_db = Conexion_DB()
    mi_cursor = mi_db.cursor() 

    sql = """SELECT nombre, apellidos, carrera
                FROM estudiantes"""

    try:
        mi_cursor.execute(sql)
    except Exception as e:
        mi_db.rollback()
        retorno = str(e)
    else:
        retorno = []                     