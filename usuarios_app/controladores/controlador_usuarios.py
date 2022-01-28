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
    Usuario.creaNuevoUsuario( nuevoUsuario )
    return redirect("/")

@app.route( '/showUser/<int:id>', methods=['GET'] )
def muestraUsuario(id):    
    miUsuario = Usuario.buscaUsuario(id)
    return render_template("show_user.html", usuario=miUsuario)

@app.route( '/editUser/<int:id>', methods=["GET"] )
def editarUsuario( id ):
    """
    usuarioAEditar = {
        "id" : userID
    }
    """
    usuarioAeditar = Usuario.buscaUsuario( id )
    return render_template( "editarUsuario.html", usuario=usuarioAeditar)

@app.route( '/updateUser/<int:id>', methods=["POST"] )
def actualizarUsuario( id ):
    usuarioAEditar = {
        "id" : id,
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    Usuario.updateUsuario( usuarioAEditar )
    
    return redirect( '/' )

@app.route( '/removeUser/<int:id>', methods=["POST"] )
def eliminarUsuario( id ):
    usuarioAEliminar = {
        "id": id
    }
    Usuario.eliminarUsuario( usuarioAEliminar )

    return redirect( '/' )