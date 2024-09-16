import mysql.connector

class MySqlConn():
    def __init__(self):
        self.mydb=mysql.connector.connect(host='localhost',
                                          user='root',
                                          password='root',
                                          database='SRL_Angajati')
        self.cursor=self.mydb.cursor()

    def select(self,query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insert(self,query):
        self.cursor.execute(query)
        self.mydb.commit()

    def update(self,query):
        self.cursor.execute(query)
        self.mydb.commit()
    
    def acces(self,Poarta,id_angajat,Data,Sens):
        query=f'INSERT INTO SRL_Angajati.Acces VALUES (%s, %s, %s, %s, %s);'
        values=(Poarta,id_angajat,Data,Sens)
        self.cursor.execute(query,values)
        self.connection.commit()
    
    def close(self):
        self.cursor.close()
        self.connection.close()


    # def adaugare_utilizator(self,id_angajat,nume,prenume,companie,id_manager):
    #     query=f'INSERT INTO SRL_Angajati.Utilizatori VALUES (%s, %s, %s, %s, %s);'
    #     values=(id_angajat,nume,prenume,companie,id_manager)
    #     self.cursor.execute(query,values)
    #     self.connection.commit()
    #     return "Utilizator adaugat"

