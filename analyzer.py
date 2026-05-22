import os

def main():
    fails, accepts = read_log()
    print_report(fails, accepts)  


def read_log():
    ip_dic = {}
    fail_counter = 0
    accepted_counter = 0

    for file_name in os.listdir("logs"):
        file_path = os.path.join("logs", file_name)

        with open(file_path) as new_file:   
            for line in new_file:   
                line = line.split(" ")

                if "from" in line:
                    ip = line[line.index("from") + 1]
                    if ip not in ip_dic:
                        ip_dic[ip] = []

                         

                if line[0] == "Accepted":
                        accepted_counter += 1
                elif line[0] == "Failed":
                        fail_counter += 1
                else:
                    raise ValueError  
                

                         

    return fail_counter, accepted_counter   

def ip_parsing(line):
    pass
                    
def print_report(failed: int, accepted: int):
    with open("results.txt", "w") as new_file:
        new_file.write(f"LOG ANALYZER RESULTS:\n\n")        
        new_file.write(f"Failed attempts = {failed}\n")
        new_file.write(f"Accepted attempts = {accepted}\n")

main()