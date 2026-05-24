Idea of how to store IP information

ip_dict = {
    "1.1.1.1" : {"failed": 1, "accepted": 2}
}


## V3 ideas:
- change the code so that in def ip_analysis the dictionary keys are the threats and items the IPs. Then later in the results program don't have to sort them again
- better threat analysis, now it is only based on sum of failed and accepted logins
- RegEx IP parsing instead of hard coding