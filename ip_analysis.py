def analyze(ip_dict):
    suspicions_dict = {}
    attempt_sum = 0
    for ip in ip_dict:
        attempt_sum = ip_dict[ip]["accepted"] - ip_dict[ip]["failed"]
        if attempt_sum < -2:
            suspicions_dict[ip] = "HIGH-THREAT"
        elif attempt_sum < -1:
            suspicions_dict[ip] = "MEDIUM-THREAT"
        elif attempt_sum < 0:
             suspicions_dict[ip] = "LOW-THREAT"
             
    return suspicions_dict