
def dfs(i, j, board, visited, empty, n):
    section = []
    stack = [(i, j)]
    while stack:
        x, y = stack.pop()
        if x >= 0 and y >= 0:  
            try:
                if visited[x][y] == False and board[x][y] == n:
                    visited[x][y] = True
                    section.append((x,y))
                    
                    stack.append((x-1, y))
                    stack.append((x+1, y))
                    stack.append((x, y-1))
                    stack.append((x, y+1))
                    
            except IndexError:
                continue
    empty.append(sorted(section))

def standard_0(b):
    tmp = []
    std_x = b[0][0]
    std_y = b[0][1]
    for x, y in b:
        tmp.append((x-std_x, y-std_y))
    return sorted(tmp)


def solution(game_board, table):
    answer = []
    N = len(game_board)

    visited_board = [list(False for _ in range(N)) for _ in range(N)]
    empty_board = []   
    
    visited_table = [list(False for _ in range(N)) for _ in range(N)]
    empty_table = []    

    for i in range(N):
        for j in range(N):
            if visited_board[i][j] == False and game_board[i][j] == 0:
                dfs(i, j, game_board, visited_board, empty_board, 0)

    for i in range(N):
        for j in range(N):
            if visited_table[i][j] == False and table[i][j] == 1:
                dfs(i, j, table, visited_table, empty_table, 1)
    
    blocks = []
    for block in empty_table:
        blocks.append(standard_0(block))


    def match(block):  
        for x in range(N):
            for y in range(N):
                move = []
                for _x, _y in block:
                    new_x = x+_x
                    new_y = y+_y
                    if new_x >= 0 and new_y >=0:  
                        try:
                            _ = game_board[x+_x][y+_y]  
                            move.append((x+_x, y+_y))
                        except IndexError:
                            break
                    else:
                        break
                if len(block) == len(move) and move in empty_board: 
                    empty_board.remove(move)
                    answer.extend(move)
                    return True
        return False

    def rotate_90(block):
        new = []
        for x, y in block:
            new.append((y, N-1 - x))
        return standard_0(new)
        


    for block in blocks:
        for _ in range(4):
            if match(block) == False:      
                block = rotate_90(block)    
            else: 
                break

    return len(answer)