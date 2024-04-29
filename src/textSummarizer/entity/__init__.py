#update Entity
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Dataingestionconfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class Datavalidationconfig:
    root_dir: Path
    STATUS_FILE: str
    required_file: list
