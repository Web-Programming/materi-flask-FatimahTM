from flask import Flask, request, jsonify
from app import app, db
from models import Fakultas, Prodi, Mahasiswa  # Adjust the import based on your directory structure

# Route for creating a new Fakultas
@app.route('/fakultas', methods=['POST'])
def create_fakultas():
    data = request.json
    new_fakultas = Fakultas(nama=data['nama'])
    db.session.add(new_fakultas)
    db.session.commit()
    return jsonify({'message': 'Fakultas created', 'id': new_fakultas.id}), 201

# Route for getting all Fakultas
@app.route('/fakultas', methods=['GET'])
def get_fakultas():
    fakultas_list = Fakultas.query.all()
    return jsonify([{'id': f.id, 'nama': f.nama} for f in fakultas_list]), 200

# Route for updating a Fakultas
@app.route('/fakultas/<int:id>', methods=['PUT'])
def update_fakultas(id):
    data = request.json
    fakultas = Fakultas.query.get_or_404(id)
    fakultas.nama = data['nama']
    db.session.commit()
    return jsonify({'message': 'Fakultas updated'}), 200

# Route for deleting a Fakultas
@app.route('/fakultas/<int:id>', methods=['DELETE'])
def delete_fakultas(id):
    fakultas = Fakultas.query.get_or_404(id)
    db.session.delete(fakultas)
    db.session.commit()
    return jsonify({'message': 'Fakultas deleted'}), 200

# Similar routes can be created for Prodi and Mahasiswa

# Route for creating a new Prodi
@app.route('/prodi', methods=['POST'])
def create_prodi():
    data = request.json
    new_prodi = Prodi(nama=data['nama'], fakultas_id=data['fakultas_id'])
    db.session.add(new_prodi)
    db.session.commit()
    return jsonify({'message': 'Prodi created', 'id': new_prodi.id}), 201

# Route for getting all Prodi
@app.route('/prodi', methods=['GET'])
def get_prodi():
    prodi_list = Prodi.query.all()
    return jsonify([{'id': p.id, 'nama': p.nama, 'fakultas_id': p.fakultas_id} for p in prodi_list]), 200

# Route for updating a Prodi
@app.route('/prodi/<int:id>', methods=['PUT'])
def update_prodi(id):
    data = request.json
    prodi = Prodi.query.get_or_404(id)
    prodi.nama = data['nama']
    prodi.fakultas_id = data['fakultas_id']
    db.session.commit()
    return jsonify({'message': 'Prodi updated'}), 200

# Route for deleting a Prodi
@app.route('/prodi/<int:id>', methods=['DELETE'])
def delete_prodi(id):
    prodi = Prodi.query.get_or_404(id)
    db.session.delete(prodi)
    db.session.commit()
    return jsonify({'message': 'Prodi deleted'}), 200

# Route for creating a new Mahasiswa
@app.route('/mahasiswa', methods=['POST'])
def create_mahasiswa():
    data = request.json
    new_mahasiswa = Mahasiswa(nama=data['nama'], nim=data['nim'], prodi_id=data['prodi_id'])
    db.session.add(new_mahasiswa)
    db.session.commit()
    return jsonify({'message': 'Mahasiswa created', 'id': new_mahasiswa.id}), 201

# Route for getting all Mahasiswa
@app.route('/mahasiswa', methods=['GET'])
def get_mahasiswa():
    mahasiswa_list = Mahasiswa.query.all()
    return jsonify([{'id': m.id, 'nama': m.nama, 'nim': m.nim, 'prodi_id': m.prodi_id} for m in mahasiswa_list]), 200

# Route for updating a Mahasiswa
@app.route('/mahasiswa/<int:id>', methods=['PUT'])
def update_mahasiswa(id):
    data = request.json
    mahasiswa = Mahasiswa.query.get_or_404(id)
    mahasiswa.nama = data['nama']
    mahasiswa.nim = data['nim']
    mahasiswa.prodi_id = data['prodi_id']
    db.session.commit()
    return jsonify({'message': 'Mahasiswa updated'}), 200

# Route for deleting a Mahasiswa
@app.route('/mahasiswa/<int:id>', methods=['DELETE'])
def delete_mahasiswa(id):
    mahasiswa = Mahasiswa.query.get_or_404(id)
    db.session.delete(mahasiswa)
    db.session.commit()
    return jsonify({'message': 'Mahasiswa deleted'}), 200