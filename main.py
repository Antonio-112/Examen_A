from flask import app, render_template, request, Flask

app = Flask(__name__)

usuarios = {
    "juan": "admin",
    "pepe": "user"
}

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def formulario():
    precio_tarro = 9000
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        n_tarros = int(request.form['n_tarros'])

        total_sin_descuento = precio_tarro * n_tarros

        if 18 <= edad <= 30:
            descuento = total_sin_descuento * 0.15
        elif edad > 30:
            descuento = total_sin_descuento * 0.25
        else:
            descuento = 0.0

        total_con_descuento = total_sin_descuento - descuento

        return render_template('ejercicio1.html',
                               nombre=nombre,
                               t_sin_descuento=total_sin_descuento,
                               descuento=f"{descuento}",
                               t_con_descuento=total_con_descuento)
    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def formulario_2():
    mensaje = ""
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasenha = request.form['contrasenha']

        # Verificar credenciales
        if usuario in usuarios and usuarios[usuario] == contrasenha:
            if usuario == "juan":
                mensaje = f"Bienvenido administrador {usuario}"
            elif usuario == "pepe":
                mensaje = f"Bienvenido usuario {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos."
    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run()
