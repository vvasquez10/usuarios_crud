from usuarios_app.config.mysqlconnection import connectToMySQL

class Usuario():
    def __init__(self, id, first_name, last_name, email, created_at, updated_at):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def getAllUsers(cls):
        query = "SELECT * FROM users;"
        result_fromDB = connectToMySQL( "users" ).query_db( query )
        listaUsuarios = []
        for usuario in result_fromDB:
            listaUsuarios.append( Usuario( usuario["id"], usuario["first_name"], usuario["last_name"], usuario["email"], usuario["created_at"], usuario["updated_at"]) )
        return listaUsuarios
    
    @classmethod
    def creaNuevoUsuario(cls, dataUsuario): #no puedo enviar un objeto porque estaría incompleto, sino que le mando un dic con los datos que tengo
        query = "INSERT INTO users(first_name, last_name, email) VALUES(%(first_name)s, %(last_name)s, %(email)s);"        
        resultado = connectToMySQL( "users" ).query_db( query, dataUsuario )
        return resultado # Devuelve un ID
    
    @classmethod
    def buscaUsuario(cls, userID): # Devuelve un objeto Usuario
        dataUsuario = {
            'id' : userID
        }
        query = "SELECT * FROM users WHERE id = %(id)s;"        
        resultado = connectToMySQL( "users" ).query_db( query, dataUsuario )
        usuarioEncontrado = Usuario(resultado[0]["id"], resultado[0]["first_name"], resultado[0]["last_name"], resultado[0]["email"], resultado[0]["created_at"], resultado[0]["updated_at"])
        return usuarioEncontrado
    
    @classmethod
    def updateUsuario(cls, usuarioAeditar):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        resultado = connectToMySQL( "users" ).query_db( query, usuarioAeditar )
        return resultado

    @classmethod
    def eliminarUsuario(cls, usuarioAeliminar):
        query = "DELETE FROM users WHERE id = %(id)s;"
        resultado = connectToMySQL( "users" ).query_db( query, usuarioAeliminar )
        return resultado


