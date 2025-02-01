import boto3
import psycopg2
import json

from config import get_db_config

sqs = boto3.client("sqs", region_name="us-east-1")

conn = psycopg2.connect(
    **get_db_config()
)


def lambda_handler(event, context):
    for record in event["Records"]:
        message = json.loads(record["body"])
        task_id = message["task_id"]
        result = message["result"]

        # Обновить БД
        with conn.cursor() as cur:
            cur.execute("UPDATE tasks SET status = %s, result_data = %s WHERE id = %s",
                        ("completed", json.dumps(result), task_id))
            conn.commit()

    return {"status": "done"}
