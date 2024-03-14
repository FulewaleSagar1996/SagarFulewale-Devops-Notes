sabse phle awwwws ke andaar linux create karo,usme chef worksatation install kre
wha ek directory create krna cookbooks nam ki.name is same
cooknook ke andar ar ek cookbook banynge jiska nam test cookbook rahge
ar uske andar reci  pe create krnge diff diff.recipe matlab code likhna hai

**steps***
ec2-user
sudo su
yum update -y
now go to google,search www.chef.io
go to dwnld--chef workstation--enter name,email fake,company,cpy url
wget url
ls
yum install -y (chef workstation)
which chef
iske bad ka screenshot mai dekh lena
chef --version
mkdir cookbooks
ls
cd cookbooks/
chef generate cookbook <name of cookbook ex. testcookbook>
yum install tree -y
tree
iske bad hume recipe create karna hai to testcookbook ke andar jaynge
cd test-cookbook
chef generate recipe <name of recipe>
tree 
cd .. (recipe create karne ke bad bahar ana hai ,srf recipe banane k wqt andar
jana hai ar fr pura kam bahar see hi karna hai)
vi test-cookbook/recipes/test-recipe.rb = rb means ruby must hai
iske bad code enter karna hai file create karne ka
ab hume jo code likha hai use check karna hai sahi hai ya galat krke==
chef exec ruby -c test-cookbook/recipes/test-recipe.rb
output = syntex is ok
fir jo chef client hta hai o jake ohai se puchega ki config hai uya nahi
uske liye command hti hai
chef-client -zr "recipe [test-cookbook::test recipe]"

chef client puchega.agar code nahi hai to recipe banayga..receipe command se 
recipe banane ke liye command diya hai fir test cookbook and test recipe ki file
run hgi ar wha ka code run hga

z= local machine r = run list
ls/

2nd recipe
cd test-cookbook/= slash lagaye ya maat lagao
chef generate recipe recipe2
cd ..
vi test-cookbook/recipes/recipe2.rb
isme hum do code likhnge.one for create file and other for install package
code apvideo se copy paste karke dekh lo
chef-client -zr :"recipe[test-cookbok :: recipe2]"
