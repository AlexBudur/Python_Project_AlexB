from datetime import datetime
from Database import *
import csv
from MySqlConn import *

class Chiulangii():
    def __init__(self):
        self.db=MySqlConn

def afisare_chiulangii(self):
    query="SELECT CONVERT(Data,Date) as Date, MID(Data,12,2) AS Ora, Sens, Poarta, id_angajat from SRL_Angajati.Acces WHERE Data=CURRENT_DATE();"
    self.db.cursor.execute(query)
    results=self.db.cursor.fetchfall()
    self.db.connection.commit()
    return results
    print(query)


# convert string to date

# data=datetime.strptime(Data, '%m/%d/%y').date()
# ora=datetime.strptime(Data, '%H')

