from data.modelo.hospitales import Hospital

class DaoHospitales:
    def get_all(self,db) -> list[Hospital]:
        cursor = db.cursor()

        cursor.execute("SELECT * FROM hospitales")

        equipos_en_db = cursor.fetchall()  # Cambio aquí: antes era hospital_en_db
        equipos : list[Hospital]=list()
        for equipo in equipos_en_db:
            hospital = Hospital(equipo[0], equipo[1], equipo[2])
            equipos.append(hospital)
        cursor.close()
        return equipos

    def get_num(self, db, numero_pacientes : int):
        cursor = db.cursor()
        sql = ("SELECT * FROM hospitales WHERE numero_pacientes > (%s)")
        data = (numero_pacientes,)
        cursor.execute(sql,data)
        equipos_en_db = cursor.fetchall()
        equipos : list[Hospital]=list()
        for equipo in equipos_en_db:
            hospital = Hospital(equipo[0], equipo[1], equipo[2])
            equipos.append(hospital)
        cursor.close()
        return equipos

    def insert(self, db, nombre : str):
        cursor = db.cursor()
        sql = ("INSERT INTO hospitales (nombre) values (%s)")
        data = (nombre,)
        cursor.execute(sql, data)
        # cursor.execute(f"INSERT INTO artistas (nombre) VALUES ('{nombre}')")
        db.commit()
        cursor.close()

    def delete(self, db, id : str):
        cursor = db.cursor()
        sql = ("DELETE FROM hospitales where id = (%s)")
        data = (id,)
        cursor.execute(sql,data)
        # cursor.execute(f"INSERT INTO artistas (nombre) VALUES ('{nombre}')")
        db.commit()
        cursor.close()

    def update(self, db, hospital_id: str, nuevo_numero_pacientes: int):
        cursor = db.cursor()
        sql = ("UPDATE hospitales SET numero_pacientes = %s WHERE id = %s")
        data = (nuevo_numero_pacientes, hospital_id)
        cursor.execute(sql, data)
        db.commit()
        cursor.close()