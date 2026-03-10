from flask import Flask, render_template

app = Flask(__name__)


# Готовимся к миссии
@app.route('/')
@app.route('/index')
def index():
    user = "USER"
    return render_template('index.html', title='Заготовка',
                           username=user)


# Тренировки в полёте
@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', title='Тренировки',
                           profession=prof)


# Список профессий
@app.route('/list_prof/<viv>')
def list_prof(viv):
    return render_template('list_prof.html', title='Профессии',
                           display=viv)


# По каютам!
@app.route('/distribution')
def distribution():
    members = ["Ридли Скотт", "Энди Уир", "Марк Уотни", "Венката Капур", "Тедди Сандерс", "Шон Бин"]
    return render_template('distribution.html', title='Каюты',
                           members=members)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
