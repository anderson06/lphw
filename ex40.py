class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

    def backward_song(self):
        for line in list(reversed(self.lyrics)):
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

sapo = ["O sapo nao lava o pe",
        "Nao lava pq nao quer",
        "Ele mora la na lagoa",
        "Nao lava o pe pq nao quer",
        "Mas que chule"]

sapo_song = Song(sapo)

sapo_song.sing_me_a_song()

sapo_song.backward_song()
