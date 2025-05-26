import pygame

class Animation(pygame.sprite.Sprite):
    def __init__(self, x, y, spritesheet, num_frames):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
            
        self.position = pygame.Vector2(x, y)
        self.last_update_time = pygame.time.get_ticks()
        self.spritesheet = spritesheet
        self.num_frames = num_frames

        
    
    def extract_frames(self, row, col):
        frames = []
        frame_width = int(self.spritesheet.get_width() / col)
        frame_height = int(self.spritesheet.get_height() / row)

        for i in range(self.num_frames):
            col_index = i % col
            row_index = i // col
            frame = self.spritesheet.subsurface(pygame.Rect(col_index * frame_width, row_index * frame_height, frame_width, frame_height))
            frames.append(frame)
        return frames
