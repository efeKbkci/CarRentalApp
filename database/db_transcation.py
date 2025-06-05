class DBTranscation:
    def __init__(self, connection: DatabaseConnection):
        self.conn = connection.connection
        self.cursor = connection.cursor

    def get_entities(self, table: Table, query: str = "") -> list[dict]:
        sql = f"SELECT * FROM {table.value} {query}"
        try:
            self.cursor.execute(sql)
            columns = [col[0] for col in self.cursor.description]
            rows = self.cursor.fetchall()
            return [dict(zip(columns, row)) for row in rows]
        except Exception as e:
            print("Query error:", e)
            return []

    def add_new_entity(self, table: Table, data: dict) -> bool:
        try:
            keys = ", ".join(data.keys())
            values = ", ".join(["%s"] * len(data))
            sql = f"INSERT INTO {table.value} ({keys}) VALUES ({values})"
            self.cursor.execute(sql, list(data.values()))
            self.conn.commit()
            return True
        except Exception as e:
            print("Insert error:", e)
            return False

    def update_entity(self, table: Table, data: dict) -> bool:
        if "id" not in data:
            print("Update requires 'id' field.")
            return False
        try:
            id_val = data.pop("id")
            set_str = ", ".join([f"{k}=%s" for k in data.keys()])
            sql = f"UPDATE {table.value} SET {set_str} WHERE id = %s"
            self.cursor.execute(sql, list(data.values()) + [id_val])
            self.conn.commit()
            return True
        except Exception as e:
            print("Update error:", e)
            return False

    def delete_entity(self, table: Table, entity_id: str) -> bool:
        try:
            sql = f"DELETE FROM {table.value} WHERE id = %s"
            self.cursor.execute(sql, (entity_id,))
            self.conn.commit()
            return True
        except Exception as e:
            print("Delete error:", e)
            return False
