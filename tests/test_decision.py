from rule_engine import evaluate_rules

def test_approve():

    request = {
        "request_id": "TEST001",
        "income": 60000,
        "credit_score": 720
    }

    assert evaluate_rules(request) == "approve"


def test_reject():

    request = {
        "request_id": "TEST002",
        "income": 20000,
        "credit_score": 550
    }

    assert evaluate_rules(request) == "reject"


def test_manual_review():

    request = {
        "request_id": "TEST003",
        "income": 40000,
        "credit_score": 650
    }

    assert evaluate_rules(request) == "manual_review"