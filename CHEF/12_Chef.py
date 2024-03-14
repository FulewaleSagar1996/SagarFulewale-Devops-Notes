***** Chef Introduction *******

it is configuration managment tool
indudtry mai ek position hti thi system adminidtration 
iska kam company ke mutiple sserver ko manage karne ka rhta hai.
user create karna ,update krne , protect krna,install krna etc ye kam hta h
6-7 system hai to easy hai ye work karna lkn 500 system hai to kaise karega ek sath
aise isme automation picture mai aya
configuration matlab each and evry minute detail of ur server..usi ko manage karna
manual mai error ar tim bht lagta tha isly tool aya ar usme chef ek hai
ye operation ke isme ata hai 
 
 2 types
 push based and pull based 
 
 **push based tool **
 server rhta h jisme sabhi updated files hti hai ar us server se multiple computer connect
 hte hai.
 IAC = infrastructure as code 
 maatlab hume jause ubuntu git window etc kuch bhi install ya update karna hai to hum
 manuall nahi krnge uske liye ek code likhenge ,ar us code ko server mai dal denge 
 ar jab run karega tab automatically sab ho jayga jo karna hai
 code ki help se hum infrastructure create kar rahe hai.isly IAC khte hai
 forcefuully hum sabi server ko update kar skate hai ar ye code hum github se lenge
 ye sabhi chize apas mai judi hti hai..github se code leta hai 
 example = Ansible and salt stalk
 
 ** Pull based **
 ap server ke pas ja rhe ho,,server apko nahi baata raha..ap puch reh ho ki koi 
 update to nahi aya..push  mai server apko bata deta hai direclty
 it check with the server periodically and fetches the configuration from it
 ex - Chef and puppet 
 yaha machine khud compare karti hai server se ar khud update hti rhti hai ar configure
 karti hai.
 chef ko adam jacob ne banaya tha in 2009
 chef is administrator tool
 
 Config management = it is a method through which we automate admin task
 it is tool turns ur code into infratructure
 reepeateble,tastable and versionable
 
 ** advantages of CM tool **
 compkte automation 
 increease uptime / sarttime
 improve performance
 ensure compliance
 prevent errors and reduce cost
 
 ///// CHEF ARCHITECTURE ////
 three comoponents are very important
 workspace or workstation , chef server and node
 * hum workstation mai apna code likhte hai ar us code ko hum recipe kahte hai
 * sabhi recipe jaha hum rakhte hai use cookbook kahte hai
 * recipe = where u written ur infra as a code
 * ccokbook = it is collection of all ur recipe
 * cookbook hamesha chef server mai upload karte hai
 lkn ye apne ap nahi jata...workstation se chef server mai hum tool ke help se jate
 hai ar use hum knife bolte hai
 knife is alsos  used to connect server to node but this process called as bootstrap
 it is a path of connection server to node.
 chef super market = it is collection of all cookbook from where u can take code
 hum chef ko do jagah install karte hai. ek waorkstation ara ek node
 jab hum node mai isntall karte hai tab 2 chize milti hai .ek ohai ar chef client
 chef client it is tool to give code from server.server se lake deti hai code node ke pas
 ohai = it is database of node where all configuration of ur current machine
 chef client ohai se puchta hai config fir o server pe jayga ar update krga jo update nahi hai
 
 workstation o jagh hai jaha hum code likhte hai with ruby langauges
 chef server o jagah hai jaha apne code ko store karte hai
 ar node o jagah hai jaha hum apne code ko apply karte hai
 
 