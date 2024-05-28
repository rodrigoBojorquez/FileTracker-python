from dotenv import load_dotenv
import os
import asyncio

# Repositories
from repositories.implementations.file_tracker import FileTrackerRepository

async def main():
    load_dotenv()
    excel_path = os.getenv("EXCEL_PATH")
    csv_path = os.getenv("CSV_PATH")
    file_url = os.getenv("FILE_URL")

    file_tracker_repository = FileTrackerRepository()
    await file_tracker_repository.store_document_by_url(file_url, excel_path)
    file_tracker_repository.convert_to_csv(from_excel=excel_path, output_path=csv_path)
    

if __name__ == "__main__":
    asyncio.run(main())