from dataclasses import dataclass


@dataclass
class MongoInstance:
    name: str = ""
    host: str = ""
    port: str = ""

    def __init__(self, name: str):
        self.name = name
