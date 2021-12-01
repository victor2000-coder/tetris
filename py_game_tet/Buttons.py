import pygame.mouse


class StandardButton:

    def __init__(self, active_color=None, inactive_color=None, clicked_color=None, contains=None, position=None, sound=None):
        self.active_clr = active_color if active_color is not None else (0, 0, 0)
        self.inactive_clr = inactive_color if inactive_color is not None else active_color
        self.clicked_clr = clicked_color if clicked_color is not None else active_color
        self.height = contains[1] if contains is not None else 0
        self.width = contains[0] if contains is not None else 0
        self.x_pos = position[0] if position is not None else 0
        self.y_pos = position[1] if position is not None else 0
        self.sound = sound

    def draw(self, display, active_color=None, inactive_color=None, clicked_color=None, contains=None, position=None,
             action=None, message=None, sound=None):
        self.inactive_clr = inactive_color if inactive_color is not None else self.inactive_clr
        self.clicked_clr = clicked_color if clicked_color is not None else self.clicked_clr
        self.active_clr = active_color if active_color is not None else self.active_clr
        self.height = contains[1] if contains is not None else self.height
        self.width = contains[0] if contains is not None else self.width
        self.x_pos = position[0] if position is not None else self.x_pos
        self.y_pos = position[1] if position is not None else self.y_pos
        self.sound = sound if sound is not None else self.sound

        mouse_pos = pygame.mouse.get_pos()
        if self.x_pos < mouse_pos[0] < self.x_pos + self.width and self.y_pos < mouse_pos[1] < self.y_pos + self.height:
            click = pygame.mouse.get_pressed()
            if click[0] == 1:
                pygame.draw.rect(display, self.clicked_clr, (self.x_pos, self.y_pos, self.width, self.height))
                if action is not None:
                    action()
                self.sound.play()
                font = pygame.font.SysFont("Comic Sans MS", 30)
                label = font.render(message, 1, (255, 255, 255))
                display.blit(label, (self.x_pos, self.y_pos + self.height / 10))
                pygame.display.update()
            else:
                pygame.draw.rect(display, self.active_clr, (self.x_pos, self.y_pos, self.width, self.height))
        else:
            pygame.draw.rect(display, self.inactive_clr, (self.x_pos, self.y_pos, self.width, self.height))

        font = pygame.font.SysFont("Comic Sans MS", 30)
        label = font.render(message, 1, (255, 255, 255))
        display.blit(label, (self.x_pos, self.y_pos + self.height / 10))

    def get_contains(self):
        return self.width, self.height


class ButtonWithMessage(StandardButton):
    def __init__(self, active_color=None, inactive_color=None, clicked_color=None, contains=None, position=None,
                 action=None, message=None, title=None, sound=None, text_color=(50, 50, 50)):
        self.txt_clr = text_color
        self.active_clr = active_color if active_color is not None else (0, 0, 0)
        self.inactive_clr = inactive_color if inactive_color is not None else active_color
        self.clicked_clr = clicked_color if clicked_color is not None else active_color
        self.height = contains[1] if contains is not None else 0
        self.width = contains[0] if contains is not None else 0
        self.x_pos = position[0] if position is not None else 0
        self.y_pos = position[1] if position is not None else 0
        self.base_height = self.height
        self.message = message
        self.action = action
        self.title = title
        self.sound = sound
        self.length = 0

    def draw(self, display, active_color=None, inactive_color=None, clicked_color=None, contains=None, position=None,
             action=None, message=None, title=None, sound=None, text_color=(50, 50, 50)):
        self.inactive_clr = inactive_color if inactive_color is not None else self.inactive_clr
        self.clicked_clr = clicked_color if clicked_color is not None else self.clicked_clr
        self.active_clr = active_color if active_color is not None else self.active_clr
        self.height = contains[1] if contains is not None else self.height
        self.width = contains[0] if contains is not None else self.width
        self.x_pos = position[0] if position is not None else self.x_pos
        self.y_pos = position[1] if position is not None else self.y_pos
        self.message = message if message is not None else self.message
        self.action = action if action is not None else self.action
        self.title = title if title is not None else self.title
        self.sound = sound if sound is not None else self.sound
        font = pygame.font.SysFont("Comic Sans MS", 30)
        title_label = font.render(self.title, 1, self.txt_clr)
        font = pygame.font.SysFont("Comic Sans MS", 15)
        message_label = font.render(self.message, 1, self.txt_clr)
        self.txt_clr = text_color if text_color != (50, 50, 50) else self.txt_clr

        mouse_pos = pygame.mouse.get_pos()
        if self.x_pos < mouse_pos[0] < self.x_pos + self.width and self.y_pos < mouse_pos[1] < self.y_pos + self.height:
            click = pygame.mouse.get_pressed()
            if click[0] == 1:
                self.sound.play()
                if self.action is not None:
                    self.action()
                display.fill(self.clicked_clr)

                display.blit(title_label, (self.x_pos, self.y_pos + self.base_height / 10))
                return False

                pygame.time.delay(500)
            else:
                if self.height < self.base_height * 1.5:
                    self.height += 2
                    pygame.draw.rect(display, self.active_clr, (self.x_pos, self.y_pos, self.width, self.height))

                else:
                    pygame.draw.rect(display, self.active_clr, (self.x_pos, self.y_pos, self.width, self.height))
                    display.blit(message_label, (self.x_pos, self.y_pos + self.base_height * 1.01))
        else:
            self.height = self.base_height
            pygame.draw.rect(display, self.inactive_clr, (self.x_pos, self.y_pos, self.width, self.height))
        display.blit(title_label, (self.x_pos, self.y_pos + self.base_height / 10))
        return True


class ButtonsSet:
    def __init__(self, position=None):
        self.x_pos = position[0] if position is not None else 0
        self.y_pos = position[1] if position is not None else 0
        self.buttons: StandardButton = []

    def add_component(self, component: StandardButton):
        self.buttons += [component]

    def draw(self, display_, position=None):
        self.x_pos = position[0] if position is not None else self.x_pos
        self.y_pos = position[1] if position is not None else self.y_pos
        temp_y_contains = 0

        for button in self.buttons:
            temp_y_contains += button.get_contains()[1]
        pygame.draw.rect(display_, (0, 0, 0),
                         (self.x_pos - 2, self.y_pos - 2, self.buttons[0].width + 2, temp_y_contains + 2), 2)
        temp_y_contains = 0
        for button in self.buttons:
            b = button.draw(display=display_, position=(position[0], position[1] + temp_y_contains))
            if not b:
                pygame.display.update()
                pygame.time.delay(500)
                break
            temp_y_contains += button.get_contains()[1]
        pygame.display.update()
