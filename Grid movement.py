def ret_pos(grid, value): ## возвращает позицию игрока
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == value:
                output=[i,j]
    return(output)

GRID_SIZE = 3

grid = [[0 for i in range(GRID_SIZE)] for i in range(GRID_SIZE)]
grid[1][1] = 'P'

while True:
    
    
    print('')
    print('Текущая доска:')
    print(grid[0])
    print(grid[1])
    print(grid[2])
    
    
    while True:
        print('')
        print("Куда идем?")
        command = input()
        
        if ret_pos(grid, 'P') == [0,0]:
            if command == 'направо':
                grid[0][0], grid[0][1] = grid[0][1], grid[0][0]
                break
            elif command == 'вниз':
                grid[0][0], grid[1][0] = grid[1][0], grid[0][0]
                break
            else:
                print('там стена, чувак')
                continue
        
        elif ret_pos(grid, 'P') == [0,1]:
            if command == 'налево':
                grid[0][1], grid[0][0] = grid[0][0], grid[0][1] 
                break
            elif command == 'вниз':
                grid[0][1], grid[1][1] = grid[1][1], grid[0][1] 
                break
            elif command == 'направо':
                grid[0][1], grid[0][2] = grid[0][2], grid[0][1]
                break
            else:
                print('там стена, чувак')
                continue
            
        elif ret_pos(grid, 'P') == [0,2]:
            if command == 'налево':
                grid[0][1], grid[0][2] = grid[0][2], grid[0][1] 
                break
            elif command == 'вниз':
                grid[0][2], grid[1][2] = grid[1][2], grid[0][2]
                break
            else:
                print('там стена, чувак')
                continue
            
            
        elif ret_pos(grid, 'P') == [1,0]:
            if command == 'наверх':
                grid[0][0], grid[1][0] = grid[1][0], grid[0][0] 
                break
            elif command == 'направо':
                grid[1][0], grid[1][1] = grid[1][1], grid[1][0]
                break
            elif command == 'вниз':
                grid[1][0], grid[2][0] = grid[2][0], grid[1][0]
                break
            else:
                print('там стена, чувак')
                continue
            
        elif ret_pos(grid, 'P') == [1,1]:
            if command == 'налево':
                grid[1][1], grid[1][0] = grid[1][0], grid[1][1]
                break
            elif command == 'наверх':
                grid[1][1], grid[0][1] = grid[0][1], grid[1][1]
                break
            elif command == 'направо':
                grid[1][1], grid[1][2] = grid[1][2], grid[1][1]
                break
            elif command == 'вниз':
                grid[1][1], grid[2][1] = grid[2][1], grid[1][1]
                break
            
        elif ret_pos(grid, 'P') == [1,2]:
            if command == 'наверх':
                grid[1][2], grid[0][2] = grid[0][2], grid[1][2] 
                break
            elif command == 'налево':
                grid[1][2], grid[1][1] = grid[1][2], grid[1][1]
                break
            elif command == 'вниз':
                grid[1][2], grid[2][2] = grid[2][2], grid[1][2]
                break
            else:
                print('там стена, чувак')
                continue
            
        elif ret_pos(grid, 'P') == [2,0]:
            if command == 'наверх':
                grid[2][0], grid[1][0] = grid[1][0], grid[2][0] 
                break
            elif command =='вправо':
                grid[2][0], grid[2][1] = grid[2][1], grid[2][0]
                break
            else:
                print('там стена, чувак')
                continue
            
        elif ret_pos(grid, 'P') == [2,1]:
            if command == 'наверх':
                grid[2][1], grid[1][1] = grid[1][1], grid[2][1] 
                break
            elif command == 'налево':
                grid[2][1], grid[2][0] = grid[2][0], grid[2][1]
                break
            elif command == 'направо':
                grid[2][1], grid[2][2] = grid[2][2], grid[2][1]
                break
            else:
                print('там стена, чувак')
                continue
        
        elif ret_pos(grid, 'P') == [2,2]:
            if command == 'налево':
                grid[2][2], grid[2][1] = grid[2][1], grid[2][2] 
                break
            elif command == 'наверх':
                grid[2][2], grid[1][2] = grid[1][2], grid[2][2]
                break
            else:
                print('там стена, чувак')
                continue
