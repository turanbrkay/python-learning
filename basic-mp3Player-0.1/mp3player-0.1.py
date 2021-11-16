import random
import time


class Mp3player():

    def __init__(self,songs=["Mesafe - SerdarOrtaç","Civciv - Tuğkan","Kibrit - OnurcanÖzcan","İstanbul - SezanAksu"],
                 playingsong = "'Song is not playing right now'"):
        self.songs = songs
        self.soundlevel = 100
        self.playingsong = playingsong

    def showMenu(self):
        print("""
        music list = {}
        playing song = {}
        sound level = {}

        1- choose song 
        2- volume up
        3- volume down
        4- random song
        5- add song
        6- del song
        7- quit
         """.format(self.songs, self.playingsong, self.soundlevel))

    def chooseSong(self):
        counter = 1
        for song in self.songs:
            print("{}) {} ".format(counter, song))
            counter += 1

        whichsong = int(input("Enter the number of the song you want to select.."))

        while whichsong < 1 or whichsong > len(self.songs):
            whichsong = int(input("Wrong entry.. Please enter within the specified range."))

        self.playingsong = self.songs[whichsong-1]

    def volumeUp(self):
        if self.soundlevel == 100:
            pass
        else:
            self.soundlevel += 5

    def volumeDown(self):
        if self.soundlevel == 0:
            pass
        else:
            self.soundlevel -= 5

    def addSong(self):
        songname = input("Enter the name of the song you want to add: ")
        singername = input("Enter the name of the singer: ")

        self.songs.append(songname + " - " + singername)

    def chooseRandomSong(self):
        randomsong = random.choice(self.songs)
        print("Choice Song: ",randomsong)

        self.playingsong = randomsong

    def quit(self):
        print("Exiting the program...")
        time.sleep(2)
        quit()

    def choice(self):
        choice = int(input("Make your choice: "))
        while choice > 7 or choice < 0:
            int(input("Please enter numbers 1-7"))

        return choice

    def delSong(self):
        counter = 1
        for song in self.songs:
            print("{}) {} ".format(counter,song))
            counter += 1

        deletesong = int(input("Enter the number of the song you want to delete."))

        while deletesong < 1 or deletesong > len(self.songs):
            deletesong = int(input("Wrong entry...\nPlease enter within the specified range."))

        if self.playingsong == self.songs[deletesong - 1]:
            self.playingsong = "'Song is not playing right now'"
        else:
            pass

        self.songs.pop(deletesong-1)    # listeler 0 dan başlar saymaya

    def play(self):
        self.showMenu()

        sec = self.choice()

        if sec == 1:
            self.chooseSong()
        elif sec == 2:
            self.volumeUp()
        elif sec == 3:
            self.volumeDown()
        elif sec == 4:
            self.chooseRandomSong()
        elif sec == 5:
            self.addSong()


        elif sec == 6:
            self.delSong()
        elif sec == 7:
            self.quit()

mp3calar = Mp3player()

while True:
    mp3calar.play()

