import os 
import re

def read_log():

    regex_ip = r"\d+\.\d+\.\d+\.\d+"
    ip_dict = {}
    fail_counter = 0
    accepted_counter = 0
    unknown_lines = []

    for file_name in os.listdir("logs"):
        file_path = os.path.join("logs", file_name)

        with open(file_path) as new_file:   
            for line in new_file:
                result = re.search(regex_ip, line)   

                if result:
                    ip = result.group()
                    if ip not in ip_dict:
                        ip_dict[ip] = {"accepted": 0, "failed": 0}
                else:
                    unknown_lines.append(line)  

                if "Accepted" in line:
                        accepted_counter += 1
                        ip_dict[ip]["accepted"] += 1                  
                elif "Failed" in line:
                        ip_dict[ip]["failed"] += 1       
                        fail_counter += 1
                else:
                    unknown_lines.append(line)  
                    

    return fail_counter, accepted_counter, unknown_lines, ip_dict 