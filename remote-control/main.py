from pygame.locals import *
import src.assets as assets
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Remote Control")
assets.load()

class Log:
    def __init__(self):
        self.log_list = []
        self.y_offset = 15
        self.removing = False
        self.font = pygame.font.SysFont(None, 20, True)
        self.color = (0,0,0)
    
    def add(self, text):
        self.log_list.append([self.font.render(text, True, (0,0,0)), text])
    
    def draw(self, screen):
        if len(self.log_list) > 5 and not self.removing: self.removing = True
        if self.removing:
            if self.color[0] <= 255:
                self.log_list[0] = [self.font.render(self.log_list[0][1], True, self.color), self.log_list[0][1]]
                self.color = (self.color[0]+1, self.color[1]+1, self.color[2]+1)
            else:
                self.removing = False
                self.color = (0,0,0)
                self.log_list.pop(0)

        for i, txt in enumerate(self.log_list): 
            screen.blit(txt[0], (620, self.y_offset*i))


class Button:
    pressed = False
    def __init__(self, pos, direction, sprite_rotation):
        self.direction = direction
        self.disabled = False
        self.sprites = [pygame.transform.rotate(assets.button_sprite, sprite_rotation), 
                        pygame.transform.rotate(assets.selected_button_sprite, sprite_rotation),
                        pygame.transform.rotate(assets.disabled_button_sprite, sprite_rotation)]
        self.atual = 0
        self.rect = pygame.Rect(0, 0, self.sprites[self.atual].get_width(), self.sprites[self.atual].get_height())
        self.rect.center = pos

    def callback(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pygame.mouse.get_pos()) and not Button.pressed and not self.disabled:
                Button.pressed = True
                self.atual = 1
                log_listener.add(f"Comando: {self.direction}")
                # Add desired function

        elif event.type == MOUSEBUTTONUP and not self.disabled:
            Button.pressed = False
            self.atual = 0
    
    def draw(self, screen):
        if self.disabled: self.atual = 2
        screen.blit(self.sprites[self.atual], self.rect.topleft)


class Switch:
    pressed = False
    def __init__(self, pos, function):
        self.function = function
        self.sprites = [assets.switch_on_sprite, assets.switch_off_sprite]
        self.atual = 0
        self.rect = pygame.Rect(pos[0], pos[1], 
            self.sprites[self.atual].get_width(), self.sprites[self.atual].get_height())
    
    def callback(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pygame.mouse.get_pos()) and not Switch.pressed:
                Switch.pressed = True
                if self.atual: self.atual = 0
                else: self.atual = 1
                log_listener.add(f"Comando: {self.function}")
                # Add desired function

        elif event.type == MOUSEBUTTONUP and Switch.pressed:
            Switch.pressed = False
            
    def draw(self, screen):
        screen.blit(self.sprites[self.atual], (self.rect.topleft))


center = (screen.get_width() / 2, 500)
log_listener = Log()
switch = Switch((20, 20), "Ligar/Desligar")
left_button = Button((center[0]-150, center[1]), "Esquerda", 0)
right_button = Button((center[0]+150, center[1]), "Direita", 180)
foward_button = Button((center[0], center[1]-150), "Frente", 270)
toward_button = Button((center[0], center[1]+150), "Trás", 90)
buttons = [left_button, right_button, foward_button, toward_button]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        for b in buttons: b.callback(event)
        switch.callback(event)
    screen.fill((255,255,255))

    for b in buttons: 
        if switch.atual: b.disabled = True
        else: b.disabled = False
        b.draw(screen)
    log_listener.draw(screen)
    switch.draw(screen)

    pygame.display.flip()