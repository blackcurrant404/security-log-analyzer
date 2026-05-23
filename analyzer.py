import os

def main():
    fails, accepts, unknown_lines, ip_dict = read_log()
    suspicions_list = ip_analysis(ip_dict)
    print_report(fails, accepts, unknown_lines, suspicions_list)  


def read_log():
    ip_dict = {}
    fail_counter = 0
    accepted_counter = 0
    unknown_lines = []

    for file_name in os.listdir("logs"):
        file_path = os.path.join("logs", file_name)

        with open(file_path) as new_file:   
            for line in new_file:   
                line = line.split(" ")

                if "from" in line:
                    ip = line[line.index("from") + 1].strip()
                    if ip not in ip_dict:
                        ip_dict[ip] = {"accepted": 0, "failed": 0}

                if line[0] == "Accepted":
                        accepted_counter += 1
                        ip_dict[ip]["accepted"] += 1                  
                elif line[0] == "Failed":
                        ip_dict[ip]["failed"] += 1       
                        fail_counter += 1
                    else:
                        unknown_lines.append(line)                      

    return fail_counter, accepted_counter, unknown_lines, ip_dict 

def ip_analysis(ip_dict):
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
        

def print_report(failed_total: int, accepted_total: int, unknown_lines: list, suspicious_dict: dict):
    with open("results.txt", "w") as new_file:
        new_file.write(f"LOG ANALYZER RESULTS:\n\n")        
        new_file.write(f"Failed attempts = {failed_total}\n")
        new_file.write(f"Accepted attempts = {accepted_total}\n\n\n")

        high_threat_list = []
        medium_threat_list = []
        low_threat_list = []

        for ip, threat_level in suspicious_dict.items():
            if threat_level == "HIGH-THREAT":
                high_threat_list.append(ip)
            elif threat_level == "MEDIUM-THREAT":
                medium_threat_list.append(ip)
            elif threat_level == "LOW-THREAT":
                low_threat_list.append(ip)

        new_file.write("HIGH_THREAT:\n") 
        for ip2 in high_threat_list:
            new_file.write(f"{ip2}\n")
        new_file.write("MEDIUM_THREAT:\n") 
        for ip2 in medium_threat_list:
            new_file.write(f"{ip2}\n")
        new_file.write("LOW_THREAT:\n") 
        for ip2 in low_threat_list:
            new_file.write(f"{ip2}\n")

        new_file.write("\n\nUnknown lines:")
        for line in unknown_lines:
            new_file.write(line + "\n")
main()