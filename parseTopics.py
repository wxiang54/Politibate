def parse():
    newtext=''
    f=open('topics.csv','r')
    subjectlist= f.read()
    splited=subjectlist.split("\n")
    f.close()
    for k in range(len(splited)):
        mylist = []
        sub=splited[k].split(",")
        for j in sub:
            mylist.append(j)
        splited[k] = mylist 
    return splited
print parse()

2016 Presidential Election: The Candidates and Where They Stand on the Issues,Should Marijuana Be a Medical Option?,Should More Gun Control Laws Be Enacted?,Should Animals Be Used for Scientific or Commercial Testing?,Should the Death Penalty Be Allowed?,Should Students Have to Wear School Uniforms?,Should the Drinking Age Be Lowered from 21 to a Younger Age?,Should the Federal Minimum Wage Be Increased?,Should Abortion Be Legal?,What Are the Solutions to Illegal Immigration in America?