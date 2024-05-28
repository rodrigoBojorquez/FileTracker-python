from abc import ABC, abstractmethod
from typing import Any

class FileTrackerRepositoryBase(ABC):
    @abstractmethod
    async def store_document_by_url(self, url: str, output_path: str) -> Any:
        pass

    @abstractmethod
    def convert_to_csv(self, from_excel: str, output_path: str) -> Any:
        pass