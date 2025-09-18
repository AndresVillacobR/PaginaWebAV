from flask import Flask, render_template

app = Flask(__name__)

# Ruta principal -> index.html
@app.route('/index')
def index():
    return render_template('index.html')

# Ruta -> base.html
@app.route('/base')
def base():
    return render_template('base.html')

# Ruta -> mision.html
@app.route('/mision')
def mision():
    return render_template('mision.html')

# Ruta -> vision.html
@app.route('/vision')
def vision():
    return render_template('vision.html')

# Ruta -> sedes.html
@app.route('/sedes')
def sedes():
    return render_template('sedes.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
