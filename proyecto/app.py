from flask import Flask, render_template, request #importa la libreria flask, el render template es para redireccionar


app = Flask(__name__,template_folder='template') #inicio de la libreia

#index
@app.route('/') # funcion desde flask
def home(): #etiqueta para definir la funcion
    return render_template ("home.html") #se redirecciona al archivo entre las comillas
#home (juan esteban)

@app.route('/login') # funcion desde flask
def login(): #etiqueta para definir la funcion
    return render_template ("login.html") #se redirecciona al archivo entre las comillas
#el login (julian)


@app.route('/tc') # funcion desde flask
def tc(): #etiqueta para definir la funcion
    return render_template ("t_c.html") #se redirecciona al archivo entre las comillas
#terminos y condiciones (juan pablo)

@app.route('/perfilcliente') # funcion desde flask
def perfilcliente(): #etiqueta para definir la funcion
    return render_template ("perfilcliente.html") #se redirecciona al archivo entre las comillas
# (harold)



if __name__ == "__main__": #se verifica que el codigo esea ejecuta desde el programa principal

    app.run(debug=True) #se usa para iniciar la pagina web
