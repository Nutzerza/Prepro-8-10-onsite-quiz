"""Squid game 2"""
def main(num):
    """get num loop prind"""
    player = []
    time = 1
    dig = 0
    for i in range(num):
        player.append(i+1)
    while True:
        ren = len(player)
        if ren == 1:
            break
        elif dig < ren and (dig+1) < ren:
            print("Round %d : Person %d killed person %d" %(time, player[dig], player[dig+1]))
            player.pop(dig+1)
            dig += 1
            time += 1
        elif dig < ren and (dig+1) >= ren:
            print("Round %d : Person %d killed person %d" %(time, player[dig], player[0]))
            player.pop(0)
            dig = 0
            time += 1
        else:
            dig = 0
            print("Round %d : Person %d killed person %d" %(time, player[dig], player[dig+1]))
            player.pop(dig+1)
            dig += 1
            time += 1
    print("Person %d is the winner" %player[0])
main(int(input()))
