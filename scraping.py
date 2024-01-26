import requests
import re
from bs4 import BeautifulSoup


godFather_link = "https://www.dailyscript.com/scripts/The_Godfather.html"
godFather2_link="https://www.dailyscript.com/scripts/godfather2.html"


html_gf1 = requests.get(godFather_link)
html_gf2 = requests.get(godFather2_link)

# In text 1 i could potential identify michaels blocks by looking for the a lone MICHAEL and then a blank line above and below

with open('text1.html','w',encoding='utf-8') as file:
    file.writelines(html_gf1.text)
    
with open('text2.html','w',encoding='utf-8') as file:
    file.writelines(html_gf2.text)
    

    

# All the text inside text1 is inside a <pre>
bs_gf1 = BeautifulSoup(html_gf1.text)
lines=[]
# for letting the program know when to add to the line list
dialogue_flag=False
parentheses_flag=False
index=0
with open('Godfather1.txt','w') as godfatha:
    for line in bs_gf1.get_text().splitlines():
   
        if dialogue_flag:
            # flush list and set flag to false
            if line=='':
           
                lines.append('\n')
                #Adds spaces to strings
                for i in range(1,len(lines)-1):
                    lines[i]=' '+lines[i]
                    lines[i] =lines[i].replace('  ',' ')
                    
                godfatha.writelines(lines)
                lines=[]
                dialogue_flag=False
                index+=1
                continue
            # This line is to deal with a special case where the parens are seperated by lines
            if line.strip()[0]=='(' and line.strip()[-1]!=')':
                parentheses_flag=True
                continue
            elif line.strip()[-1]==')':
                parentheses_flag=False
                continue
            if parentheses_flag:
                continue
            lines.append(re.sub('\(([^()]*)\)','',line.strip()))

            
        if line.find('\t\t\t\tMICHAEL')!=-1:
            dialogue_flag=True
            continue

# I just copy pasted because I didnt want to make a function
bs_gf1 = BeautifulSoup(html_gf2.text)
with open('Godfather2.txt','w') as godfatha2:
    for line in bs_gf1.get_text().splitlines():
      
        if dialogue_flag:
            # flush list and set flag to false
            if line=='':
                lines.append('\n')
                #Adds spaces to strings
                for i in range(1,len(lines)-1):
                    lines[i]=' '+lines[i]
                    lines[i] =lines[i].replace('  ',' ')
                    
                godfatha2.writelines(lines)
                lines=[]
                dialogue_flag=False
                continue
            # This code is to account for cases where text in parentheses is spread out across multiple lines
            if line.strip()[0]=='(' and line.strip()[-1]!=')':
                parentheses_flag=True
                continue
            elif line.strip()[-1]==')':
                parentheses_flag=False
                continue
            if parentheses_flag:
                continue
            
            lines.append(re.sub('\(([^()]*)\)','',line.strip()))

        if line.find('\t\t\t\tMICHAEL')!=-1:
            dialogue_flag=True
            continue