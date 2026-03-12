import random

def verify_credit_service():
    
    # simulate external service failure randomly
    if random.random() < 0.3:
        raise Exception("Credit verification service failed")

    return True