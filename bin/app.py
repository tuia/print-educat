import web
import pyqrcode 
import time

urls = (
  '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class Index(object):
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(name="Nome", cpf="CPF", school="school", campus="campus", building="building", classroom="classroom", level="level", course="course", test="test" )
        dadosAluno = "%s, %s" % (form.name, form.cpf)

        nomeAluno = "%s" % form.name
        imagemAluno = "%s.svg" % form.name
        cpfAluno = "%s" % form.cpf
        levelAluno = "%s" % form.level

        schoolAluno = "%s" % form.school
        courseAluno = "%s" % form.course
        testAluno = "%s" % form.test
        campusAluno = "%s" % form.campus
        buildingAluno = "%s" % form.building
        classroomAluno = "%s" % form.classroom
        
        number = pyqrcode.create( dadosAluno )
        number.svg( 'static/img/students-codes/' + nomeAluno + '.svg', scale=8)

        return render.index(nomeAluno = nomeAluno, cpfAluno = cpfAluno, campusAluno = campusAluno, levelAluno = levelAluno, schoolAluno = schoolAluno, imagemAluno = imagemAluno, courseAluno = courseAluno, buildingAluno = buildingAluno, classroomAluno = classroomAluno, testAluno = testAluno, dadosAluno = dadosAluno)

if __name__ == "__main__":
    app.run()



