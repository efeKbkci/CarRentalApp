from dataclasses import dataclass, asdict
import uuid

@dataclass
class BaseEntity:
    entity_id:str = str(uuid.uuid4())

    def convert_dict(self) -> dict:
        return asdict(self)
