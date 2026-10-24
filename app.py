from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/estudiantes/api/v1/hola', methods=['GET'])
def hola():
    return jsonify("hola mundo")

@app.route('/estudiantes/api/v1/saludo', methods=['GET'])
def saludo():
    data = request.get_json(silent=True) or {}
    nombre = data.get('nombre') or request.args.get('nombre')
    apellido = data.get('apellido', '') or request.args.get('apellido', '')

    if not nombre:
        return jsonify({"mensaje": "Debe de ingresar el nombre del estudiante"}), 400

    nombre_completo = f"{nombre} {apellido}".strip()
    return jsonify({"saludo": f"Hola {nombre_completo}"})



# 1. Obtener todos los estudiantes (GET)
@app.route('/estudiantes', methods=['GET'])
def obtener_estudiantes():
    return jsonify({
        "mensaje": "Lista de estudiantes obtenida correctamente.",
        "estudiantes": [
            "Ana",
            "Carlos",
            "María"
        ]
    })

# 2. Agregar un estudiante (POST)
@app.route('/estudiantes', methods=['POST'])
def agregar_estudiante():
    data = request.get_json(silent=True) or {}
    nombre = data.get('nombre', 'Pedro')
    return jsonify({
        "mensaje": "Estudiante agregado correctamente.",
        "estudiante": nombre
    }), 201

# 3. Actualizar un estudiante (PUT)
@app.route('/estudiantes/<int:id_estudiante>', methods=['PUT'])
def actualizar_estudiante(id_estudiante):
    data = request.get_json(silent=True) or {}
    return jsonify({
        "mensaje": "Estudiante actualizado correctamente.",
        "id": id_estudiante
    })

# 4. Eliminar un estudiante (DELETE)
@app.route('/estudiantes/<int:id_estudiante>', methods=['DELETE'])
def eliminar_estudiante(id_estudiante):
    return jsonify({
        "mensaje": "Estudiante eliminado correctamente.",
        "id": id_estudiante
    })

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)