import psycopg2 as ps
import datetime
salir = False
print("Control de citas")
def postgres_insert(nombre,edad,peso,altura,fecha,hora):
    conexion=None
    try:
        conexion=ps.connect(database="Parcial2",user="postgres",password="123456",host="172.25.16.1",port="5432")
        #cursor=conexion.cursor("""INSERT INTO public."controlCitas"("ID", nombre, edad, peso, altura, fecha, hora)VALUES (nextval('pk_controlCitas'), %s, %s, %s, %s, %s,%s); """,(nombre,edad,peso,altura,fecha,hora))
        cursor=conexion.cursor()
        cursor.execute("""INSERT INTO public."controlCitas"("ID", nombre, edad, peso, altura,
        fecha, hora)VALUES (nextval('pk_controlCitas'), %(nm)s, %(ed)s, %(pes)s, %(alt)s, %(date)s,%
        (h)s); """,{'nm':nombre,'ed':edad ,'pes':peso ,'alt':altura ,'date':fecha ,'h':hora})
        conexion.commit()
        cursor.close()
    except (Exception, ps.Error) as error:
        print("Error al obtener datos ", error)
    finally:
        if conexion is not None:
            conexion.close()

def postgres_select(fecha):
     #selectquery=""" SELECT nombre,hora FROM public."controlCitas" where fecha = '2021-04-22'; """
    conexion=None
    try:
        conexion=ps.connect(database="Parcial2",user="postgres",password="123456",host="172.25.16.1",port="5432")
        cursor=conexion.cursor()
        cursor.execute(""" SELECT nombre,hora FROM public."controlCitas" where fecha = %(fecha)s; """,{'fecha':fecha})
        datos=cursor.fetchall()
        print("Registro de datos del programa:")
        for fila in datos:
            print("Nombre: ",fila[0])
            print("Hora: ",fila[1]) 
            print("Fecha: ",fecha)
            print("\n")
            
        cursor.close()
    except (Exception, ps.Error) as error:
        print("Error al obtener datos ", error)
    finally:
        if(conexion is not None):
            conexion.close()

def in_datos():
    try:
        nombre=str(input("Ingrese el nombre del paciente: "))
        edad=int(input("Ingrese la edad del paciente: "))
        peso=float(input("Ingrese el peso del paciente: "))
        altura=float(input("Ingrese la altura del paciente: "))
        print("Formato de fecha YY-MM-DD")
        dia=int(input("Ingrese el dia de la cita: "))
        mes=int(input("Ingrese el mes de la cita: "))
        year=int(input("Ingrese el año de la cita: "))
        print("Formato de hora 24hrs. HH:MM")
        hora=str(int(input("Ingrese la hora: ")))
        minutos=str(int(input("Ingrese los minutos: ")))
        date=datetime.date(year,mes,dia)
        hr=hora+':'+minutos
        print(date)
        print(hr)
        return nombre, edad,peso,altura,date,hr
    except:
        print("Se ha ingresado mal un dato, por favor intentalo de nuevo")

while(salir!=True):
    try:
        print("Menú: \n 1) Ingresar cita \n 2) Mostrar citas \n 3)Salir")
        opc=int(input("Ingrese la opción:\n-->"))
        if(opc==1):
            nombre,edad,peso,altura,date,hr=in_datos() 
            postgres_insert(nombre,edad,peso,altura,date,hr)
        elif(opc==2):
            print("Formato de fecha YY-MM-DD")
            dia=int(input("Ingrese el dia de la cita: "))
            mes=int(input("Ingrese el mes de la cita: "))
            year=int(input("Ingrese el año de la cita: "))
            print("")
            date=datetime.date(year,mes,dia)
            postgres_select(date)
        elif(opc==3):
            salir=True 
        else:
            print("Opcion invalida elige otra!!!")
    except Exception as exc:
        print(str(exc)+"\n Algo va mal")