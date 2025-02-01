Обновленный сценарий:
* API (Flask на EC2)
  + Принимает запрос и кладет данные в SQS (Queue A). 
  + Записывает начальный статус задачи в PostgreSQL (например, pending).

* Обработчик данных (Lambda A)
  + Берет сообщение из Queue A, обрабатывает его. 
  + Кладет результат в SQS (Queue B). 

* Триггер событий (EventBridge)
  + EventBridge отслеживает появление данных в Queue B и вызывает Lambda B.

* Финальная обработка (Lambda B + PostgreSQL)
  + Lambda B берет результат из Queue B. 
  + Обновляет статус в PostgreSQL (completed, failed и т. д.), а также сохраняет результат.

* Что в базе?

Таблица tasks с колонками:
* id (UUID, Primary Key)
* status (pending, processing, completed, failed)
* created_at, updated_at 
* result_data (JSON или Text)

Что освоишь дополнительно?
✅ Работа с PostgreSQL в AWS (можно развернуть на RDS или локально в EC2).
✅ Lambda → PostgreSQL (например, через psycopg2).

Если план устраивает, могу расписать последовательные шаги!