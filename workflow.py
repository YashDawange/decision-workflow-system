def process_workflow(request, decision):

    history = []

    history.append("RECEIVED")

    history.append("VALIDATED")

    history.append("RULE_EVALUATED")

    history.append(decision.upper())

    history.append("COMPLETED")

    return history