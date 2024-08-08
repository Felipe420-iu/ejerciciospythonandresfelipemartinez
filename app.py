from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/registrar', methods=['POST'])
def registrar_usuario():
    return '''
        <h2>Registro de Usuario</h2>
        <form method="post" action="/usuario_registrado">
            <label>Ingresa tu nombre de usuario:</label><br>
            <input type="text" name="nombre_usuario"><br>
            <label>Ingresa tu correo electrónico:</label><br>
            <input type="email" name="correo_electronico"><br>
            <label>Ingresa tu contraseña:</label><br>
            <input type="password" name="contrasena"><br>
            <label>Confirma tu contraseña:</label><br>
            <input type="password" name="confirmar_contrasena"><br>
            <input type="submit" value="Registrar">
        </form>
    '''

@app.route('/usuario_registrado', methods=['POST'])
def usuario_registrado():
    nombre_usuario = request.form['nombre_usuario']
    correo_electronico = request.form['correo_electronico']
    contrasena = request.form['contrasena']
    confirmar_contrasena = request.form['confirmar_contrasena']
    
    if contrasena == confirmar_contrasena:
        usuario = {
            "Nombre de usuario": nombre_usuario,
            "Correo electrónico": correo_electronico,
            "Contraseña": contrasena
        }
        return f'''
            <h2>Usuario registrado con éxito!</h2>
            <p>Información del usuario:</p>
            <pre>{usuario}</pre>
        '''
    else:
        return '''
            <h2>Las contraseñas no coinciden. Por favor, intenta de nuevo.</h2>
            <a href="/registrar">Volver al registro</a>
        '''

if __name__ == '_main_':
    
    app.run(debug=True)
@app.route('/')
def bienvenida():
    return '''
        <h1>Hola ¡bienvenido!</h1>
        <form method="post" action="/saludar">
            <label>¿Cuál es tu nombre?</label><br>
            <input type="text" name="nombre"><br>
            <input type="submit" value="Enviar">
        </form>
    '''

@app.route('/saludar', methods=['POST'])
def saludar():
    nombre = request.form['nombre']
    return f'''
        <h2>Hola, {nombre}, un gusto en saludarte</h2>
        <form method="post" action="/edad">
            <label>¿Qué edad tienes?</label><br>
            <input type="text" name="edad"><br>
            <input type="submit" value="Enviar">
        </form>
    '''

@app.route('/edad', methods=['POST'])
def edad():
    edad = request.form['edad']
    return '''
        <h2>¡Genial!</h2>
        <form method="post" action="/hobby">
            <label>¿Cuál es tu hobby favorito?</label><br>
            <input type="text" name="hobby"><br>
            <input type="submit" value="Enviar">
        </form>
    '''

@app.route('/hobby', methods=['POST'])
def hobby():
    hobby = request.form['hobby']
    if hobby.lower() == "leer":
        mensaje = "¡Qué interesante! Leer es una gran forma de aprender."
    else:
        mensaje = "¡Genial! Es bueno tener pasatiempos que disfrutes."
    
    return f'''
        <h2>{mensaje}</h2>
        <form method="post" action="/reciclar">
            <label>¿Qué residuo reciclas más en tu hogar?</label><br>
            <input type="text" name="residuo"><br>
            <input type="submit" value="Enviar">
        </form>
    '''

@app.route('/reciclar', methods=['POST'])
def reciclar():
    residuo = request.form['residuo']
    if residuo.lower() == "plastico":
        mensaje = "¡Que excelente! El plástico es uno de los más reciclados por la comunidad."
    else:
        mensaje = "¡Que buena manera de reciclar, te felicito!"
    
    return f'''
        <h2>{mensaje}</h2>
        <form method="post" action="/menu_reciclaje">
            <input type="submit" value="Continuar con reciclaje">
        </form>
    '''

@app.route('/menu_reciclaje', methods=['POST'])
def menu_reciclaje():
    return '''
        <h2>Selecciona lo que deseas reciclar:</h2>
        <form method="post" action="/confirmar_reciclaje">
            <input type="radio" name="material" value="PLASTICO"> PLASTICO<br>
            <input type="radio" name="material" value="CARTON"> CARTON<br>
            <input type="radio" name="material" value="VIDRIO"> VIDRIO<br>
            <input type="radio" name="material" value="METAL"> METAL<br>
            <input type="submit" value="Seleccionar">
        </form>
    '''

@app.route('/confirmar_reciclaje', methods=['POST'])
def confirmar_reciclaje():
    material = request.form['material']
    return f'''
        <h2>Tu selección es {material}, excelente</h2>
        <form method="post" action="/registrar">
            <input type="submit" value="Registrar usuario">
        </form>
    '''

