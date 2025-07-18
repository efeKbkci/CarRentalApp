from .table import Table

from model import User, Car, Appointment

from dataclasses import asdict
import sqlite3
import os

class DBTransaction:
    table_entity_dict = {Table.USER: User, Table.CAR: Car, Table.APPOINTMENTS: Appointment}

    def __init__(self):
        db_path = os.path.join("database", "car_rental.db") # operating system independent
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def get_entities(self, table: Table, *filter):
        conditions = list() 
        values = list()
        for column, operand, value in filter:
            conditions.append(f"{column} {operand} ?")
            values.append(value)

        where_str = " AND ".join(conditions) 
        query = f"SELECT * FROM {table.value} WHERE {where_str}" if conditions else f"SELECT * FROM {table.value}"

        self.cursor.execute(query, values)
        rows = self.cursor.fetchall()

        entity = self.table_entity_dict.get(table) # User, Car, Appointment
        return [entity(*row) for row in rows] 

    def get_entity(self, table: Table, filter: dict):
        columns = " AND ".join([f"{key} = ?" for key in filter.keys()])
        values = tuple(filter.values())
        self.cursor.execute(f"SELECT * FROM {table.value} WHERE {columns}", values)
        
        row = self.cursor.fetchone()
        if row is None:
            return None
        
        entity_cls = self.table_entity_dict.get(table)
        return entity_cls(*row)
         
    def add_new_entity(self, table: Table, entity: object):
        data = asdict(entity) 
        columns = ", ".join(data.keys()) # entity_id, name, email
        placeholder = ", ".join("?" * data.__len__()) # ?, ?, ?
        values = tuple(data.values()) # 123-dth-51-cv, efe, efkanefekabakcii@gmail.com
        
        try:
            self.cursor.execute(f"INSERT INTO {table.value} ({columns}) VALUES ({placeholder})", values)
            self.conn.commit()
            return True
        except sqlite3.IntegrityError as err:
            return False

    def update_entity(self, table: Table, updated_entity: object):
        data = asdict(updated_entity)
        columns = ", ".join([key + " = ?" for key in list(data.keys())[:-1]]) # "name = ?, email = ?"
        self.cursor.execute(f"UPDATE {table.value} SET {columns} WHERE entity_id = ?", tuple(data.values()))
        self.conn.commit()

    def delete_entity(self, table:Table, entity_id: str):
        self.cursor.execute(f"DELETE FROM {table.value} WHERE entity_id = ?", (entity_id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()