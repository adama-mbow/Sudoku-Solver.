import pygame
import pygame.gfxdraw
from pygame.locals import *
from sudoku_Backtracking import *
from force_brute import *

# Paramettre GUI
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 700
GRID_SIZE = 9
CELL_SIZE = WINDOW_WIDTH // GRID_SIZE

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = ( 0,255, 0)
GRAY = (200, 200, 200)

 #Variables pour le bouton déroulant
options = ["Option 1", "Option 2", "Option 3"]
selected_option = None
size = (400, 300)
#dropdown_rect = pygame.Rect(100, 100, 200, 30)
dropdown_rect = pygame.Rect(100, WINDOW_HEIGHT - 80, 200, 30)






dropdown_open = False




# Initialiser Pygame
pygame.init()

# Creer la fenetre de jeu
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Sudoku Solver")


# Function pour afficher les grilles
def grid():
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(window, BLACK, (x, 0), (x, WINDOW_HEIGHT-200))
    for y in range(0, WINDOW_HEIGHT-200, CELL_SIZE):
        pygame.draw.line(window, BLACK, (0, y), (WINDOW_WIDTH, y))

# Function pour afficher les nombre sur les grilles
def numbers(objet):
    font = pygame.font.Font(None, 36)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            num = objet.grid[i][j]
            numb = objet.original_grid[i][j]
            if num != 0:
                text = font.render(str(num), True, BLUE)
            if numb == 0:
                text = font.render(str(num), True, GREEN)
            text_rect = text.get_rect()
            text_rect.center = (j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2)
            window.blit(text, text_rect)



# tourner le jeu
running = True
file_name = 'evilsudoku.txt'  
solverBacktracking= SudokuSolverBacktracking(file_name)  # Crée une instance de SudokuSolver en utilisant le fichier
solverForceBrute = SudokuSolverForceBrute(file_name)
while running:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            running = False

        
        # ajoute a partir de test.py
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if dropdown_rect.collidepoint(event.pos):
                dropdown_open = not dropdown_open
            elif dropdown_open:
                for i, option in enumerate(options):
                    option_rect = pygame.Rect(dropdown_rect.x, dropdown_rect.y + (i + 1) * dropdown_rect.height,
                                              dropdown_rect.width, dropdown_rect.height)
                    if option_rect.collidepoint(event.pos):
                        selected_option = option
                        dropdown_open = False



    window.fill(WHITE)
    
    #ajoute via test.py
    
    # Dessiner le bouton déroulant
    pygame.draw.rect(window, GRAY, dropdown_rect)
    pygame.draw.rect(window, BLACK, dropdown_rect, 2)
    pygame.draw.line(window, BLACK, (dropdown_rect.x + dropdown_rect.width - 20, dropdown_rect.y + 10),
                     (dropdown_rect.x + dropdown_rect.width - 10, dropdown_rect.y + 20))
    pygame.draw.line(window, BLACK, (dropdown_rect.x + dropdown_rect.width - 10, dropdown_rect.y + 20),
                     (dropdown_rect.x + dropdown_rect.width - 0, dropdown_rect.y + 10))

    # Dessiner les options du bouton déroulant
    if dropdown_open:
        for i, option in enumerate(options):
            option_rect = pygame.Rect(dropdown_rect.x, dropdown_rect.y + (i + 1) * dropdown_rect.height,
                                      dropdown_rect.width, dropdown_rect.height)
            pygame.draw.rect(window, WHITE, option_rect)
            pygame.draw.rect(window, BLACK, option_rect, 2)
            if option == selected_option:
                pygame.draw.rect(window, GRAY, option_rect)

            font = pygame.font.Font(None, 24)
            text = font.render(option, True, BLACK)
            text_rect = text.get_rect()
            text_rect.center = option_rect.center
            window.blit(text, text_rect)


    grid()
    numbers(solverBacktracking)
    
    
    if solverBacktracking.solve_sudoku_backtracking():
        numbers(solverBacktracking)
    else:
        print("No solution found.")

    
    pygame.display.flip() 
    pygame.display.update()

# Quit the game

pygame.quit()
