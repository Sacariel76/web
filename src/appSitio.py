from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

from data.clsConexion import clsConexion
from data.clsDatos import clsDatos


conex = clsConexion()


@app.route('/')
def index():
    return render_template('index.html', datos=conex.consultar())


@app.route('/agregar', methods=['GET'])
def agregar():
    return render_template('agregar.html')


@app.route('/exec_agregar', methods=['POST'])
def exec_agregar():
    if conex.agregar(clsDatos(0, request.form['txtTexto'], request.form['txtDescrip'])):
        app.logger.debug("Datos almacenados correctamente")
    else:
        app.logger.debug("Se presentó un problema con los datos")
    return redirect(url_for("index"))


@app.route('/modificar/<int:ide>', methods=['GET'])
def modificar(ide):
    return render_template('modificar.html', datos=conex.consultar(ide))


@app.route('/exec_modificar', methods=['POST'])
def exec_modificar():
    if conex.editar(clsDatos(request.form['txtID'], request.form['txtTexto'], request.form['txtDescrip'])):
        app.logger.debug("Datos modificados correctamente")
    else:
        app.logger.debug("Se presentó un problema con los datos")
    return redirect(url_for('index'))


@app.route('/exec_eliminar/<int:ide>', methods=['GET'])
def exec_eliminar(ide):
    if conex.borrar(ide):
        app.logger.debug("Datos eliminado correctamente")
    else:
        app.logger.debug("Se presentó un problema con los datos")
    return redirect(url_for('index'))


@app.route('/acerca')
def acerca():
    return render_template('acercade.html')


def creaBase():
    try:
        _conex = conex._conectar()
        with _conex.cursor() as cursor:
            cursor.execute("create table if not exists datos(id int not null auto_increment primary key, texto varchar(50) not null, descripcion varchar(100) not null)")

        _conex.commit()
        _conex.close()
    except Exception as err:
        print(err)

if __name__ == '__main__':
    creaBase()
    app.run(host='0.0.0.0', port=5001, debug=False)
