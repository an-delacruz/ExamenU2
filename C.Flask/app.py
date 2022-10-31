from flask import Flask, abort, jsonify,request,url_for,render_template,redirect,session
from database import db
from flask_migrate import Migrate
from forms import LaptopForm, MouseForm, TecladoForm
from models import Laptop, Mouse, Teclado

app = Flask(__name__)

#Configuración de la bD
USER_DB = "postgres"
PASS_DB = "admin"
URL_DB = "localhost"
NAME_DB = "flask_examen"
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

#Configurar migración
migrate = Migrate()
migrate.init_app(app,db)

#Form
app.config["SECRET_KEY"] = "123"

@app.route("/")
def inicio():
    if 'username' in session:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        usuario = request.form['username']
        session['username'] = usuario
        return redirect(url_for('index'))
    return render_template('login.html')
  
@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('inicio'))

@app.errorhandler(404)
def paginaNoEncontrada(error):
    return render_template('404.html',error=error),404
    

@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')

#Laptops
@app.route("/laptops")
def laptops():
    try:
        if 'username' in session:
            laptops = Laptop.query.all()
            return render_template("/laptops/laptops.html",laptops=laptops)
        else:
            return redirect(url_for('login'))

    except Exception as e:
        return abort(404)

@app.route("/laptops/agregar",methods=['GET','POST'])
def agregarLaptop():
    try:
        if 'username' in session:
            laptop = Laptop()
            laptopForm = LaptopForm(obj=laptop)
            if request.method == 'POST':
                if laptopForm.validate_on_submit():
                    laptopForm.populate_obj(laptop)
                    db.session.add(laptop)
                    db.session.commit()
                    return redirect(url_for('laptops'))
            return render_template('/laptops/agregarLaptop.html',forma=laptopForm)
        else:
            return redirect(url_for('login'))
    except Exception as e:
        return abort(404)

@app.route("/laptops/detalle/<int:id>")
def detalleLaptop(id):
    laptop = Laptop.query.get_or_404(id)
    return render_template('/laptops/detalleLaptop.html',laptop=laptop)

@app.route("/laptops/editar/<int:id>",methods=['GET','POST'])
def editarLaptop(id):
    try:
        if 'username' in session:
            laptop = Laptop.query.get_or_404(id)
    
            laptopForm = LaptopForm(obj=laptop)
            if request.method == 'POST':
                if laptopForm.validate_on_submit():
                    laptopForm.populate_obj(laptop)
                    #update
                    db.session.commit()
                    return redirect(url_for('laptops'))
            return render_template('/laptops/editarLaptop.html',forma=laptopForm)
        else:
            return redirect(url_for('login'))
    except Exception as e:
        return abort(404)

@app.route("/laptops/eliminar/<int:id>")
def eliminarLaptop(id):
    try:
        laptop = Laptop.query.get_or_404(id)
        db.session.delete(laptop)
        db.session.commit()
        return redirect(url_for('laptops'))
    except Exception as e:
        return abort(404)

#Teclados
@app.route("/teclados")
def teclados():
    try:
        if 'username' in session:
            teclados = Teclado.query.all()
            return render_template("/teclados/teclados.html",teclados=teclados)
        else:
            return redirect(url_for('login'))

    except Exception as e:
        return abort(404)

@app.route("/teclados/agregar",methods=['GET','POST'])
def agregarTeclado():
    try:
        if 'username' in session:
            teclado = Teclado()
            tecladoForm = TecladoForm(obj=teclado)
            if request.method == 'POST':
                if tecladoForm.validate_on_submit():
                    tecladoForm.populate_obj(teclado)
                    db.session.add(teclado)
                    db.session.commit()
                    return redirect(url_for('teclados'))
            return render_template('/teclados/agregarTeclado.html',forma=tecladoForm)
        else:
            return redirect(url_for('login'))
    except Exception as e:
        return abort(404)

@app.route("/teclados/editar/<int:id>",methods=['GET','POST'])
def editarTeclado(id):
    try:
        if 'username' in session:
            teclado = Teclado.query.get_or_404(id)
    
            tecladoForm = TecladoForm(obj=teclado)
            if request.method == 'POST':
                if tecladoForm.validate_on_submit():
                    tecladoForm.populate_obj(teclado)
                    #update
                    db.session.commit()
                    return redirect(url_for('teclados'))
            return render_template('/teclados/editarTeclado.html',forma=tecladoForm)
        else:
            return redirect(url_for('login'))
    except Exception as e:
        return abort(404)

@app.route("/teclados/eliminar/<int:id>")
def eliminarTeclado(id):
    try:
        teclado = Teclado.query.get_or_404(id)
        db.session.delete(teclado)
        db.session.commit()
        return redirect(url_for('teclados'))
    except Exception as e:
        return abort(404)




#Mouses
@app.route("/mouses")
def mouses():
    try:
        if 'username' in session:
            mouses = Mouse.query.all()
            return render_template("/mouses/mouses.html",mouses=mouses)
        else:
            return redirect(url_for('login'))

    except Exception as e:
        return abort(404)

@app.route("/mouses/agregar",methods=['GET','POST'])
def agregarMouse():
    try:
        if 'username' in session:
            mouse = Mouse()
            mouseForm = MouseForm(obj=mouse)
            if request.method == 'POST':
                if mouseForm.validate_on_submit():
                    mouseForm.populate_obj(mouse)
                    db.session.add(mouse)
                    db.session.commit()
                    return redirect(url_for('mouses'))
            return render_template('/mouses/agregarMouse.html',forma=mouseForm)
        else:
            return redirect(url_for('login'))
    except Exception as e:
        return abort(404)

@app.route("/mouses/editar/<int:id>",methods=['GET','POST'])
def editarMouse(id):
    try:
        if 'username' in session:
            mouse = Mouse.query.get_or_404(id)
    
            mouseForm = MouseForm(obj=mouse)
            if request.method == 'POST':
                if mouseForm.validate_on_submit():
                    mouseForm.populate_obj(mouse)
                    #update
                    db.session.commit()
                    return redirect(url_for('mouses'))
            return render_template('/mouses/editarMouse.html',forma=mouseForm)
        else:
            return redirect(url_for('login'))
    except Exception as e:
        return abort(404)


@app.route("/mouses/eliminar/<int:id>")
def eliminarMouse(id):
    try:
        mouse = Mouse.query.get_or_404(id)
        db.session.delete(mouse)
        db.session.commit()
        return redirect(url_for('mouses'))
    except Exception as e:
        return abort(404)
