import time

class SudokuSolverForceBrute:   # nom de la classe en fonction de la methode choisie 
    def __init__(self, file_name):
        self.grid = self.read_sudoku_file(file_name)  # Initialise la grille en lisant le fichier
        self.original_grid = self.read_sudoku_file(file_name)  # Initialise la grille originale

    def read_sudoku_file(self, file_name):
        grid = []  # Liste pour stocker la grille
        with open(file_name, 'r') as file:  # Ouvre le fichier en mode lecture
            for line in file:  # Parcourt les lignes du fichier
                line = line.strip()  # Supprime les espaces vides en début et fin de ligne
                row = []  # Liste pour stocker les chiffres de la ligne
                for char in line:  # Parcourt les caractères de la ligne
                    if char == '_':  # Si le caractère est '_', 
                        row.append(0) # remplacer par le chiffre 0
                    else:
                        row.append(int(char))  # Convertit le caractère en entier et l'ajoute à la ligne
                grid.append(row)  # Ajoute la ligne à la grille
        return grid  # Retourne la grille

    def print_sudoku(self):
        for i in range(9):
            for j in range(9):
                if self.original_grid[i][j] == 0:
                    print('\033[1m' + str(self.grid[i][j]) + '\033[0m', end=' ')  # Affiche en gras les valeurs ajoutées
                else:
                    print(str(self.grid[i][j]), end=' ')  # Affiche les valeurs d'origine
            print()  # Passe à la ligne suivante



#Fonction affichant la grille originale 

    def print_orginal_grid(self):    

        print("Affichage de la grille originale ")
        for i in range(9):
            for j in range(9):
                print(str(self.original_grid[i][j]), end=' ')
            print()         
        print()  # aller a la ligne suivante 



    def is_valid(self, row, col, num):
        for i in range(9):
            if self.grid[row][i] == num or self.grid[i][col] == num:  # Vérifie si le chiffre est déjà présent dans la ligne ou la colonne
                return False

        start_row = (row // 3) * 3  # Détermine le début de la sous-grille 3x3 en fonction de la position de la case
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == num:  # Vérifie si le chiffre est déjà présent dans la sous-grille 3x3
                    return False

        return True  # Le chiffre peut être placé dans la position (row, col)


    def solve_sudoku_brute_force(self):
        def backtrack():
            for row in range(9):
                for col in range(9):
                    if self.grid[row][col] == 0:  # Recherche d'une case vide
                        for num in range(1, 10):  # Essayer tous les chiffres de 1 à 9
                            if self.is_valid(row, col, num):
                                self.grid[row][col] = num  # Place le chiffre dans la case
                                if backtrack(): 
                                    return True
                                self.grid[row][col] = 0  # Annule la valeur si la solution n'est pas valide
                        return False
            return True

        return backtrack()  # Appelle la fonction récursive pour résoudre le Sudoku en partant de la première case

""" 
# Exemple d'utilisation
file_name = 'evilsudoku.txt'
solver = SudokuSolver(file_name)

print("Grille initiale :")
solver.print_sudoku()

if solver.solve_sudoku_brute_force():
    print("\nGrille résolue avec la méthode de force brute :")
    solver.print_sudoku()
else:
    print("Aucune solution trouvée avec la méthode de force brute.")

# Réinitialisation de la grille
solver.grid = solver.read_sudoku_file(file_name)

start_time = time.time() #enregistrer le temps de debut d'éxecution du code
if solver.solve_sudoku_brute_force():
    end_time = time.time() #enregistrer le fin de l'execution 
    print("\nGrille résolue avec la méthodedu backtracking :")
    solver.print_sudoku()
    execution_time = end_time - start_time #calculer le temps d'execution
    print("le Temps d'éxecution :{:.6f} seconde".format(execution_time))
else:
    print("Aucune solution trouvée avec la méthode du backtracking.") """
