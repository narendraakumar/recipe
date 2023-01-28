from enum import Enum
class ExtendedEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class FileFormat(ExtendedEnum):
    CSV = ".csv"
    ZIP = ".zip"
    TXT = ".txt"
    JSON = ".json"
    GAN_ZIP = ".zip"

print(FileFormat.list)