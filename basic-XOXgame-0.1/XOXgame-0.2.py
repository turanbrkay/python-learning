import time
print("""
    BASİT XOX OYUNUNA HOŞGELDİNİZ
OYUNU İLK ÜÇLEMEYİ YAPAN KAZANACAKTIR\n
""")

class Game():

    def __init__(self):

        self.board = ["-","-","-",
                      "-","-","-",
                       "-","-","-"]

        self.numbers = ["1","2","3","4","5","6","7","8","9"]

    def DisplayBoard(self):
        print("-"*45,"\n")
        print(self.board[0], " | ",self.board[1]," | ",self.board[2],"\t\t","1 | 2 | 3")
        print(self.board[3]," | ", self.board[4]," | ", self.board[5],"\t\t","4 | 5 | 6")
        print(self.board[6]," | ", self.board[7]," | ", self.board[8],"\t\t","7 | 8 | 9")

    def PlayGame(self):
        self.DisplayBoard()

        self.HandleTurn()
        self.WhoWin()

    def HandleTurn(self):
        counter = 2

        while True:
            if counter % 2 == 0:
                print("X'in sırası!")
                position = input("1'den 9'a kadar bir sayı seçiniz.")
                while position not in self.numbers:

                    position = input("1 ile 9 arası bir sayı girmeniz gerekiyorr!!!..")



                position = int(position)-1

                if self.board[position] == "-":
                    self.board[position] = "x"
                    self.DisplayBoard()
                    self.WhoWin()
                    counter += 1
                    continue
                else:
                    print("Seçilen Yer DOLU!")
                    self.DisplayBoard()

                self.DisplayBoard()
            elif counter % 2 != 0:
                print("O'nun sırası!")
                position = input("1'den 9'a kadar bir sayı seçiniz.")
                while position not in self.numbers:
                    position = input("1 ile 9 arası bir sayı girmeniz gerekiyorr!!!..")

                position = int(position)-1

                if self.board[position] == "-":
                    self.board[position] = "o"
                    self.DisplayBoard()
                    self.WhoWin()
                    counter += 1
                    continue
                else:
                    print("Seçilen Yer DOLU!")
                    self.DisplayBoard()



        self.DisplayBoard()

    def WhoWin(self):

        row1 = self.board[0] == self.board[1] == self.board[2] == "x"
        row2 = self.board[3] == self.board[4] == self.board[5] == "x"
        row3 = self.board[6] == self.board[7] == self.board[8] == "x"
        columns1 = self.board[0] == self.board[3] == self.board[6] == "x"
        columns2 = self.board[1] == self.board[4] == self.board[7] == "x"
        columns3 = self.board[2] == self.board[5] == self.board[8] == "x"
        diagonal1 = self.board[0] == self.board[4] == self.board[5] == "x"
        diagonal2 = self.board[2] == self.board[4] == self.board[6] == "x"

        row11 = self.board[0] == self.board[1] == self.board[2] == "o"
        row22 = self.board[3] == self.board[4] == self.board[5] == "o"
        row33 = self.board[6] == self.board[7] == self.board[8] == "o"
        columns11 = self.board[0] == self.board[3] == self.board[6] == "o"
        columns22 = self.board[1] == self.board[4] == self.board[7] == "o"
        columns33 = self.board[2] == self.board[5] == self.board[8] == "o"
        diagonal11 = self.board[0] == self.board[4] == self.board[5] == "o"
        diagonal22 = self.board[2] == self.board[4] == self.board[6] == "o"

        if row1 or row2 or row3 or columns1 or columns3 or columns2 or diagonal1 or diagonal2:
            print("X kazandı! TEBRİKLER..")
            time.sleep(2)
            tekrar = input("Tekrar oynamak ister misiniz? E/H")
            if tekrar == "E" or tekrar == "e":
                self.PlayGame()
            else:
                print("Çıkış yapılıyor")
                time.sleep(2)
                quit()
        elif row11 or row22 or row33 or columns11 or columns33 or columns22 or diagonal11 or diagonal22:
            print("O kazandı! TEBRİKLER..")
            time.sleep(2)
            tekrar = input("Tekrar oynamak ister misiniz? E/H")
            if tekrar == "E" or tekrar == "e":
                self.PlayGame()
            else:
                print("Çıkış yapılıyor")
                time.sleep(2)
                quit()
            time.sleep(2)
        elif "-" not in self.board:

            print("Berabere Bitti!")
            time.sleep(2)
            tekrar = input("Tekrar oynamak ister misiniz? E/H")
            if tekrar == "E" or tekrar == "e":
                self.PlayGame()
            else:
                print("Çıkış yapılıyor")
                time.sleep(2)
                quit()
            time.sleep(2)




game = Game()
while True:
    game.PlayGame()