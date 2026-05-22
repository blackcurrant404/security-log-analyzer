def main():
    read_log()

def read_log():
        with open("sample_auth.log") as new_file:
              for line in new_file:
                    print(line, end="")

main()