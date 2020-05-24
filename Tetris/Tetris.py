"""
**************************************************************************************************************
Höfundur:       Huldar
Dagsetning:     24.maí 2020
Forrit:         Tetris í python
Upplýsingar:    Upphaflegi tetris leikurinn: https://is.wikipedia.org/wiki/Tetris
                Reglurnar um hvað formin heita, liti, stigagjöf og fleira er hægt að finna á 
                ensku síðunni á wikipedia um tetris.
                Nöfnin á tetrimino-unum er að finna hér: https://tetris.fandom.com/wiki/Tetromino
**************************************************************************************************************
"""

# Import modules
from random import randint  # Random til að láta forritið velja næsta tetrimino af handahófi - Documentation : https://docs.python.org/3/library/random.html
import pyglet # Eining/mát (e. module) sem gerir okkur kleift að spila hljóðskrár og ýmislegt fleira - Documentation : https://pyglet.readthedocs.io/en/latest/index.html
pyglet.options['search_local_libs'] = True  # Leyfum pyglet einingunni að skoða möppuna sem við erum í til að finna hljóðskránna okkar


# Declare dependencies
theme_song = pyglet.media.load("Tetris_theme.ogg")  # Segir forritinu hvaða lag við ætlum að nota
spilari = pyglet.media.Player()                     # Býr til spilara (e. player). Gerir okkur kleift að "loop-a" hljóðskrár

# Stigagjöf
"""
Fyrir 1 línu
100 stig
Fyrir 2 línur
250 stig
Fyrir 3 línur
400 stig
Fyrir 4 línur (einnig þekkt sem Tetris)
800 stig
Fyrir að fá Tetris tvisvar í röð
1200 stig (fást fyrir seinna Tetris-ið)

Þegar leikmaður leggur tetrimino niður með því að hard drop-pa
10 stig fyrir hvern reit sem tetrimino-inn féll niður um í hard drop-pinu
"""
points_1_line = 100
points_2_lines = 250
points_3_lines = 400
points_tetris = 800
points_double_tetris = 1200
points_per_square_hard_drop = 10


# Útbúum tetrimino-a - Þeir eru 7 - Munum eftir að gefa þeim allar þær skipanir sem þeir þurfa að kunna
    # Tetrimino 1 - I
    # Tetrimino 2 - O
    # Tetrimino 3 - T
    # Tetrimino 4 - S
    # Tetrimino 5 - Z
    # Tetrimino 6 - J
    # Tetrimino 7 - L

# Spila tetris lagið í bakgrunninum á meðan leikurinn er í gangi - Loop - Mikilvægt að skilgreina spilarann áður en appið er keyrt
spilari.queue(theme_song)
spilari.loop = True
spilari.play()

# Búum til skjá og setjum leikskjá (e. The Tetris Zone) inn í hann
skjar = pyglet.window.Window()
pyglet.app.run()

# Gerum upphafsskjá sem leyfir þér að smella á "Spila"

# Hliðargluggar
    # Sínum til hliðar, í litlum glugga, hvaða tetrimino er næstur. Tetrimino-ar eru valdir af handahófi
    # Sínum fyrir neðan gluggann stigafjölda
    # Sínum á hvaða borði (e. level) leikmaðurinn er
    # Sínum fjölda lína sem leikmaðurinn hefur tekist að láta hverfa

next_tetrimino = randint(1, 7)

# Setjum tetrimino inn í skjáinn einn í einu

# Látum tetrimino-ana detta, einn í einu, rólega niður

# Snúum tetrimino-inum þegar leikmaðurinn ýtir á upp örina

# Færum tetrimino-inn til hægri/vinstri þegar leikmaðurinn ýtir á hægri/vinstri örvatakkana

# Látum tetrimino-inn detta hratt niður á meðan leikmaðurinn heldur niðri niður örvatakkanum

# Setja þá alla leið niður ef leikmaður ýtir á bilslánna - Þekkt sem "Hard drop"

# Láta tetrimino-a stoppa þegar þeir rekast á annan tetrimino fyrir neðan sig
    # Setja næsta tetrimino af stað þegar núverandi tetrimino stoppar
    # Láta leikinn enda þegar tetrimino er stoppar og er fyrir ofan toppinn á skjánum
        # Þegar leikurinn endar --> Sýna "GAME OVER" og stig leikmanns

# Þegar tetriminoarnir mynda heila, óbrotna, lárétta línu yfir allan leikskjáinn þá hverfa þeira og leikmaðurinn fær
# stig í samræmi við hversu margar línur hurfu samtímis.
    # Láta alla kubba fyrir ofan línuna detta niður þegar línan/línurnar hverfa

print("Forritið keyrði í gegn")