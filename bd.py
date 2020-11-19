import sqlite3 as sql


class TransactionObject():
    database    = "pedidos.db"
    conn        = None
    cur         = None
    connected   = False
 
    def connect(self):
        TransactionObject.conn      = sql.connect(TransactionObject.database)
        TransactionObject.cur       = TransactionObject.conn.cursor()
        TransactionObject.connected = True
 
    def disconnect(self):
        TransactionObject.conn.close()
        TransactionObject.connected = False
 
    def execute(self, sql, parms = None):
        if TransactionObject.connected:
            if parms == None:
                TransactionObject.cur.execute(sql)
            else:
                TransactionObject.cur.execute(sql, parms)
            return True
        else:
            return False
 
    def fetchall(self):
        return TransactionObject.cur.fetchall()
 
    def persist(self):
        if TransactionObject.connected:
            TransactionObject.conn.commit()
            return True
        else:
            return False


def initDB():
    trans = TransactionObject()
    trans.connect()
    trans.execute("""
        CREATE TABLE IF NOT EXISTS 
        pedidos (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        tamanho TEXT NOT NULL,
        sabor1 TEXT NOT NULL,
        sabor2 TEXT,
        sabor3 TEXT,
        refri TEXT,
        borda TEXT,
        endereco TEXT NOT NULL)
        """)
    trans.persist()
    trans.disconnect()

def insert(nome, tamanho, sabor1, sabor2, sabor3, borda, refri, endereco):
    trans = TransactionObject()
    trans.connect()
    trans.execute("INSERT INTO pedidos VALUES(NULL, ?,?,?,?,?,?,?,?)", (nome, tamanho, sabor1, sabor2, sabor3, borda, refri, endereco))
    trans.persist()
    trans.disconnect()


def view():
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM pedidos")
    rows = trans.fetchall()
    trans.disconnect()
    return rows

# def search(nome="", sobrenome="", email="", cpf=""):
#     trans = TransactionObject()
#     trans.connect()
#     trans.execute("SELECT * FROM pedidos WHERE nome=? or sobrenome=? or email=? or cpf=?", (nome,sobrenome,email, cpf))
#     rows = trans.fetchall()
#     trans.disconnect()
#     return rows
def search(nome="", tamanho="", sabor1="",sabor2="",sabor3="",refri="",borda="",endereco=""):
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM pedidos WHERE nome=? or tamanho=?  or sabor1=?  or sabor2=?  or sabor3=?  or refri=?  or borda=?  or endereco=?" , (nome,tamanho,sabor1,sabor2,sabor3,refri,borda,endereco))
    rows = trans.fetchall()
    trans.disconnect()
    return rows

# def search2(nome):
#     trans = TransactionObject()
#     trans.connect()
#     consulta = "SELECT * FROM pedidos WHERE nome={}".format(nome)
#     trans.execute(consulta)
#     rows = trans.fetchall()
#     trans.disconnect()
#     return rows


def delete(id):
    trans = TransactionObject()
    trans.connect()
    trans.execute("DELETE FROM pedidos WHERE id = ?", (id,))
    trans.persist()
    trans.disconnect()

def update(id, nome, tamanho, sabor1, sabor2, sabor3, borda, refri, endereco):
    trans = TransactionObject()
    trans.connect()
    trans.execute("UPDATE pedidos SET nome =?, tamanho=?, sabor1=?, sabor2=?, sabor3=?, borda=?, refri=?, endereco=? WHERE id = ?",(nome, tamanho, sabor1, sabor2, sabor3, borda, refri, endereco, id))
    trans.persist()
    trans.disconnect()

initDB()


# criando a tabela (schema)