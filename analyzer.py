from log_reader import read_log 
from report import print_report
from ip_analysis import analyze

def main():
    fails, accepts, unknown_lines, ip_dict = read_log()
    suspicions_list = analyze(ip_dict)
    print_report(fails, accepts, unknown_lines, suspicions_list)  

main()