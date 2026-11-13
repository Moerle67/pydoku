class Feld:
    def __init__(self):
        self.feld = []
        lst_numbers = [1,2,3,4,5,6,7,8,9]
        for zeile in range (9):
            lst_zeile = []
            for spalte in range (9):
                lst_zeile.append(lst_numbers.copy())
            self.feld.append(lst_zeile)

    def print_feld(self):
        print()
        print("| 1  2  3 | 4  5  6 | 7  8  9 |")
        print("-"*32)
        for zeile in range(9):
            print("|", end="")
            for spalte in range(9):
                if spalte == 3 or spalte == 6:
                    print("|", end = "")
                if len(self.feld[zeile][spalte])==1:
                    print(" ",self.feld[zeile][spalte]," ",sep="", end="")
                else:
                    print("   ", end="")
            print("|")
            print("-"*32)

