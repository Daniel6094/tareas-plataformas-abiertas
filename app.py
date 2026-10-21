from flask import Flask, jsonify, request

app = Flask(__name__)

# Endpoint 1: /estudiantes/api/v1/hola
@app.route('/estudiantes/api/v1/hola', methods=['GET'])
def hola():
    return jsonify("hola mundo")

# Endpoint 2: /estudiantes/api/v1/saludo
@app.route('/estudiantes/api/v1/saludo', methods=['GET'])
def saludo():
    # Obtener los datos enviados en el Body (JSON) o por parámetros URL
    data = request.get_json(silent=True) or {}
    nombre = data.get('nombre') or request.args.get('nombre')
    apellido = data.get('apellido', '') or request.args.get('apellido', '')

    # Validar si se envió el nombre
    if not nombre:
        return jsonify({"mensaje": "Debe de ingresar el nombre del estudiante"}), 400

    nombre_completo = f"{nombre} {apellido}".strip()
    return jsonify({"saludo": f"Hola {nombre_completo}"})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)