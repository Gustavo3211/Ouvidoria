import mysql.connector
from config import user, password, host, database

def conectar():
  cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)

 
  #funções mysql 
  # pesquisa: SELECT [coluna] from [tabela] where [tabela] = %s
  # inserir: INSERT INTO [tabela]([coluna],[coluna]) Values (%s, %s)
  # editar: UPDATE SET [coluna]=%s,[coluna2]=%s where ID = %s
  return cnx

def desligarbanco(cnx):
  cnx.close()

def inserirbanco(cnx,valor1,valor2):
  cursor = cnx.cursor()
        
  query = ("INSERT INTO ocorrencia "
            "(oco, tipo) "
            "VALUES (%s, %s)")
        
  inserir_ocorrencia = (valor1, valor2)

  cursor.execute(query, inserir_ocorrencia)
  cnx.commit()
  print("Ocorrencia Inserida com Sucesso.")
  cursor.close()

def listarbanco(cnx):
  cursor = cnx.cursor()
  query = ("SELECT ID, tipo, oco FROM ocorrencia")
  cursor.execute(query)
  result = cursor.fetchall() #cria uma tupla com os dados do banco
  for i in result:
    if i[1] == 1:
      tipo="Elogio"
    elif i[1] == 2:
      tipo="Reclamação"
    elif i[1]==3:
      tipo="Sugestão"
    else:
      tipo="Erro ao pegar o tipo da ocorrencia."
    print("N° Ocorrencia: {} ) - Tipo: {} | Ocorrencia: {}".format(i[0],tipo,i[2]))#pega os valores da tupla usando format e imprime.
  if len(result) == 0:
    print("Nao existem ocorrencias")
  cursor.close()

def deletabanco(cnx, valor1):
  cursor = cnx.cursor()
        
  query = ("DELETE FROM `ocorrencia`"
           "WHERE ID = %s")
  try: 
    deletar = (valor1,)#MYSQL.connect só funciona com tuplas, então criamos uma com apenas um valor.

  except:
    print("Houve um erro")

  else:
    print("Ocorrencia deletada com Sucesso.")
  finally:
    cursor.execute(query, deletar)
    cnx.commit()
    cursor.close()

def truncate(cnx):
  cursor = cnx.cursor()
  query = "TRUNCATE TABLE ocorrencia"
  cursor.execute(query)
  cursor.close()
  print("A Tabela de ocorrencia foi resetada.")

def pesquisarbanco(cnx,valor1):
  cursor = cnx.cursor()
  query = ("SELECT ID, tipo, oco FROM ocorrencia where tipo = %s")
  pesquisar =(valor1,)
  cursor.execute(query, pesquisar)
  result = cursor.fetchall() #cria uma tupla com os dados do banco
  for i in result:
    if i[1] == 1:
      tipo="Elogio"
    elif i[1] == 2:
      tipo="Reclamação"
    elif i[1]==3:
      tipo="Sugestão"
    else:
      tipo="Erro ao pegar o tipo da ocorrencia."
    print("N° Ocorrencia: {} ) - Tipo: {} | Ocorrencia: {}".format(i[0],tipo,i[2]))#pega os valores da tupla usando format e imprime.
  if len(result) == 0:
    print("Esta ocorrencias não existe")
  cursor.close()



  