from dataclasses import dataclass, asdict, field
import uuid

# If you didn't use __post_init__ method, you'd get 'non-default argument 'user_id' follows default argument 'entity_id'' error.
# field(init=False): Don't include this feature in the __init__ function
# __post_init__(): After all features get initialized, call this method. 
# The purpose of this approach was to initialize the entity_id attribute after other attributes

@dataclass
class BaseEntity:
    id: str = field(init=False)

    def __post_init__(self):
        self.id = str(uuid.uuid4())

    def convert_dict(self) -> dict:
        return asdict(self)
