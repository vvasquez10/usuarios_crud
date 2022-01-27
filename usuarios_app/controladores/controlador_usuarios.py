from usuarios_app import app
from flask import render_template, redirect, request, session
from usuarios_app.modelos.Usuario import Usuario

@app.route( '/', methods=['GET'] )
def despliegaUsuarios():
    return render_template( "all_users.html", usuarios=Usuario.getAllUsers())

@app.route( '/newUser', methods=['GET'] )
def despliegaNuevoUsuario():
    return render_template( "new_user.html")

@app.route( '/createUser', methods=['POST'] )
def creaUsuario():
    nuevoUsuario = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]        
    }
    
    resultado = Usuario.creaNuevoUsuario( nuevoUsuario )
    print(resultado)

    return redirect("/")