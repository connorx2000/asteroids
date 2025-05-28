import pygame
import random
from pygame import mixer

sound_enabled = False

pygame.init()
try:
    mixer.init()
    sound_enabled = True
except pygame.error:
    print("No sound device detected or accessible. Sound has been disabled!")
    sound_enabled = False

#Default Sounds
explosion_sound = None
shooting_sound = None
damage_sound = None
engine_sound = None

#Default Music
chiptune_music = None
funky_dnb_music = None
gaming_arcade_music = None
polysynth_groove_music = None

#Sound Activate Source
if sound_enabled:
    explosion_sound = mixer.Sound("./sounds/explosion.wav")
    shooting_sound = mixer.Sound("./sounds/shooting.mp3")
    damage_sound = mixer.Sound("./sounds/damage.wav")
    engine_sound = mixer.Sound("./sounds/engine.wav")

    chiptune_music = pygame.mixer.music.load("./sounds/music/chiptune.wav")
    funky_dnb_music = pygame.mixer.music.load("./sounds/music/funky_DnB.wav")
    gaming_arcade_music = pygame.mixer.music.load("./sounds/music/gaming_arcade.wav")
    polysynth_groove_music = pygame.mixer.music.load("./sounds/music/polysynth_groove.wav")

#Sound Dict
sounds = {
    'explosion': explosion_sound,
    'shooting': shooting_sound,
    'damage': damage_sound,
    'engine': engine_sound
}

#Music Dict
music = {
    1: chiptune_music,
    2: funky_dnb_music,
    3: gaming_arcade_music,
    4: polysynth_groove_music
}

def play_sound(name, sound_loop, volume=1.0):
    if sound_enabled and sounds.get(name):
        print(f"Playering sound {name}")
        sound = sounds.get(name)
        sound.set_volume(volume)
        sound.play(loops=sound_loop)
    
def play_music(volume=1.0):
    random_number = random.randint(1, len(music))
    if sound_enabled:
        print(f"Playing music track: {music.get(random_number)}")
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(loops=-1)