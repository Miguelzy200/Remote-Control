import pygame
import os

def load():
    global switch_on_sprite, switch_off_sprite, button_sprite, disabled_button_sprite, selected_button_sprite
    abspath = os.path.dirname(__file__)
    switch_on_sprite = pygame.image.load(os.path.join(abspath, "switch_on.png")).convert_alpha()
    switch_off_sprite = pygame.image.load(os.path.join(abspath, "switch_off.png")).convert_alpha()
    button_sprite = pygame.image.load(os.path.join(abspath, "seta.png")).convert_alpha()
    disabled_button_sprite = pygame.image.load(os.path.join(abspath, "seta_desabilitada.png")).convert_alpha()
    selected_button_sprite = pygame.image.load(os.path.join(abspath, "seta_selecionada.png")).convert_alpha()
    button_sprite = pygame.transform.scale(button_sprite, (100, 100))
    disabled_button_sprite = pygame.transform.scale(disabled_button_sprite, (100, 100))
    selected_button_sprite = pygame.transform.scale(selected_button_sprite, (100, 100))