__author__ = 'avarm1'



import random
import Imagesmanage

class Startup(object):
    file=open("names.txt")
    data=file.read()
    data=data.split("\n")

    name=data[random.randint(0,len(data)-1)]
    alphabets=[]
    chances=5
    victory=1


    def printanimal(self):
        for i in self.name:
            if(i==" "):
                print(" ",end=" ")
            elif(self.alphabets[ord(i)-ord("a")]=="found"):
                print(i,end=" ")


            else:
                print("_ ",end="")


    def startguess(self):

        for i in range(0,26):
            self.alphabets.append(1)

        while(True):
            random_number = random.randint(0, len(self.name)-1)
            if(self.name[random_number]!=" "):
                break



        for i in self.name:

            if(i.isalpha()):
                self.alphabets[ord(i)-ord("a")]=0


        self.alphabets[ord(self.name[random_number])-ord("a")]="found"

        self.printanimal()










    def enterinput(self):
        while(self.chances>0 and self.victory>0):
            choice = input("\t\tguess the animal")
            if(choice.isalpha()):
                choice=choice.lower()
                if(self.alphabets[ord(choice)-ord("a")]==0):
                    self.alphabets[ord(choice)-ord("a")]="found"
                    self.victory=self.alphabets.count(0)
                    self.printanimal()

                elif(self.alphabets[ord(choice)-ord("a")]==1):
                    self.chances=self.chances-1
                    print("wrong guess...you have %d chyances remaining"%self.chances)
                    Imagesmanage.displayimage(5-self.chances)
                    self.printanimal()
                    self.alphabets[ord(choice)-ord("a")]="wrong"

                elif(self.alphabets[ord(choice)-ord("a")]=="wrong" or self.alphabets[ord(choice)-ord("a")]=="found"):
                    print("already selected....try other one")
                    self.printanimal()
            else:
                print("enter only alphabets")
                self.printanimal()


temp=Startup()
temp.startguess()
temp.enterinput()
if(temp.chances<=0):

    print("\nsorry you have lost\n try again")
else:
    print("\nhurry you won")







