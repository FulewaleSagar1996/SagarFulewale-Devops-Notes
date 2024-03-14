# after downlading java git and maven in your laptop 

maven ka kam jenkins se karwana hai to hum maven ka path denge ki o kis jagah pada hai laptop mai
ar dusre tarike mia hum direclty jenkins mai maven instal kerke kam karwaynge

*go to google chrome loacal host:8080 login
** go to manage jenkins on left side of jenkins dashboard>>> manage plugins>>>available>>>
select maven inegration and green balls>>>> install wiahout restart

** go to neaw item maven project
** now got to manage jenkins >>>> global tools confi 
go to add jdk >> uncheck install automatically option 
name >>> java
java_home >>> c\programefiles\java\jdk

** now got to maven 
name = MAVEN
MAVEN_HOME = c\devtoold\apache maven

#### MAVEN PROJECT 
go to github time tracker
** click n time tracker repo 
** fork to copy this repo
** sign into your github acount
** click on time tracker repo 
** clone
** go to c drive 
** git clone<url of time tracker repo>
** cd time tracker
** c:\time-tracker> mvn clean package


###  Ab isis kam ko Jenkins ke through karna hai
## maven project by jenkins

** now go to jenkins >>> new item >> entername >> mymavenproject
** then select maven project >>> ok
source code managment
>> repository URL <path of time tracker>
build option >> root pom >> pom.xml
goals and option >>> clean package >>> save
go to jenkis home page >>> click on 
mymavenproject>> build now

## schedule project 
periodically ye kam kar skata hai ....you can see automatically build after one minute
you can automatically build..but isme har bar o chekc karta hai kuch changeas liye ho ya nahi kiye ho fir bhi

## Source code Polling (poll SCM)
isme jab change karnge tab hi build hga automatcally..bar bar nahi karte rahge 
**  noow go to jenkins homepage
** go to mymavenproject >> configure
** now goto build triggr >> poll scm 

####   Check its videos direclty for more clearity #####

after this videos 
# linked project, viewws, user managment, and master slave concept 
you can watch direclty on videos bcz it is GUI based

linked project matlab ek kam hte hi dusra kam chalu hna automatic
upstrem linked project and downstream linked project
 take screenshot for this lab 
 lecture 39
 
 # lecture 40 = u can direclty perform lab
 