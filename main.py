__author__ = 'avarm1'



import random

class Startup(object):
    name="sparrow"
    alphabets=[]
    chances=5
    victory=1


    def printanimal(self):
        for i in self.name:
            if(self.alphabets[ord(i)-ord("a")]=="found"):
                print(i,end=" ")
            else:
                print("_ ",end="")


    def startguess(self):

        for i in range(0,26):
            self.alphabets.append(1)

        random_number = random.randint(0, len(self.name)-1)


        for i in self.name:

            self.alphabets[ord(i)-ord("a")]=0

        self.alphabets[ord(self.name[random_number])-ord("a")]="found"


        for letter in self.name:
            if(self.name[random_number]==letter):
                print(letter,end=" ")
            else:
                print("_ ",end="")



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







