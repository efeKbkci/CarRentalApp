class DBTranscation():
    def __init__(self,connection: DatabaseConnection):
        pass
    def get_entities(self,table :Table, query:str) -> list[BaseEntity]:
        pass
    def add_new_entity(self,table: Table, data: dict) -> bool:
        pass
    def update_entity(self,table: Table, data:dict) -> bool:
        pass
    def delete_entity(self,table : Table, entity_id:str) -> bool:
        pass
