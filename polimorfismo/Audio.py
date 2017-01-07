class AudioFile():
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception('Formato invalido')
        self.filename = filename

class Mp3File(AudioFile):
    ext = 'mp3'
    def play(self):
        print('Tocando: %s' % self.filename)

class WaveFile(AudioFile):
    ext = 'wave'
    def play(self):
        print('Tocando: %s' % self.filename)

mp3 = Mp3File('musica.mp3')
mp3.play()

wave = WaveFile('musica.wave')
wave.play()