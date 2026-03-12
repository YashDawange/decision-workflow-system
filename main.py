from fastapi import FastAPI
from rule_engine import evaluate_rules
from workflow import process_workflow
from audit_logger import create_audit_log
from database.db import requests_db
from external_service import verify_credit_service
from pydantic import BaseModel

class DecisionRequest(BaseModel):
    request_id: str
    income: float
    credit_score: int

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Decision System Running"}


@app.post("/request")
def process_request(request: DecisionRequest):

    request = request.dict()

    request_id = request["request_id"]

    if request_id in requests_db:
        return {
            "message": "Duplicate request",
            "result": requests_db[request_id]
        }

    service_ok = call_external_service_with_retry()

    if not service_ok:
        return {"message": "External credit service unavailable"}

    decision = evaluate_rules(request)

    history = process_workflow(request, decision)

    audit = create_audit_log(request, decision)

    result = {
        "decision": decision,
        "history": history,
        "audit": audit
    }

    requests_db[request_id] = result

    return result

@app.get("/request/{request_id}")
def get_request_status(request_id: str):

    if request_id in requests_db:
        return requests_db[request_id]

    return {"message": "Request not found"}

def call_external_service_with_retry():

    for attempt in range(3):

        try:
            verify_credit_service()
            return True

        except Exception as e:
            print("External service failed. Retrying...", attempt+1)

    return False