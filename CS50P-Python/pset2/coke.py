#Couldn't solve 8/8 tests but did 7/8.
#Did multiple attempts later but couldn't figure out the way.so i guess this is fine.

def main():
    due = 50
    valid_coins = [5,10,25] 
    while due > 0:
        coin = int(input("Insert Coin: "))
        if coin in valid_coins:
            due = due - coin
            if due < 0:
                print(f"Change Owed: {due*(-1)}")
            else:
                print(f"Amount Due: {due}")
        else:
            print(f"Amount Due: {due}")

main()