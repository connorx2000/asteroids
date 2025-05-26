import pygame
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

#Sound Activate Source
if sound_enabled:
    explosion_sound = mixer.Sound("./sounds/explosion.wav")
    shooting_sound = mixer.Sound("./sounds/shooting.mp3")
    damage_sound = mixer.SoundType("./sounds/damage.wav")

#Sound Dict
sounds = {
    'explosion': explosion_sound,
    'shooting': shooting_sound,
    'damage': damage_sound
}

def play_sound(name, volume=1.0):
    if sound_enabled and sounds.get(name):
        print(f"Playering sound {name}")
        sound = sounds.get(name)
        sound.set_volume(volume)
        sound.play()
        