from .table import Table
from model import User, Car, Appointment

class DBTransaction:
    """
    Represents database transactions.
    """

    def __init__(self) -> None:
        """
        Initializes the DBTransaction with a database connection.
        """
        ...

    def get_entities(self, table: Table, *filter) -> list:
        """
        Retrieves entities from the database based on the specified table and filter.

        :param table: The table from which to retrieve entities.
        :param filter: A list containing the filters. First index is column_name, second operand, third value
                       Example: [("gas_type", "=", "gasoline"), ("price", "<=", 50))].
        :return: A list of entities matching the filter criteria.
        """
        ...

    def get_entity(self, table: Table, filter: dict) -> 'User | Car | Appointment | None':
        """
        Retrieves a single entity from the database based on the specified table and filter.

        :param table: The table from which to retrieve the entity.
        :param filter: A dictionary containing the filter. 
                       It contains a unique column name and value such as “email”, “entity_id”.

                       Example: get_entity(Table.CAR, {"entity_id":"0123-trwd"}) -> SELECT * FROM car WHERE entity_id = ?, ("0123-twrd")
        :return: The entity matching the filter, or None if not found.
        """
        ...

    def add_new_entity(self, table: Table, entity: object) -> bool:
        """
        Adds a new entity to the database.

        :param table: The table in which to add the new entity.
        :param entity: An entity from model package. It can be User, Car or Appointment
        """
        ...
    
    def update_entity(self, table: Table, updated_entity: object) -> None:
        """
        Updates an existing entity in the database.

        :param table: The table containing the entity to update.
        :updated_entity: An entity from model package. It can be User, Car or Appointment
        """
        ...
    def delete_entity(self, table: Table, entity_id: str) -> None:
        """
        Deletes an entity from the database.
        :param table: Table to delete the entity 
        :param entity_id: The ID of the entity to delete.
        """
        ...
    def close_connection(self) -> None:
        """
        Closes database connection and prevents any memory leak. 
        """
        ...