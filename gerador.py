import pyqrcode
from inscritos import *

def remove_mascara(cpf):
	cpf_sem_mascara = ''
	for c in cpf:
		if c not in '.-':
			cpf_sem_mascara += c

	return cpf_sem_mascara


with open("provas/index.html") as f:
	template = f.read()
	
for inscrito in inscritos:
	prova = template.replace("{{nome}}", inscrito['nome'])
	prova = prova.replace("{{cpf}}", inscrito['cpf'])

	cpf = remove_mascara(inscrito['cpf'])

	inscrito_qrcode = pyqrcode.create('http://url.que.sera.disponibilizada.no.qrcode/cpf=' + cpf)
	inscrito_qrcode.svg('provas/img/students-codes/' + cpf + '.svg')

	with open('provas/' + cpf + '.html', 'w') as f:
		f.write(prova)
