## Install Apache
## Added colon to install 
package 'httpd2' do
    action :install
end

## Enable Apache on startup
## Actions in list (enable, start)
service 'httpd2' do
  action [ :enable, :start ]
end

file '/etc/motd' do
   owner 'root'
   group 'root'
   mode '0644'
   content 'Hello world'
end


## Simple user creation
user 'gavin.ho' do 
	home '/home/gavin.ho'
	password 'test'
end

## Cron resource to scheule everyday and 5:45
cron 'schedule' do
  minute '45'
  hour '5'
  command 'echo Hello World > /tmp/cron-output.txt'
end

## Set timezone to London in system
timezone 'Set Timezone to London' do
  timezone 'GMT'
end
