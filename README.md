# Ping Script
## Problem Statement
Read in XX number of variables when launched, each one representing a server name that the server your script runs on has DNS resolution for
Iterate through those server variables, testing each one with a ping command, the ping should run five times, with a two second pause between each one
## Output


![Screenshot from 2022-02-11 10-44-47](https://user-images.githubusercontent.com/55188287/153540993-5bb0f679-427c-4186-8a57-a8573307b5c4.png)

If sever is down it will give output DOWN server is not responding

![Screenshot from 2022-02-11 10-54-40](https://user-images.githubusercontent.com/55188287/153541716-e8824154-1eae-4492-a46f-73cbea62baf0.png)

## Crontab
Crontab stands for “cron table”. It allows to use job scheduler, which is known as cron to execute tasks. Crontab is also the name of the program, which is used to edit that schedule. It is driven by a crontab file, a config file that indicates shell commands to run periodically for the specific schedule.
To run script on every 5 min here I use Crontab

## Crontab Commands
 1 systemctl status cron.service
 
 To check status of crontab

 2 systemctl start cron.service
 
 To start crontab

 3 systemctl enable cron.service

 To enable crontab

 4 crontab -e

 by using this command we can edit file

 for this script entries mentioned below
 

*/05    *       *       *       *       /usr/bin/python3        /home/priyankalimbulkar/python1/code.py
 
 ![Screenshot from 2022-02-11 12-17-12](https://user-images.githubusercontent.com/55188287/153548215-e7626a0d-1c7d-492a-9aca-d7dbf1bda534.png)

 5 crontab -l 
 
 To check list of task
 
 ![Screenshot from 2022-02-11 12-17-27](https://user-images.githubusercontent.com/55188287/153548250-7094b980-be8c-4c96-bd67-d356886f99f2.png)

 6 sudo tail -f /var/log/syslog

 To check logs of crontab

 By using mail also we can check our job is running properly or not

 7 sudo apt-get install postfix
 
 To install Postfix

Postfix is default mail transfer agent
 
 8 sudo apt install mailutils
 
 To install mail Commands

 9 mail
 
 To check our job is running properly or not
 
 ![Screenshot from 2022-02-11 12-17-43](https://user-images.githubusercontent.com/55188287/153548274-a1a9f8dc-e7a9-4fe0-bf1b-0513880405fb.png)


