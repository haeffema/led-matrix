import pygame
from pygame.joystick import Joystick
import Collision
from playground import Playground


class Controller:
    def __init__(self, joystick: Joystick):
        self.Joy = joystick

    def get_button_pressed(self, blo, position, collision: Collision.Collision_Dedektor, playground: Playground):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYHATMOTION:
                hat_x, hat_y = event.value
                if hat_x == -1 and hat_y == 0:
                    blo.rotate(True)  # left
                if hat_x == 1 and hat_y == 0:
                    blo.rotate(False)  # right
            if event.type == pygame.JOYBUTTONDOWN:
                try:
                    if event.button == 1:
                        blo.rotate(False)  # right
                    if event.button == 0:
                        blo.rotate(True)  # left
                    if event.button == 7:
                        return "End!"
                except KeyError:
                    pass

        # Check if button is currently pressed
        if self.Joy.get_button(1) > 0.001:
            blo.rotate(False)  # right

        if self.Joy.get_button(0) > 0.001:
            blo.rotate(True)  # left

        if self.Joy.get_button(7) > 0.001:
            end = "End!"
            return end

        if self.Joy.get_axis(0) < -0.001:
            newposition = (position[0] - 1, position[1])
            if not collision.at_wall(playground, blo, newposition[0]):
                position = newposition

        if self.Joy.get_axis(0) > 0.001:
            newposition = (position[0] + 1, position[1])
            if not collision.at_wall(playground, blo, newposition[0]):
                position = newposition

        return position
