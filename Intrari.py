import os
import shutil
import time
import csv
import MySqlConn

class Intrari():

    def __init__(self,Intrari='Proiect/Intrari', backup_intrari='Proiect/backup_intrari'):
        self.Intrari=os.path.abspath(Intrari)
        self.backup_intrari=os.path.abspath(backup_intrari)
        os.makedirs(self.Intrari,exist_ok=True)
        os.makedirs(self.backup_intrari,exist_ok=True)
        self.db=MySqlConn

    def numar_poarta(self,file_name):
        return int(file_name.split('Poarta')[1].split('.')[0])
    
    def backup(self,file_name):
            intrari=os.path.join(self.intrari,file_name)
            backup=os.path.join(self.backup_intrari,file_name)
            shutil.move(intrari,backup)


    def intrari_noi(self):
        while True:
            files=os.listdir(self.intrari)
            for file_name in files:
                if file_name.startswith("Poarta") and file_name.endswith("csv"):
                    numarPoarta=self.numar_poarta(file_name)
                    self.process_file(file_name,numarPoarta)
                    self.backup(file_name)
                if file_name.startswith("Poarta") and file_name.endswith("txt"):
                    numarPoarta=self.numar_poarta(file_name)
                    self.process_file(file_name,numarPoarta)
                    self.backup(file_name)
            time.sleep(5)

if __name__=="__main__":

    file_processor=Intrari()

    def fisier_nou(self,file_name,numar_poarta):
        file_path=os.path.join(self.intrari,file_name)
        if file_name.endswith(".csv"):
            with open(file_path,'r') as file:
                csv_reader=csv.reader(file)
                header=next(csv_reader, None)
                for row in csv_reader:
                        id_angajat=int(row[0])
                        Data=row[1]
                        Sens=row[2]
                        Poarta=numar_poarta
                        self.db.acces(Poarta,id_angajat,Data,Sens)
        elif file_name.endswith(".txt"):
            with open(file_path,'r') as file:
                for line in file:
                        row=line.strip().split(',')
                        id_angajat=int(row[0])
                        Data=row[1]
                        Sens=row[2]
                        Poarta=numar_poarta
                        self.db.acces(Poarta,id_angajat,Data,Sens)
        





    