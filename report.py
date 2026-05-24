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