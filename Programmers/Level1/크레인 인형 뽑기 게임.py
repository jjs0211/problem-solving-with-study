def solution(board, moves):
    basket = []
    cnt = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                basket.append(board[j][i-1])
                board[j][i-1] = 0
                if len(basket) >= 2:
                    if basket[-2] == basket[-1]:
                        del basket[-2]
                        del basket[-1]
                        cnt+=2
                break
            else:
                pass
    return cnt