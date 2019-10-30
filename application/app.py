from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask("estudantes")

app.config['MONGO_URI'] = "mongodb+srv://admin:admin@cluster0-andrm.mongodb.net/laura?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route("/")
def hello_world():
    return "Hello World!", 200

@app.route('/estudantes', methods=['GET'])
def listar_estudantes():
	request.args.to_dict()
	modalidade = request.args.get("modalidade")
	dtIni = request.args.get("dtIni")
	dtFim = request.args.get("dtFim")
	estudantes = mongo.db.estudantes
	output = []
	for e in estudantes.find({ 'modalidade' : modalidade, 'data_inicio' : {'$lt' : dtFim, '$gte' : dtIni } }).sort([( 'data_inicio', -1 )]) :
		output.append({'nome' : e['nome'], 'modalidade' : e['modalidade'], 'data_inicio' : e['data_inicio']})
	return jsonify({'result' : output})

@app.route('/cursos', methods=['GET'])
def listar_cursos():
	request.args.to_dict()
	campus = request.args.get("campus")
	
	estudantes = mongo.db.estudantes
	output = []
	for curso in estudantes.distinct('curso', { 'campus' : campus }) :
		output.append(curso)
	return jsonify({'cursos' : output})

@app.route('/alunos', methods=['GET'])
def contar_alunos_campus():
	request.args.to_dict()
	campus = request.args.get("campus")
	dtIni = request.args.get("dtIni")
	dtFim = request.args.get("dtFim")
	
	estudantes = mongo.db.estudantes
	result = estudantes.find({ 'campus' : campus, 'data_inicio' : {'$lt' : dtFim, '$gte' : dtIni } })
	return jsonify({'campus' : campus, 'dataIni' : dtIni, 'dataFim' : dtFim, 'num_alunos' : result.count()})

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
	estudante = request.get_json()
	mongo.db.estudantes.insert_one(estudante)
	return "Estudante inserido", 201
	
@app.route('/aluno', methods=['GET'])
def get_aluno_ra():
	request.args.to_dict()
	ra = request.args.get("ra")
	output = []
	estudantes = mongo.db.estudantes
	for a in estudantes.find({ 'ra' : ra }) :
		output.append({ 'nome' : a['nome'], 'idade_ate_31_12_2016' : a['idade_ate_31_12_2016'], 'ra' : a['ra'], 'campus' : a['campus'], 'municipio' : a['municipio'], 'curso' : a['curso'], 'modalidade' : a['modalidade'], 'nivel_do_curso' : a['nivel_do_curso'], 'data_inicio' : a['data_inicio'] })
	return jsonify(output)

@app.route('/remover', methods=['DELETE'])
def remover():
	request.args.to_dict()
	ra = request.args.get("ra")
	campus = request.args.get("campus")
	response = mongo.db.estudantes.delete_one({ 'ra' : ra, 'campus' : campus })
	if response.deleted_count > 0 :
		return "Estudante deletado", 202
	else :
		return "Erro ao deletar estudante", 404

app.run()