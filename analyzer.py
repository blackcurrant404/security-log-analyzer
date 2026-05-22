def main():
    read_log()

def read_log():
    Fail_counter = 0
    Accepted_counter = 0

    with open("sample_auth.log") as new_file:
        for line in new_file:
            line = line.split(" ")
            if line[0] == "Accepted":
                    Accepted_counter += 1
            elif line[0] == "Failed":
                        Fail_counter += 1
            else:
                raise ValueError     

        print_report(Fail_counter, Accepted_counter)  

                    
def print_report(failed: int, accepted: int):
    with open("results.txt", "w") as new_file:
        new_file.write(f"LOG ANALYZER RESULTS:\n\n")        
        new_file.write(f"Failed attempts = {failed}\n")
        new_file.write(f"Accepted attempts = {accepted}\n")

main()