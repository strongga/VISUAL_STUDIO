import pygame

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Simple Game")

# Set up the clock
clock = pygame.time.Clock()

# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Draw a red circle in the center of the screen
    pygame.draw.circle(screen, (255, 0, 0), (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), 50)

    # Update the screen
    pygame.display.flip()

    # Limit the frame rate to 60 FPS
    clock.tick(60)

# Clean up
pygame.quit()