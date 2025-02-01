import os
from uuid import uuid4

import boto3
import psycopg2
from flask import Flask, request, jsonify

from config import get_db_config, TO_PROCESS_TASK_QUEUE_URL

app = Flask(__name__)

sqs = boto3.client('sqs', region_name="us-east-1")

conn = psycopg2.connect(**get_db_config(), )


@app.route("/task", methods=["POST"])
def create_task():
    task_id = str(uuid4())
    data = request.json

    with conn.cursor() as cur:
        cur.execute("INSERT INTO tasks (id, status) VALUES (%s, %s)", (task_id, "pending"))
        conn.commit()

    sqs.send_message(QueueUrl=TO_PROCESS_TASK_QUEUE_URL, MessageBody=task_id)
    return jsonify({"task_id": task_id, "status": "pending"})


if __name__ == '__main__':
    app.run()
