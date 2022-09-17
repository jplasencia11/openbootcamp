print("Primera Parte") 
def main (a,b,c):
    total= a+b+c
    return total
print (main(3,2,1))
print("Segunda Parte")
class coche:
    door=4

    def incre(self):
        total= int(self.door)
        total+=1
        print (total)

def main():
    miCoche=coche()
    miCoche.incre()


if __name__=='__main__':main()
