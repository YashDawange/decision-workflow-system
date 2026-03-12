def create_audit_log(request, decision):

    log = {}

    log["request"] = request

    log["decision"] = decision

    return log