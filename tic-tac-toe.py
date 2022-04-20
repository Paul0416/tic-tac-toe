##Define starting board
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

##Define all possible combinations to win (constant)
winCombinations =[[1,2,3], [4,5,6], [7,8,9], [1,5,9], [3,5,7], [1,4,7], [2,5,8], [3,6,9]]

##Set up array for player inputs (in int) and one for counting the matches
playerInput =[[],[]]
matchCount=[0,0]
turns = 1
stop = False

##Display inital board
for row in board:
    print(row, "\n")
    
while stop == False:
    ##Prevent numbers above 9 to be entered
    while True:
        try:
            position = int(input("Welk nummer kies je? \n"))
            if position in range(10):
                break

        except:
            pass
    ##Player is defined by the 'turns' counter
    player = turns % 2
    if player == 0:
        playerNicename = "O"
    else:
        playerNicename = "X"
        
    ##Updating and displaying the board
    for row in board:
        for i in row:
            if position == i:
                ##Find where the number from the input is^^^^^^^             
                if player == 0:
                    letter = "O"
                    ##Update the input array of player O (turns % 2 == 0)
                    playerInput[0].append(position)
                else:
                    letter = "X"
                    ##Update the input array of player X (turns % 2 == 1)
                    playerInput[1].append(position)
                    
                ##Update the board
                row.pop((position-1) % 3)
                row.insert((position-1) % 3, letter)
        print(row, "\n")
    for combination in winCombinations:
        for i in playerInput[player]:
            if i in combination:
                matchCount[player] += 1
                ##Check how many numbers from the input match with the numbers from each combination ^^^^
        if matchCount[player] == 3:
            print("\n", playerNicename, "heeft gewonnen!")
            stop = True
            ## A player wins if they have managed to obtain a winning combination
        matchCount[player] = 0
    if turns == 9:
        stop = True
        print("Het is gelijkspel!")
    turns += 1


        
