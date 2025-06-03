class DBTranscation():
    def get_entities(self,table :Table, query:str) -> list[BaseEntity]:
        pass
    def add_new_entity(table: Table, query : str) -> bool:
        pass
    def update_entity(table: Table, data:dict) -> bool:
        pass
    def delete_entity(table : Table, entity_id:str) -> bool:
        pass
