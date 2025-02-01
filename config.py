from dotenv import load_dotenv
import os

load_dotenv()


def get_db_config() -> dict:
    return {
        "dbname": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "host": os.getenv("DB_HOST"),
    }


TO_PROCESS_TASK_QUEUE_URL = os.getenv("TO_PROCESS_TASK_QUEUE_URL")
PROCESSED_TASK_QUEUE_URL = os.getenv("PROCESSED_TASK_QUEUE_URL")