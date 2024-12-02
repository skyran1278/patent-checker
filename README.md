```sh
docker compose up -d

curl -X POST http://localhost:8000/check \
-H "Content-Type: application/json" \
-d '{"patent_id": "US-RE49889-E1", "company_name": "Walmart Inc."}'
```
