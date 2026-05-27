def print_report(failed_total: int, accepted_total: int, unknown_lines: list, suspicious_dict: dict):
    
    with open("results.txt", "w") as new_file:
        new_file.write(f"LOG ANALYZER RESULTS:\n\n")        
        new_file.write(f"Failed attempts = {failed_total}\n")
        new_file.write(f"Accepted attempts = {accepted_total}\n\n\n")

        for level, ip_list in suspicious_dict.items():
            new_file.write(f"{level}:\n".upper())
            for ip in ip_list:
                new_file.write(f"{ip}\n")
            new_file.write("\n")

        new_file.write("\n\nUnknown lines:")
        for line in unknown_lines:
            new_file.write(line + "\n")