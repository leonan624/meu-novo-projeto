import psycopg2 as con
# abrindo conexão
conexao = con.connect(database="BaseDeDados",
                      user="leonan",
                      password="mg8851",
                      host="127.0.0.1",
                      port="5432"
                      )
# adiquirindo um cursor
cursor = conexao.cursor()
# executando comandos SQL
comando ='''SELECT * FROM pessoa;'''
cursor.execute(comando)

pp = cursor.fletchall()
for table in pp:
    print("nome: ", table[1])
    print("idade: ", table[2])
    print("sexo: ", table[3])
    print("pais: ", table[4])
    print("\n")




# encerrando a operação
conexao.commit()
cursor.close()
conexao.close()