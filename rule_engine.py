import json

def load_rules():
    with open("config/rules.json") as f:
        data = json.load(f)
    return data["rules"]

def evaluate_rules(request):

    rules = load_rules()

    income = request["income"]
    credit_score = request["credit_score"]

    for rule in rules:

        condition = rule["condition"]

        if condition == "default":
            return rule["decision"]

        if eval(condition):
            return rule["decision"]