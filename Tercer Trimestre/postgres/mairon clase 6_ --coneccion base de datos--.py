import psycopg2

def conectar():
    try:
        conexion = psycopg2.connect(
            host="localhost",
            database="SENA_1",
            user="postgres",
            password="123456"
        )
        print("Conexión exitosa a la base de datos")
        return conexion
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")

if __name__ == "__main__":
    conectar()