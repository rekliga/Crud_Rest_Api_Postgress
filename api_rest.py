from flask import Flask,request,jsonify,session
from bdconn import create,delete,update,read,inicio,registra
from marshmallow import Schema, fields
import json

app = Flask(__name__)


#estructura para la tabla de usuarios
class UsuarioSchema(Schema):
    id = fields.Int(dump_only=True)
    fullname = fields.Str()
    password = fields.Str()
    email = fields.Str()
    imagen = fields.Raw()

# estructura para publicaciones
class PublicacionSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    priority = fields.Int()
    status = fields.Str()
    time_since_published = fields.TimeDelta()
    user_id = fields.Int()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

app.secret_key = 'contra123'  # Clave secreta para la sesión
#validar = inicio(username, password)
# Ruta para el inicio de sesión
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    validar = inicio(username, password)
    #id de usr(validar[2])
    if username == validar[0] and password == validar[1]:
        session['logged_in'] = True
        session['usuario'] = username
        session['password'] = password
        session['id'] = validar[2]
        return jsonify({'message': f'Login exitoso {username}'})
    else:
        return jsonify({'message': 'Credenciales inválidas'}), 401


@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    mail = request.json.get('correo')
    #validar = inicio(username, password)
    #id de usr(validar[2])
    if registra(username, password, mail ) == True:
        return jsonify({'message': 'Registro Exitoso'}),200
    else:
        return jsonify({'message': 'Registro No correcto'}), 401

# Ruta para el cierre de sesión
@app.route('/logout',methods=['POST'])
def logout():
    session.pop('logged_in', None)
    return jsonify({'message': 'Cierre de sesión exitoso'})

# Ruta protegida que requiere inicio de sesión
@app.route('/protected',methods=['POST'])
def protected():
    print(session)
    if 'logged_in' in session:
        return jsonify({'message': 'Ruta protegida'})
    else:
        return jsonify({'message': 'Acceso no autorizado'}), 401


@app.route('/crear',methods=['POST'])
def crear():
    if 'logged_in' in session:
        try:
            titulo = request.json.get('title')
            descrip = request.json.get('description')
            estatus = request.json.get('status')
            res =create(titulo, descrip, estatus, session['id'])
            #print(create(titulo, descrip, estatus, session['id']))
            return res
        except:
            return jsonify({'message': 'Revisa tus datos'}), 401
    else:
        return jsonify({'message': 'Acceso no autorizado'}), 401    



@app.route('/consultar',methods=['GET'])
def consultar():
    if 'logged_in' in session:
        res = read(session['id'])
        print(res)
        return res


@app.route('/eliminar',methods=['DELETE'])
def eliminar():
    if 'logged_in' in session:
        id_borrar = (request.json.get('id_pub'))
        #print(session['id'])
        borrar = delete(int(id_borrar), session['id'])
        return borrar
        

@app.route('/update',methods=['POST'])
def actualizar():
    if 'logged_in' in session:
        titulo = request.json.get('title')
        descrip = request.json.get('description')
        status = request.json.get('status')
            
        res = update(titulo, descrip, session['id'], 19)
        return res

if __name__ == '__main__':
    app.run(debug=True)










