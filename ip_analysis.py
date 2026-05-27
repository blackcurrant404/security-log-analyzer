def analyze(ip_dict):
    threats = {"high-threat": [], "medium-threat": [], "low-threat": [], "no-threat": []}
    for ip, items in ip_dict.items():
        fail_amount = 0
        threat_level = 0
        for attempt in items["attempts"]:
    
            if attempt == "accepted":
                fail_amount = 0
            else:
                fail_amount += 1
            
            if fail_amount > 3 and threat_level < 1:
                threat_level = 1
            elif fail_amount > 5 and threat_level < 2: 
                threat_level = 2
            elif fail_amount > 7 and threat_level < 3:
                threat_level = 3

        if threat_level == 3:
            threats["high-threat"].append(ip)
        elif threat_level == 2:
            threats["medium-threat"].append(ip)
        elif threat_level == 1:
            threats["low-threat"].append(ip)
        elif threat_level == 0:
            threats["no-threat"].append(ip) 
             
    return threats
