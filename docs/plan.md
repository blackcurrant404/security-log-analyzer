Idea is to do a log analyzer. In the sample_auth.log file I have some logs for analyzation.

## security log analyzer plan

## V1 
- read log files
- identify failed and accepted attempts
- create report file that tells number of both attempts

## V2
- extract IPs
- count failed attempts per IP
- adds suspicious IPs to the report
- unknown line handling
- support for multiple log files

## V3
- RegEx ip parsing
- refactor code into smaller functions
- improve threat detection logic (to be defined)