# kg-devops-test

__Devops Section__

TODO: Remove hardcoded values (subnets) + Bonus section

AWS
Change the hardcoded values in LBv2 section (subnets in my personal default vpc), then upload *.json files in Cloudformation via AWS Console or AWS Cli and Create Stack

NOTE: Never touched chef before, so apologies in advance.
Chef (changed httpd2 to apache2 for my environment)
1. Deployed local docker container with ruby + chef packages
2. Tested code with: chef-client --local-mode test.rb
3. Ran the following commands to check changes
    
    ls -lrt /etc/motd ## list file
    
    crontab -l ## see cron entry
    
    cat /etc/passwd ## see new user
    
    date ## show datetime and timezone
    

__Scripting Section__

command: python getBeersGreaterThan <abv_value>
