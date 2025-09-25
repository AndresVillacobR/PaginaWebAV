from flask import Flask, render_template, request , redirect, url_for
import conexion as db

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/mision', methods=['GET', 'POST'])
def mision():
    codsede = ''
    desede = ''
    if request.method == 'POST':
        codsede = request.form.get('codsede', '')
        desede = request.form.get('desede', '')
        print(f"Código de Sede: {codsede}, Descripción de Sede: {desede}")

        conn = db.create_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO ciudad (idCiudad, Descripcion) VALUES (%s, %s)"
        data = (codsede, desede)
        try:
            cursor.execute(sql, data)
            conn.commit()
            print("Registro insertado exitosamente")
        except Exception as e:
            print(f"Error al insertar el registro: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("Metodo GET recibido")

    return render_template('mision.html', codsede=codsede, desede=desede)


@app.route('/vision')
def vision():
    return render_template('vision.html')


@app.route('/sedes', methods=['GET', 'POST'])
def sedes():
    if request.method == 'POST':
        codsede = request.form.get('codsede', '')
        desede = request.form.get('desede', '')
        dirsede = request.form.get('dirsede', '')
        idciudad = request.form.get('IdCiudad', '')
        desciudad = request.form.get('Descripcion', '')

        print(f"Código de Sede: {codsede}, Descripción: {desede}, Dirección: {dirsede}, Ciudad: {idciudad}-{desciudad}")

        conn = db.create_connection()
        cursor = conn.cursor()
        try:
           
            sql_ciudad = "INSERT IGNORE INTO ciudad (IdCiudad, Descripcion) VALUES (%s, %s)"
            cursor.execute(sql_ciudad, (idciudad, desciudad))

            sql_sede = "INSERT INTO sede (IdSede, Descripcion, Direccion, IdCiudad) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql_sede, (codsede, desede, dirsede, idciudad))

            conn.commit()
            print("Sede y ciudad agregadas exitosamente")
        except Exception as e:
            print(f"Error al insertar la sede: {e}")
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('listasedes'))

    return render_template('sedes.html')

@app.route('/sedesok', methods=['GET', 'POST'])
def sedesok():
    if request.method == 'POST':
        codsede = request.form.get('codsede', '')
        desede = request.form.get('desede', '')
        dirsede = request.form.get('dirsede', '')
        idciudad = request.form.get('IdCiudad', '')
        desciudad = request.form.get('Descripcion', '')

        print(f"Código de Sede: {codsede}, Descripción: {desede}, Dirección: {dirsede}, Ciudad: {idciudad}-{desciudad}")

        conn = db.create_connection()
        cursor = conn.cursor()
        try:
           
            sql_ciudad = "INSERT IGNORE INTO ciudad (IdCiudad, Descripcion) VALUES (%s, %s)"
            cursor.execute(sql_ciudad, (idciudad, desciudad))

            sql_sede = "INSERT INTO sede (IdSede, Descripcion, Direccion, IdCiudad) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql_sede, (codsede, desede, dirsede, idciudad))

            conn.commit()
            print("Sede y ciudad agregadas exitosamente")
        except Exception as e:
            print(f"Error al insertar la sede: {e}")
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('sedesok.html'))


@app.route('/listasedes', methods=['GET'])
def listasedes():
    conn = db.create_connection()
    cursor = conn.cursor()
    sql = """
        SELECT 
            s.IdSede,
            s.Descripcion AS DescripcionSede,
            s.Direccion,
            c.IdCiudad,
            c.Descripcion AS DescripcionCiudad
        FROM sede s 
        INNER JOIN ciudad c ON s.IdCiudad = c.IdCiudad
    """
    sedes = []
    try:
        cursor.execute(sql)
        sedes = cursor.fetchall()
        print("Registros obtenidos exitosamente")
    except Exception as e:
        print(f"Error al obtener los registros: {e}")
    finally:
        cursor.close()
        conn.close()

    return render_template('listasedes.html', sedes=sedes)


@app.route('/ciudades', methods=['GET', 'POST'])
def ciudades():
    if request.method == 'POST':
        idCiudad = request.form.get('idCiudad', '')
        descCiudad = request.form.get('descCiudad', '')

        print(f"Código de ciudad: {idCiudad}, Descripción: {descCiudad}")

        conn = db.create_connection()
        cursor = conn.cursor()
        
        sql = "INSERT INTO ciudad (idCiudad, Descripcion) VALUES (%s, %s)"
        data = (idCiudad, descCiudad)
        try:
            cursor.execute(sql, data)
            conn.commit()
            print("Ciudad agregada exitosamente")
        except Exception as e:
            print(f"Error al insertar la ciudad: {e}")
        finally:
            cursor.close()
            conn.close()

    return render_template('ciudades.html')

@app.route('/ciudadesok', methods=['GET', 'POST'])
def ciudadesok():   
    if request.method == 'POST':
        idCiudad = request.form.get('idCiudad', '')
        descCiudad = request.form.get('descCiudad', '')

        print(f"Código de ciudad: {idCiudad}, Descripción: {descCiudad}")

        conn = db.create_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO ciudad (idCiudad, Descripcion) VALUES (%s, %s)"
        data = (idCiudad, descCiudad)
        try:
            cursor.execute(sql, data)
            conn.commit()
            print("Ciudad agregada exitosamente")
        except Exception as e:
            print(f"Error al insertar la ciudad: {e}")
        finally:
            cursor.close()
            conn.close()

    return render_template('ciudadesok.html')


@app.route('/listaciudades', methods=['GET', 'POST'])
def listaciudades():  
    conn = db.create_connection()
    cursor = conn.cursor()
    sql = "SELECT idCiudad, Descripcion FROM ciudad"  
    ciudades = []
    try:
        cursor.execute(sql)
        ciudades = cursor.fetchall()  
        print("Registros obtenidos exitosamente")
    except Exception as e:
        print(f"Error al obtener los registros: {e}")
    finally:
        cursor.close()
        conn.close()

    return render_template('listaciudades.html', ciudades=ciudades)

@app.route('/eliminar/<codsede>', methods=['GET' , 'POST'])
def eliminar(codsede):
    
    if validar == True:
        
        conn = db.create_connection()
        cursor = conn.cursor()
        sql = "DELETE FROM sede WHERE IdSede = %s"
        try:
            cursor.execute(sql, (codsede,))
            conn.commit()
            print("Registro eliminado exitosamente")
        except Exception as e:
            print(f"Error al eliminar el registro: {e}")
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('listasedes'))
    else:
        return redirect(url_for('listasedes'))

@app.route('/editar/<codsede>', methods=['GET', 'POST'])
def editar(codsede):   
    conn= db.create_connection()
    cursor= conn.cursor()   
    sql= "SELECT IdSede, Descripcion, Direccion, IdCiudad FROM sede WHERE IdSede= %s"
    try:
        cursor.execute(sql, (codsede,))
        sede= cursor.fetchone()
        print("Registro obtenido exitosamente") 
    except Exception as e:
        print(f"Error al obtener el registro: {e}")
    finally:
        cursor.close()
        conn.close()    
        
    return render_template('listasedes', sede=sede)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


@app.route('/editar/<codsede>', methods=['GET', 'POST'])
def editar(codsede):
    conn = db.create_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        desede = request.form['desede']
        dirsede = request.form['dirsede']

        sql = "UPDATE sede SET descripcion = %s, direccion = %s WHERE IdSede = %s"
        data = (desede, dirsede, codsede)

        try:
            cursor.execute(sql, data)
            conn.commit()
            print("✅ Registro actualizado correctamente")
        except Exception as e:
            print(f"❌ Error al actualizar el registro: {e}")
        finally:
            cursor.close()
            conn.close()
            return redirect('/listasedes')

    else:
        sql = "SELECT descripcion, direccion FROM sede WHERE IdSede = %s"
        try:
            cursor.execute(sql, (codsede,))
            sede = cursor.fetchone()
            print("✅ Registro obtenido correctamente")
        except Exception as e:
            print(f"❌ Error al obtener el registro: {e}")
            sede = None
        finally:
            cursor.close()
            conn.close()

        if sede:
            return render_template(
                'editar.html',
                codsede=codsede,
                desede=sede[0],
                dirsede=sede[1]
            )
        else:
            return "Sede no encontrada", 404

