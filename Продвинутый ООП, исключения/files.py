class File:
    def __init__(self, name, size, date, owner):
        self.name = name
        self.size = size
        self.date = date
        self.owner = owner
    
    def create(self, name):
        self.name = name
        print(f'Create file: {self.name}')

    def copy(self, new_name):
        print(f'Copy {self.name} to {new_name}')
    
    def move(self, new_name):
        pass
    
    def delete(self):
        pass

class Audio(File):
    def __init__(self):
        self.audio_codec = "mp3"

class Video(File):
    def __init__(self):
        self.video_codec = "flv"

class Photo(File):
    def __init__(self):
        self.resolution = "1024x768"


if __name__ == "__main__":
    audio = Audio()
    audio.create("newaudio.mp3")
    audio.copy("copyed_audio.mp3")
    
