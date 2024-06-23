"""================================================================================================
Institute....: Universidad Técnica Nacional
Headquarters.: Pacífico
Career.......: Tecnologías de la Información
Period.......: 2-2023
Document.....: clsConexion.py
Goals........: Create data access control with MySQL engine
Professor....: Jorge Ruiz (york)
Student......:
================================================================================================"""
# import mysql library, you must execute 'pip install pymysql' into terminal window
# python -m venv venv

import pymysql.cursors
from data.clsDatos import clsDatos

class clsConexion():
    # Declara las variables para la conexion
    # Recuerde cambiar la dirección y contraseña de su servidor
    servidor = '127.0.0.0'
    basedatos = 'siuuuuuuu'
    usuario = 'admin'
    contra = 'Nube123'

    def __init__(self):
        pass

    def _conectar(self):
        try:
            _conex = pymysql.connect(host=self.servidor,
                                    user=self.usuario,
                                    password=self.contra,
                                    database=self.basedatos,
                                    cursorclass=pymysql.cursors.DictCursor)
        except Exception as err:
            print(err)
        return _conex

    def agregar(self, dato):
        estado = False
        AuxSql = "insert into datos(texto, descripcion) values('{0}','{1}')".format(dato.Texto, dato.Descripcion)
        try:
            _conex = self._conectar()
            with _conex.cursor() as cursor:
                cursor.execute(AuxSql)

            _conex.commit()
            _conex.close()
            estado = True
        except Exception as err:
            print(err)
        return estado

    def editar(self, dato):
        estado = False
        AuxSql = "update datos set texto = '{1}', descripcion = '{2}' where id = {0}".format(dato.ID, dato.Texto,
                                                                                             dato.Descripcion)
        try:
            _conex = self._conectar()
            with _conex.cursor() as cursor:
                cursor.execute(AuxSql)

            _conex.commit()
            _conex.close()
            estado = True
        except Exception as err:
            print(err)
        return estado

    def borrar(self, ide):
        estado = False
        AuxSql = "delete from datos where id = {0}".format(ide)
        try:
            _conex = self._conectar()
            with _conex.cursor() as cursor:
                cursor.execute(AuxSql)

            _conex.commit()
            _conex.close()
            estado = True
        except Exception as err:
            print(err)
        return estado

    def consultar(self, ide=None):
        data = ''
        salida = []

        try:
            _conex = self._conectar()
            with _conex.cursor() as cursor:
                if ide is None:
                    cursor.execute("Select * from datos")
                else:
                    cursor.execute("Select * from datos where id = {0}".format(ide))
                data = cursor.fetchall()

            cursor.close()
            _conex.close()
        except Exception as err:
            print(err)

        for tupla in data:
            salida.append(clsDatos(tupla['id'], tupla['texto'], tupla['descripcion']))

        return salida
