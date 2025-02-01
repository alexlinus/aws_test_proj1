import boto3
import psycopg2
import json

from config import get_db_config, PROCESSED_TASK_QUEUE_URL

sqs = boto3.client("sqs", region_name="us-east-1")

conn = psycopg2.connect(**get_db_config())


def lambda_handler(event, context):
    for record in event["Records"]:
        task_id = record["body"]
        # Логика обработки
        result = {"sum": sum(range(10)), "task_id": task_id, "status": "successfully_processed"}

        # Обновить статус в БД
        with conn.cursor() as cur:
            cur.execute("UPDATE tasks SET status = %s WHERE id = %s", ("processing", task_id))
            conn.commit()

        # Отправить в SQS B
        sqs.send_message(QueueUrl=PROCESSED_TASK_QUEUE_URL, MessageBody=json.dumps({"task_id": task_id, "result": result}))

    return {"status": "done"}
