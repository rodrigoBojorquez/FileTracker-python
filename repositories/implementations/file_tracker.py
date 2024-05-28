import os
import requests
from repositories.definitions.file_tracker_base import FileTrackerRepositoryBase
from typing import Any
import pandas as pd
from icecream import ic

class FileTrackerRepository(FileTrackerRepositoryBase):
    def __init__(self):
        self.session = requests.Session()

    async def store_document_by_url(self, url: str, output_path: str) -> str:
        directory_path = os.path.dirname(output_path)

        if not directory_path:
            os.makedirs(directory_path)

        response = self.session.get(url, stream=True)

        response.raise_for_status()

        with open(output_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        return output_path

    def convert_to_csv(self, from_excel: str, output_path: str) -> Any:
        df = pd.read_excel(from_excel, engine="xlrd")
        df.to_csv(output_path, index=False, encoding="utf-8", sep="~")
