## pre requisite

httpd (browse)
php (dashboard)
gec & gd (complier to convert row code into binaries)
makefile (to build)
perl (script)

main configuration file   ===== interview que
/usr/local/nagios/etc/nagios.cfg 

All monitoring things called as "service "

## Dahboard Overview 

In dashboard , you can see 
host and services

# Installation of Nagios on linux
To start nagios core installation you must have your EC2 instance up and 
run and have already configured ssh access to the instance.

Step1: install prerequisite software on your ec2 machine prior to nagios
installation like apache,php,gcc compiler and gd development libraries

** sudo su
** yum install httpd php
** yum install gcc glib glib-common
** tum install gd gd-devel

Step2= create account information, you need to setup a nagios
user run the following commands
** adduser -m nagios
** passwd nagios
now,it ask to enter password and give it 
 
** groupadd nagioscmd
** usermod -a -G nagioscmd nagios
** usermod -a -G nagioscmd apache

Step3= download nagios core and the plugins create a directory for 
storing the downloads
** mkdir ~downloads
** cd ~downloads

Download the source codes tarballs of both nagios and the nagios plugins
** check links from videos
https://yer.dl.sourceforge.net/project/nagios/nagios-4.x/nagios-4.0.8/nagios-4.0.8.tar.gz
wget http://nagios-plugins.org/download/nagios-plugins-2.0.3.tar.gz

Step4= compile and install nagios extract the nagios source code tarball
** tar zxvf nagios-4.0.8. tar.gz
** cd nagios-4.0.8

Run the configuration script wit the name of the group which u have
created in above step 
** ./configure --with-command-group=nagioscmd

Compile the nagios source code
** make all

Install binary,init script,sample config files sand set permission
on the external command directly
** make install
** make install-init
** make install-config 
** make install-commandmode

step5= configure the web iinterface
** make install-webconf
htpasswd -c /usr/local/nagios/etc/htpasswd.users nagiosadmin
service httpd restart


cd ~/downloads
tar zxvf nagios-plugins-2.0.3.tar.gz
cd nagios-plugins-2.0.3

./configure --with-nagios-user=nagios --with-nagios-group=nagios
make
make install


chkconfig --add nagios
chkconfig nagios on

/usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg

service nagios start
service httpd restart

