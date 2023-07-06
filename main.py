
from sudoku_Backtracking import *
from force_brute import *



global solverForceBrute
global solverBacktracking

# interaction avec l'utilisateur via le terminale 

print() 
jeu  = int(input("Veuillez selectionner le niveau de difficulte que vous souhaitez : 1 = facile , 2 = moyen , 3 = difficile , 4 = tres difficile ,5 = tres tres difficile ")) # Choix du niveau 
print()

if int(jeu) == 1 :
   file_name = 'sudoku1.txt'  # Nom du fichier contenant la grille
   solverBacktracking= SudokuSolverBacktracking(file_name)  # Crée une instance de SudokuSolver en utilisant le fichier
   solverForceBrute = SudokuSolverForceBrute(file_name)
   print("bien niveau facile")


elif int(jeu ) == 2:
   file_name = 'sudoku2.txt'  # Nom du fichier contenant la grille
   solverBacktracking= SudokuSolverBacktracking(file_name)  # Crée une instance de SudokuSolver en utilisant le fichier
   solverForceBrute = SudokuSolverForceBrute(file_name)
   print("bien niveau moyen")
   print()


elif int(jeu ) == 3:
   file_name = 'sudoku3.txt'  # Nom du fichier contenant la grille
   solverBacktracking= SudokuSolverBacktracking(file_name)  # Crée une instance de SudokuSolver en utilisant le fichier
   solverForceBrute = SudokuSolverForceBrute(file_name)
   print("bien niveau difficile")
   print()   
   

elif int(jeu ) == 4:
   file_name = 'sudoku4.txt'  # Nom du fichier contenant la grille
   solverBacktracking= SudokuSolverBacktracking(file_name)  # Crée une instance de SudokuSolver en utilisant le fichier
   solverForceBrute = SudokuSolverForceBrute(file_name)
   print("bien niveau tres difficile")
   print()


elif int(jeu ) == 5:
   file_name = 'evilsudoku.txt'  # Nom du fichier contenant la grille
   solverBacktracking= SudokuSolverBacktracking(file_name)  # Crée une instance de SudokuSolver en utilisant le fichier
   solverForceBrute = SudokuSolverForceBrute(file_name)
   print("bien niveau tres tres difficile")
   print()   

# Choix de la methode de resolution 

print()
resolution = int(input("Par quelle methode voudriez vous resoudre le jeu : 1 = Force Brute , 2 = Backtracking "))

if int(resolution) == 2: 

   solverBacktracking.print_orginal_grid()

   print("Grille initiale :")
   solverBacktracking.print_sudoku()  # Affiche la grille initiale

   if solverBacktracking.solve_sudoku_backtracking():  # Résout le Sudoku en utilisant la méthode du backtracking
    print("\nGrille résolue avec la méthode du backtracking :")
    solverBacktracking.print_sudoku()  # Affiche la grille résolue
   else:
    print("Aucune solution trouvée avec la méthode du backtracking.")

   start_time = time.time() #enregistrer le temps de debut d'éxecution du code
   if solverBacktracking.solve_sudoku_backtracking():
    end_time = time.time() #enregistrer le fin de l'execution 
    print("\nGrille résolue avec la méthodedu backtracking :")
    solverBacktracking.print_sudoku()
    execution_time = end_time - start_time #calculer le temps d'execution
    print("le Temps d'éxecution :{:.6f} seconde".format(execution_time))
   else:
    print("Aucune solution trouvée avec la méthode du backtracking.")  



elif int (resolution)== 1:
   
   print("Grille initiale :")
   solverForceBrute.print_sudoku()

   if solverForceBrute.solve_sudoku_brute_force():
    print("\nGrille résolue avec la méthode de force brute :")
    solverForceBrute.print_sudoku()
   else:
    print("Aucune solution trouvée avec la méthode de force brute.")

# Réinitialisation de la grille
   #solverForceBrute.grid = solverForceBrute.read_sudoku_file(file_name)

   start_time = time.time() #enregistrer le temps de debut d'éxecution du code
   if solverForceBrute.solve_sudoku_brute_force():
    end_time = time.time() #enregistrer le fin de l'execution 
    print("\nGrille résolue avec la méthodedu de force brute  :")
    solverForceBrute.print_sudoku()
    execution_time = end_time - start_time #calculer le temps d'execution
    print("le Temps d'éxecution :{:.6f} seconde".format(execution_time))
   else:
    print("Aucune solution trouvée avec la méthode de force brute .") 

   


