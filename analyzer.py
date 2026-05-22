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

main()