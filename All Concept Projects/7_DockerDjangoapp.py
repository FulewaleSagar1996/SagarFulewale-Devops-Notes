########
yah docker file ko kaise containerise karke browser mai chalaye uska project hai...

yaha hum django application containerise karne wale hai.
as a devops engg apko paata rahna chy har ek langauge ki application kaise containerise karte hai
ya fir deploy karte hai..thoda bht programing ka knlowlege ya for uska work flow pata rhna chy. 

U SHOULD KNOW THE WORKFLOW OF ANY LANGAUGE DEVELOPMENT APPLICATION (GO TO DOCUMENTATION)

***** PYTHON WEB FRAMEWORK

[[[[[[django--- yah ek framework hai python application likhne ka..isme apko dab files anf folders ya fir ap
dependencies bol sakte ho..jo readymade milti hai ar apko srf code pe focus karana padta hai.
it is high level python web framework taht enables rapid development.it ig generally used for more complex
or large project 

flask--- Flask is a small and lightweight Python web framework that provides useful tools and 
features that make creating web applications in Python easier.]]]]]]]]]]]

*****JAVA WEB FRAMEWORK

Spring Boot: Reduces time in development and increases productivity—Spring Boot makes 
it much easier to develop Spring-based apps with Java.

# flow of django application-----:

# pahle hum python install karte hai ,then pip, pipe instal djangoadmin install karte hai.
djangoadmin yah skeleton creat karta hai pure developemtn ka...yah sab project ke configuration create
karke deta hai jaise ki yaha pe devops ke andar setting.py ki file hai...
url.py---yah content serve karta hai../demo is contect path
demo is name of aplication.folder mai html file hai jo hamari application ahe dikha raha hai.
views.py mai actul code hota hai...

before docker...qa or qe need to be download these dependencies anf sometime conatiner will not work
then docker come into picture and it will get easy to run application in any env.

### sabsee phle apko jira tickt se task milega then u have to study these project with developer
and write dockerfile 


######### DOCKERFILE ###############

 FROM ubuntu (#yah se base image hum lenge matlab operating system lange jo image hti hai chhoti)

 WORKDIR /app (#jaha haume apni container run kana hai ya fir application
                #rakhni hai us folder ka name)

 COPY requirements.txt /app (# usi app wale folder mai sari dependency copy karnge)
 COPY devops /app (# fir jo hamara source code hai use bhi copy karnge us foder mai)

 RUN apt-get update && \  (# then command run karnge)
     apt-get install -y python3 python3-pip && \ (# python insatll karenge or hum direclty from mai python rakh sakte the )
     pip install -r requirements.txt && \ (## depedencies instaall karnge )
     cd devops

 ENTRYPOINT ["python3"] (# isme hum command ko oveeride nahi kar sakte hai)
 CMD ["manage.py", "runserver", "0.0.0.0:8000"] (# isme oveerrie kar sakte hai jai se ki port change karna )
                                            
ony two commands needed 
docker build .
docker run -it -p 8000:8000 ////// something
