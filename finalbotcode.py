#-------system to append the database.
def data_append(sentence,words):
    db=open(r"botdata.dat","a+")
    db.write(str(sentence))
    db.write("\n")
    db.write(str(words))
    db.write("\n")
    db.close()

def list_to_string(list1):
    string=""
    for a in list1:
        string=string+a+" "
    return string.strip()

    #there is no space in the last character.

def string_to_list(string):
    list1=string.split()
    return list1

def comparison(db):
#takes a datafile as a argument, in which lines are in the form statement integer(weight), returns the most referenced answer as the reply.
    greatest=0
    reply=""
    term=0
    while term==0:
        value=db.readline()
        weight=db.readline()
        if value==" " or value=="" or weight=="" or weight==" ":
            term=1
        else:
            valuelist=string_to_list(value)
            if int(weight)>=greatest:
                greatest=int(weight)
                reply=list_to_string(valuelist)
    return reply

def uinput():
    uinput=raw_input(">>")

def find_sentences(querylist):
#accepts a list and searches the database for the sentences reffered to in the list and returns a datafile
    import os
    db=open(r"botdata.dat","a+")
    value=0
    while value==0:
        sentence=db.readline()
        words=db.readline()
        if sentence=="" or sentence==" " or words=="" or words==" ":
            value=1
        else:
            lf=0
            for a in range(0,len(querylist)):
                if querylist[a] in string_to_list(words):
                    lf=lf+1
            temp=open(r"tempdata.dat","a+")
            temp.write(sentence)
            temp.write(str(lf))
            temp.write("\n")
            temp.close()
    db.close()

def talk():
    import os
    reply="hi"
    print reply
    while True:
        uinput=raw_input(">>")
        if uinput!="":
            replylist=string_to_list(reply)
            uinputlist=string_to_list(uinput)

            data_append(uinput,reply)
            find_sentences(uinputlist)
            db=open(r"tempdata.dat","a+")
            reply=comparison(db)
            db.close()
            os.remove("tempdata.dat")
            print reply

#-------Main code.

talk()

            
    


            

        
        
                    
            

    
