import psycopg2
from dotenv import load_dotenv
import os
import json

load_dotenv(".env") #cargamos las variables
# Establece los detalles de conexión a la base de datos
host = 'localhost'     # Host donde se encuentra la base de datos
port = '5432'          # Puerto de la base de datos (por defecto es 5432)
database = os.getenv('POSTGRES_DB')#nombre de bd
user = os.getenv('POSTGRES_USER')#nombre de usuario
password = os.getenv('POSTGRES_PASSWORD')  # Contraseña de usuario de PostgreSQL

# Establece la conexión a la base de datos
conn = psycopg2.connect(
    host=host,
    port=port,
    database=database,
    user=user,
    password=password
)

cur = conn.cursor()
dicc = {}



def read(id):
    #print(f'SELECT * FROM publicaciones where user_id = {id}')
    cur.execute(f'SELECT * FROM publicaciones where user_id = {id}')
    results = cur.fetchall()
    for row in range(len(results)):
        id = results[row][0]
        titulo = results[row][1]
        descr = results[row][2]
        priority = results[row][3]
        status = results[row][4]
        time_since_published = results[row][5]
        user_id = results[row][6]
        dicc[row] ={
            "id": id,
            "titulo":titulo,
            "description": descr,
            "priority":priority,
            "status":status,
            "time_since_published":str(time_since_published),
            "user_id":user_id
        }
    conn.commit()
    return {"resultado":[dicc]}
    

def create(title, description, status, user_id):
    #ejem ('Título de ejemplo', 'Descripción de ejemplo', 1, 'Activo', INTERVAL '2 days', 6);
   
    #print(f"""INSERT INTO publicaciones (title, description, priority, status, time_since_published, user_id) VALUES ('{title}', '{description}', 1, '{status}', INTERVAL '2 days', {user_id});""")
    cur.execute(f"""INSERT INTO publicaciones (title, description, priority, status, time_since_published, user_id) VALUES ('{title}', '{description}', 1, '{status}', INTERVAL '2 days', {user_id});""")
    cur.execute(f'SELECT * FROM publicaciones where user_id = {user_id}')
    results = cur.fetchall()
    for row in range(len(results)):
        id = results[row][0]
        titulo = results[row][1]
        descr = results[row][2]
        priority = results[row][3]
        status = results[row][4]
        time_since_published = results[row][5]
        user_id = results[row][6]
        dicc[row] ={
            "id": id,
            "titulo":titulo,
            "description": descr,
            "priority":priority,
            "status":status,
            "time_since_published":str(time_since_published),
            "user_id":user_id
        }
    conn.commit()
    return {"resultado":[dicc]}

def update(title,description,user_id,id_publicacion):
    
    if (type(id_publicacion) == type(int())):
        if len(title)>0 and len(description) > 0:
            cur.execute(f"""UPDATE publicaciones SET title ='{title}',description='{description}' where user_id = {user_id} and id = {id_publicacion}""")
        else:
            if len(title)>0:
                cur.execute(f"""UPDATE publicaciones SET title ='{title}' where user_id = {user_id} and id = {id_publicacion}""")
            elif len(description) > 0:
                cur.execute(f"""UPDATE publicaciones SET description ='{description}' where user_id = {user_id} and id = {id_publicacion}""")

    cur.execute(f'SELECT * FROM publicaciones where user_id = {user_id}')
    results = cur.fetchall()
    for row in range(len(results)):
        id = results[row][0]
        titulo = results[row][1]
        descr = results[row][2]
        priority = results[row][3]
        status = results[row][4]
        time_since_published = results[row][5]
        user_id = results[row][6]
        dicc[row] ={
            "id": id,
            "titulo":titulo,
            "description": descr,
            "priority":priority,
            "status":status,
            "time_since_published":str(time_since_published),
            "user_id":user_id
        }
    conn.commit()
    return {"resultado":[dicc]}

def delete(id,user_id):
    dicc = {}
    cur.execute(f"""DELETE FROM publicaciones where id = {id}""")
    cur.execute(f'SELECT * FROM publicaciones where user_id = {user_id}')
    results = cur.fetchall()
    for row in range(len(results)):
        id = results[row][0]
        titulo = results[row][1]
        descr = results[row][2]
        priority = results[row][3]
        status = results[row][4]
        time_since_published = results[row][5]
        user_id = results[row][6]
        dicc[row] ={
            "id": id,
            "titulo":titulo,
            "description": descr,
            "priority":priority,
            "status":status,
            "time_since_published":str(time_since_published),
            "user_id":user_id
        }
    conn.commit()
    return {"resultado":[dicc]}

def inicio(usuario,Contraseña):
    cur.execute(f"""SELECT * FROM usuarios where fullname = '{usuario}'""")
    results = cur.fetchall()
    user_bd = results[0][1]
    contra_bd = results[0][2]
    id_usr = results[0][0]

    conn.commit()
    
    return user_bd,contra_bd,id_usr
def registra(usuario,Contraseña,correo):
    try:
        cur.execute(f"""INSERT INTO usuarios (fullname, "password", email, imagen)
                    VALUES ('{usuario}', '{Contraseña}', '{correo}', NULL);
                    """)
        
        cur.execute(f"""SELECT * FROM usuarios""")
        results = cur.fetchall()
        conn.commit()
        
        return True
    except:
        return False
    
#print(read(6))
#print(create("toalla del mojado", "muy padre", "chido", 6))
#print(update("", "muito chingona15", 6, 5))
#print(delete(2, 6))