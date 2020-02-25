import pygame

def type_of_circle(bigger_circle, smaller_circle, distance):
    if bigger_circle == smaller_circle and distance == 0:
        return "THE CIRCLES ARE EQUAL TO EACH OTHER."
    elif distance == 0:
        return "THE GIVEN CIRCLES ARE CONCENTRIC."
    elif distance_between_edges == 0 or distance_between_edges == -2 * smaller_circle:
        return "THE GIVEN CIRCLES ARE TANGENTIAL TO EACH OTHER."
    elif distance_between_edges > 0 or distance_between_edges < -2 * smaller_circle:
        return "THE GIVEN CIRCLES DO NOT INTERSECT EACH OTHER."
    elif distance_between_edges > -2 * smaller_circle and distance_between_edges < 0:
        return "THE GIVEN CIRCLES HAVE TWO POINTS OF INTERSECTION."


def draw(bigger_circle, smaller_circle, distance, message):
    color1 = (0, 255, 255)
    color2 = (255, 255, 0)    
    black = (0, 0, 0)
    white = (255, 255, 255)

    y = bigger_circle + 150
    center_1 = 250 + bigger_circle
    center_2 = center_1 + distance

    font = pygame.font.SysFont('ubuntu', 30)
    display_message = font.render(str(message), True, white, black)
    message_object = display_message.get_rect()
    message_object.center = (450, 650)

    gameDisplay.blit(display_message, message_object)
    pygame.draw.circle(gameDisplay, color1, (center_1, y), bigger_circle, 2)
    pygame.draw.circle(gameDisplay, color2, (center_2, y), smaller_circle, 1)

print()
print("Welcome! This is a Program to Tell the State of Two Circles.")
print()
radius_1 = float(input("Enter the Radius of First Circle: "))
radius_2 = float(input("Enter the Radius of Second Circle: "))
distance = float(input("Enter the Distance between Two Circles: "))

if radius_1 > radius_2:
    bigger_circle = radius_1
    smaller_circle = radius_2
else:
    bigger_circle = radius_2
    smaller_circle = radius_1

distance_between_edges = float(distance - (bigger_circle + smaller_circle))

scale = 300/(2 * (bigger_circle + smaller_circle) + distance_between_edges)

radius_1 = bigger_circle * scale
radius_2 = smaller_circle * scale
new_distance = distance * scale

pygame.init()
gameDisplay = pygame.display.set_mode((900, 900))
pygame.display.set_caption("State of Two Circles")
draw(int(radius_1), int(radius_2), int(new_distance), type_of_circle(bigger_circle, smaller_circle, distance))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
        	pygame.display.quit()
        	pygame.quit()
        	quit()

    pygame.display.update()
