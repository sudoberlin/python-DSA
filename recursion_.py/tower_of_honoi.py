#tower of honoi
#move n-1 disk from A to B using auxiliary bar C
#move 1 disk From A to C
#move n-1 disk B to C using auxiliry A

def toh(n,from_bar, to_bar, aux_bar):
    if n == 1:
        print ("move disk 1 from bar",from_bar, "to bar",to_bar)
        return 
    toh(n-1, from_bar, to_bar, aux_bar)
    print("move disk", n, "from bar", from_bar,"to bar", to_bar)
    toh(n-1, to_bar, aux_bar, from_bar)

n = int(input("enter a number: "))
toh(n, 'A', 'B', 'C')
