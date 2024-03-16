# function for printing updated board
def board_print():
    print('')
    print(' -', b8, ' -', d8, ' -', f8, ' -', h8, '  8')
    print(a7, ' -', c7, ' -', e7, ' -', g7, ' -', '  7')
    print(' -', b6, ' -', d6, ' -', f6, ' -', h6, '  6')
    print(a5, ' -', c5, ' -', e5, ' -', g5, ' -', '  5')
    print(' -', b4, ' -', d4, ' -', f4, ' -', h4, '  4')
    print(a3, ' -', c3, ' -', e3, ' -', g3, ' -', '  3')
    print(' -', b2, ' -', d2, ' -', f2, ' -', h2, '  2')
    print(a1, ' -', c1, ' -', e1, ' -', g1, ' -', '  1')
    print(' A', ' B', ' C', ' D', ' E', ' F', ' G', ' H')
    print('')


# functiong for ending the game and evaluating scores
def end_game():
    print('')
    print('')
    print('Game Ending...')

    if trapped == 'trapped dark':
        print('[Light Men:', len(remaining_light_men), '; Light King:', len(remaining_light_king), '] =', len(remaining_light_men) + 3 * len(remaining_light_king), 'Points')
        print('[Dark Men:', len(remaining_dark_men), '; Dark King:', len(remaining_dark_king), '] =', len(remaining_dark_men) + 3 * len(remaining_dark_king), 'Points')
        print('Light Player Wins! ')

    elif trapped == 'trapped light':
        print('[Light Men:', len(remaining_light_men), '; Light King:', len(remaining_light_king), '] =', len(remaining_light_men) + 3 * len(remaining_light_king), 'Points')
        print('[Dark Men:', len(remaining_dark_men), '; Dark King:', len(remaining_dark_king), '] =', len(remaining_dark_men) + 3 * len(remaining_dark_king), 'Points')
        print('Dark Player Wins! ')

    elif empty == 'empty dark':
        print('[Light Men:', len(remaining_light_men), '; Light King:', len(remaining_light_king), '] =', len(remaining_light_men) + 3 * len(remaining_light_king), 'Points')
        print('[Dark Men:', len(remaining_dark_men), '; Dark King:', len(remaining_dark_king), '] =', len(remaining_dark_men) + 3 * len(remaining_dark_king), 'Points')
        print('Light Player Wins! ')

    elif empty == 'empty light':
        print('[Light Men:', len(remaining_light_men), '; Light King:', len(remaining_light_king), '] =', len(remaining_light_men) + 3 * len(remaining_light_king), 'Points')
        print('[Dark Men:', len(remaining_dark_men), '; Dark King:', len(remaining_dark_king), '] =', len(remaining_dark_men) + 3 * len(remaining_dark_king), 'Points')
        print('Dark Player Wins! ')

    elif len(remaining_light_men) + 3 * len(remaining_light_king) > len(remaining_dark_men) + 3 * len(remaining_dark_king):
        print('[Light Men:', len(remaining_light_men), '; Light King:', len(remaining_light_king), '] =', len(remaining_light_men) + 3 * len(remaining_light_king), 'Points')
        print('[Dark Men:', len(remaining_dark_men), '; Dark King:', len(remaining_dark_king), '] =', len(remaining_dark_men) + 3 * len(remaining_dark_king), 'Points')
        print('Light Player Wins! ')

    elif len(remaining_light_men) + 3 * len(remaining_light_king) < len(remaining_dark_men) + 3 * len(remaining_dark_king):
        print('[Light Men:', len(remaining_light_men), '; Light King:', len(remaining_light_king), '] =', len(remaining_light_men) + 3 * len(remaining_light_king), 'Points')
        print('[Dark Men:', len(remaining_dark_men), '; Dark King:', len(remaining_dark_king), '] =', len(remaining_dark_men) + 3 * len(remaining_dark_king), 'Points')
        print('Dark Player Wins! ')

    else:
        print('[Light Men:', len(remaining_light_men), '; Light King:', len(remaining_light_king), '] =', len(remaining_light_men) + 3 * len(remaining_light_king), 'Points')
        print('[Dark Men:', len(remaining_dark_men), '; Dark King:', len(remaining_dark_king), '] =', len(remaining_dark_men) + 3 * len(remaining_dark_king), 'Points')
        print('Draw with equal points! ')

    print('Thank you for Playing! Please come again!')


who = 'L'
win = 'no win'
trapped = ''
empty = ''

a1 = c1 = e1 = g1 = b2 = d2 = f2 = h2 = a3 = c3 = e3 = g3 = ' o'
b8 = d8 = f8 = h8 = a7 = c7 = e7 = g7 = b6 = d6 = f6 = h6 = ' x'
b4 = d4 = f4 = h4 = a5 = c5 = e5 = g5 = ' -'
var_list = ['a1', 'c1', 'e1', 'g1', 'b2', 'd2', 'f2', 'h2', 'a3', 'c3', 'e3', 'g3',
            'b4', 'd4', 'f4', 'h4', 'a5', 'c5', 'e5', 'g5',
            'b8', 'd8', 'f8', 'h8', 'a7', 'c7', 'e7', 'g7', 'b6', 'd6', 'f6', 'h6']
var_list_rev = var_list[::-1]

remaining_light_men = []
remaining_dark_men = []
remaining_light_king = []
remaining_dark_king = []

mandatory_move_src = []
mandatory_move_dest = []
mandatory_move_capt = []
mandatory_move_kcapt = []

trapped_piece = []
trapped_pieces_list = []

lcount = 0
dcount = 0

print('Welcome to Checkers!')
board_print()

while win != 'win':

    # while loop if light player still hasn't captured all capturable and it still his turn
    while who == 'L' and win != 'win':

        # for loop for mandatory capturing by light pieces
        for h in var_list:

            # mandatory capturing men
            if vars()[h] == ' o' or h in mandatory_move_dest:

                for i in range(-1, 2, 2):

                    for j in range(-1, 2, 2):
                        possible_lcapture = chr(ord(h[0]) + i) + str(int(h[1]) + j)

                        if possible_lcapture in var_list:

                            if vars()[possible_lcapture] == ' x' or vars()[possible_lcapture] == ' X':
                                lblocked_checker = chr(ord(possible_lcapture[0]) + i) + str(int(possible_lcapture[1]) + j)

                                if lblocked_checker in var_list and vars()[lblocked_checker] == ' -':

                                    if (h not in mandatory_move_src or (h in mandatory_move_src and possible_lcapture not in mandatory_move_capt)) and lblocked_checker not in mandatory_move_src:
                                        mandatory_move_src.append(h)
                                        mandatory_move_capt.append(possible_lcapture)
                                        mandatory_move_dest.append(lblocked_checker)
                                        print('Light Player must Capture Dark Piece at', possible_lcapture.upper(), '.')
                                        print('')

            # mandatory capturing king
            elif vars()[h] == ' O' or h in mandatory_move_dest:

                for i in range(-7, 8):

                    for j in range(-7, 8):

                        if abs(i) == abs(j) and i != 0 and j != 0:
                            possible_lkcapture = chr(ord(h[0]) + i) + str(int(h[1]) + j)

                            if possible_lkcapture in var_list:

                                for k in range(8):

                                    if vars()[possible_lkcapture] == ' x' or vars()[possible_lkcapture] == ' X':
                                        lblocked_checker = chr(ord(possible_lkcapture[0]) + (i * k // abs(i))) + str(int(possible_lkcapture[1]) + (j * k // abs(j)))

                                        if lblocked_checker in var_list and vars()[lblocked_checker] == ' -':

                                            if (h not in mandatory_move_src or (h in mandatory_move_src and possible_lkcapture not in mandatory_move_capt)) and lblocked_checker not in mandatory_move_src:
                                                mandatory_move_src.append(h)
                                                mandatory_move_capt.append(possible_lkcapture)
                                                mandatory_move_dest.append(lblocked_checker)
                                                print('Light Player must Capture Dark Piece at', possible_lkcapture.upper(), '.')
                                                print('')

        # continue inside while loop while there are still capturable pieces or turn to move
        if len(mandatory_move_capt) != 0 or len(mandatory_move_kcapt) != 0 or lcount == 0:

            mandatory_move_src.clear()
            mandatory_move_dest.clear()
            mandatory_move_capt.clear()
            mandatory_move_kcapt.clear()

            lmove = str(input('Light Player to play! Enter your move:'))
            lmove_list = lmove.split(' ')
            lsource = lmove_list[0].lower()

            # input 'end', game ends immediately
            if lmove.lower() == 'end':

                # lists remaining pieces per color and rank
                for rem in var_list:

                    if vars()[rem] == ' o':
                        remaining_light_men.append(rem)

                    elif vars()[rem] == ' O':
                        remaining_light_king.append(rem)

                    elif vars()[rem] == ' x':
                        remaining_dark_men.append(rem)

                    elif vars()[rem] == ' X':
                        remaining_dark_king.append(rem)

                # call function to print results
                end_game()
                win = 'win'

            elif len(lmove_list) >= 2 and lsource in var_list:

                for multi_dest in range(1, len(lmove_list)):
                    ldest = lmove_list[multi_dest].lower()

                    # search for mandatory capture again to update list for movement because capture coordinates is based on list
                    for h in var_list:

                        if vars()[h] == ' o':

                            for i in range(-1, 2, 2):

                                for j in range(-1, 2, 2):
                                    possible_lcapture = chr(ord(h[0]) + i) + str(int(h[1]) + j)

                                    if possible_lcapture in var_list:

                                        if vars()[possible_lcapture] == ' x' or vars()[possible_lcapture] == ' X':
                                            lblocked_checker = chr(ord(possible_lcapture[0]) + i) + str(int(possible_lcapture[1]) + j)

                                            if lblocked_checker in var_list and vars()[lblocked_checker] == ' -':
                                                mandatory_move_src.append(h)
                                                mandatory_move_capt.append(possible_lcapture)
                                                mandatory_move_dest.append(lblocked_checker)

                        elif vars()[h] == ' O':

                            for i in range(-7, 8):

                                for j in range(-7, 8):

                                    if abs(i) == abs(j) and i != 0 and j != 0:
                                        possible_lkcapture = chr(ord(h[0]) + i) + str(int(h[1]) + j)

                                        if possible_lkcapture in var_list:

                                            for k in range(8):

                                                if vars()[possible_lkcapture] == ' x' or vars()[possible_lkcapture] == ' X':
                                                    lblocked_checker = chr(ord(possible_lkcapture[0]) + (i * k // abs(i))) + str(int(possible_lkcapture[1]) + (j * k // abs(j)))

                                                    if lblocked_checker in var_list and vars()[lblocked_checker] == ' -':
                                                        mandatory_move_src.append(h)
                                                        mandatory_move_kcapt.append(possible_lkcapture)
                                                        mandatory_move_dest.append(lblocked_checker)

                    if ldest in var_list and ((ldest in mandatory_move_dest and lsource in mandatory_move_src) or mandatory_move_dest == []):

                        # if move is to the left and below; only capturing for men but no restriction for king
                        if ldest[0] < lsource[0] and ldest[1] < lsource[1]:

                            # men capture backwards
                            if len(mandatory_move_capt) != 0:
                                lcapture = mandatory_move_capt[0]

                                if vars()[lsource] == ' o' and vars()[ldest] == ' -' and (vars()[lcapture] == ' x' or vars()[lcapture] == ' X') and ldest in mandatory_move_dest and abs(int(ldest[1]) - int(lsource[1])) == 2:
                                    vars()[lsource] = ' -'
                                    vars()[ldest] = ' o'
                                    vars()[lcapture] = ' -'
                                    lsource = ldest

                                else:
                                    print('Sorry, Invalid Move! Try again.')
                                    break

                            # king capture backwards
                            elif len(mandatory_move_kcapt) != 0:
                                lkcapture = mandatory_move_kcapt[0]

                                if vars()[lsource] == ' O' and ldest in mandatory_move_dest:
                                    vars()[lsource] = ' -'
                                    vars()[ldest] = ' O'
                                    vars()[lkcapture] = ' -'
                                    lsource = ldest

                                else:
                                    print('Sorry, Invalid Move! Try again.')
                                    break

                            # king move backwards
                            elif vars()[lsource] == ' O' and vars()[ldest] == ' -':
                                vars()[lsource] = ' -'
                                vars()[ldest] = ' O'

                            elif vars()[lsource] == ' o' and vars()[ldest] == ' -':
                                print('Sorry, Invalid Move! Men cannot go backwards unless there is a Capture. Try again.')
                                break

                            elif vars()[lsource] == ' o' and vars()[ldest] == ' -' and ldest not in var_list:
                                print('Sorry, Invalid Move! Move out of range. Try again.')
                                break

                            else:
                                print('Sorry, Invalid Move! Try again.')
                                break

                        # move to the right and below; only capturing for men but no restriction for king
                        elif ldest[0] > lsource[0] and ldest[1] < lsource[1]:

                            if len(mandatory_move_capt) != 0:
                                lcapture = mandatory_move_capt[0]

                                if vars()[lsource] == ' o' and vars()[ldest] == ' -' and (vars()[lcapture] == ' x' or vars()[lcapture] == ' X') and ldest in mandatory_move_dest and abs(int(ldest[1]) - int(lsource[1])) == 2:
                                    vars()[lsource] = ' -'
                                    vars()[ldest] = ' o'
                                    vars()[lcapture] = ' -'
                                    lsource = ldest

                                else:
                                    print('Sorry, Invalid Move! Try again.')
                                    break

                            elif len(mandatory_move_kcapt) != 0:
                                lkcapture = mandatory_move_kcapt[0]

                                if vars()[lsource] == ' O' and ldest in mandatory_move_dest:
                                    vars()[lsource] = ' -'
                                    vars()[ldest] = ' O'
                                    vars()[lkcapture] = ' -'
                                    lsource = ldest

                                else:
                                    print('Sorry, Invalid Move! Try again.')
                                    break

                            elif vars()[lsource] == ' O' and vars()[ldest] == ' -':
                                vars()[lsource] = ' -'
                                vars()[ldest] = ' O'

                            elif vars()[lsource] == ' o' and vars()[ldest] == ' -':
                                print('Sorry, Invalid Move! Men cannot go backwards unless there is a Capture. Try again.')
                                break

                            elif vars()[lsource] == ' o' and vars()[ldest] == ' -' and ldest not in var_list:
                                print('Sorry, Invalid Move! Move out of range. Try again.')
                                break

                            else:
                                print('Sorry, Invalid Move! Try again.')
                                break

                        # move to left and above; no restriction for both men and king
                        elif ldest[0] < lsource[0] and ldest[1] > lsource[1]:

                            if len(mandatory_move_capt) != 0:
                                lcapture = mandatory_move_capt[0]

                                if vars()[lsource] == ' o' and vars()[ldest] == ' -' and (vars()[lcapture] == ' x' or vars()[lcapture] == ' X') and ldest in mandatory_move_dest and abs(int(ldest[1]) - int(lsource[1])) == 2:
                                    vars()[lsource] = ' -'
                                    vars()[ldest] = ' o'
                                    vars()[lcapture] = ' -'
                                    lsource = ldest

                                else:
                                    print('Sorry, Invalid Move! Try again.')
                                    break

                            elif len(mandatory_move_kcapt) != 0:
                                lkcapture = mandatory_move_kcapt[0]

                                if vars()[lsource] == ' O' and ldest in mandatory_move_dest:
                                    vars()[lsource] = ' -'
                                    vars()[ldest] = ' O'
                                    vars()[lkcapture] = ' -'
                                    lsource = ldest

                                else:
                                    print('Sorry, Invalid Move! Try again.')
                                    break

                            elif vars()[lsource] == ' o' and vars()[ldest] == ' -' and ldest == chr(ord(lsource[0]) - 1) + str(int(lsource[1]) + 1):
                                vars()[lsource] = ' -'
                                vars()[ldest] = ' o'

                            elif vars()[lsource] == ' O' and vars()[ldest] == ' -':
                                vars()[lsource] = ' -'
                                vars()[ldest] = ' O'

                            else:
                                print('Sorry, Invalid Move! Try again.')
                                break

                        # move to the right and above; no restriction for both men and king
                        elif ldest[0] > lsource[0] and ldest[1] > lsource[1]:

                            if len(mandatory_move_capt) != 0:
                                lcapture = mandatory_move_capt[0]

                                if vars()[lsource] == ' o' and vars()[ldest] == ' -' and (vars()[lcapture] == ' x' or vars()[lcapture] == ' X') and ldest in mandatory_move_dest and abs(int(ldest[1]) - int(lsource[1])) == 2:
                                    vars()[lsource] = ' -'
                                    vars()[ldest] = ' o'
                                    vars()[lcapture] = ' -'
                                    lsource = ldest

                                else:
                                    print('Sorry, Invalid Move! Try again.')
                                    break

                            elif len(mandatory_move_kcapt) != 0:
                                lkcapture = mandatory_move_kcapt[0]

                                if vars()[lsource] == ' O' and ldest in mandatory_move_dest:
                                    vars()[lsource] = ' -'
                                    vars()[ldest] = ' O'
                                    vars()[lkcapture] = ' -'
                                    lsource = ldest

                                else:
                                    print('Sorry, Invalid Move! Try again.')
                                    break

                            elif vars()[lsource] == ' o' and vars()[ldest] == ' -' and ldest == chr(ord(lsource[0]) + 1) + str(int(lsource[1]) + 1):
                                vars()[lsource] = ' -'
                                vars()[ldest] = ' o'

                            elif vars()[lsource] == ' O' and vars()[ldest] == ' -':
                                vars()[lsource] = ' -'
                                vars()[ldest] = ' O'

                            else:
                                print('Sorry, Invalid Move! Try again.')
                                break

                        else:
                            print('Sorry, Invalid Move! Try again.')
                            break

                        mandatory_move_src.clear()
                        mandatory_move_dest.clear()
                        board_print()
                        print('Light player moved: ', lmove.upper())
                        print('')

                        # if there are still capturable pieces continue to next iteration
                        if len(mandatory_move_capt) != 0 or len(mandatory_move_kcapt) != 0:
                            mandatory_move_capt.clear()
                            mandatory_move_kcapt.clear()
                            lcount += 1
                            continue

                        # if there are no more capturable pieces proceed
                        else:
                            mandatory_move_capt.clear()
                            mandatory_move_kcapt.clear()
                            lcount = 0

                            # if final destination is end row, promote to king
                            if ldest[1] == '8' and vars()[ldest] != ' O':
                                vars()[ldest] = ' O'
                                board_print()
                                print('Light Piece positioned at', ldest.upper(), 'has been promoted to a King.')
                                print('')

                            # this ends the while loop for the light player's turn and assigns who = 'D'
                            who = 'D'
                            win = 'no win'

                    elif (ldest not in mandatory_move_dest and lsource not in mandatory_move_src) and (lsource in var_list and ldest in var_list):
                        print('Sorry, you must Capture the Dark Piece! Try again.')
                        break

                    # if destination is not a valid variable
                    else:
                        print('Sorry, Invalid Move! Try again.')
                        break

            # if source is not a valid variable
            else:
                print('Sorry, Invalid Move! Try again.')
                break

        # if there are no more capturable pieces proceed
        else:
            mandatory_move_capt.clear()
            mandatory_move_kcapt.clear()
            lcount = 0

            # noinspection PyUnboundLocalVariable
            # if final destination is end row, promote to king
            if ldest in var_list and ldest[1] == '8' and vars()[ldest] != ' O':
                vars()[ldest] = ' O'
                board_print()
                print('Light Piece positioned at', ldest.upper(), 'has been promoted to a King.')
                print('')

            # this ends the while loop for the light player's turn and assigns who = 'D'
            who = 'D'
            win = 'no win'
            break

    # checker for if there are trapped or blocked dark pieces
    for h in var_list:

        if vars()[h] == ' X':

            for i in range(-1, 2, 2):

                for j in range(-1, 2, 2):
                    move_trapped_adj = chr(ord(h[0]) + i) + str(int(h[1]) + j)

                    if move_trapped_adj in var_list:

                        if vars()[move_trapped_adj] == ' x' or vars()[move_trapped_adj] == ' X' or vars()[move_trapped_adj] == ' o' or vars()[move_trapped_adj] == ' O':
                            move_trapped_nxt = chr(ord(move_trapped_adj[0]) + i) + str(int(move_trapped_adj[1]) + j)

                            if move_trapped_nxt in var_list and (vars()[move_trapped_nxt] == ' x' or vars()[move_trapped_nxt] == ' x' or vars()[move_trapped_adj] == ' o' or vars()[move_trapped_adj] == ' O'):
                                trapped_piece.append(move_trapped_nxt)

                            elif move_trapped_nxt not in var_list:
                                trapped_piece.append(move_trapped_nxt)

                    elif move_trapped_adj not in var_list:
                        move_trapped_nxt = chr(ord(move_trapped_adj[0]) + i) + str(int(move_trapped_adj[1]) + j)
                        trapped_piece.append(move_trapped_nxt)

            if len(trapped_piece) == 4:
                trapped_pieces_list.append(h)

        elif vars()[h] == ' x':

            for i in range(-1, 2, 2):

                for j in range(-1, 2, 2):
                    move_trapped_adj = chr(ord(h[0]) + i) + str(int(h[1]) + j)

                    if move_trapped_adj in var_list and (move_trapped_adj[0] < h[0] or move_trapped_adj[1] < h[1]):

                        if vars()[move_trapped_adj] == ' x' or vars()[move_trapped_adj] == ' X' or vars()[move_trapped_adj] == ' o' or vars()[move_trapped_adj] == ' O':
                            move_trapped_nxt = chr(ord(move_trapped_adj[0]) + i) + str(int(move_trapped_adj[1]) + j)

                            if move_trapped_nxt in var_list and (vars()[move_trapped_nxt] == ' x' or vars()[move_trapped_nxt] == ' x' or vars()[move_trapped_adj] == ' o' or vars()[move_trapped_adj] == ' O'):
                                trapped_piece.append(move_trapped_nxt)

                            elif move_trapped_nxt not in var_list:
                                trapped_piece.append(move_trapped_nxt)

                    elif move_trapped_adj not in var_list or (move_trapped_adj[0] > h[0] or move_trapped_adj[1] > h[1]):
                        move_trapped_nxt = chr(ord(move_trapped_adj[0]) + i) + str(int(move_trapped_adj[1]) + j)
                        trapped_piece.append(move_trapped_nxt)

            if len(trapped_piece) == 4:
                trapped_pieces_list.append(h)

    # lists remaining pieces per color and rank
    for rem in var_list:

        if vars()[rem] == ' o':
            remaining_light_men.append(rem)

        elif vars()[rem] == ' O':
            remaining_light_king.append(rem)

        elif vars()[rem] == ' x':
            remaining_dark_men.append(rem)

        elif vars()[rem] == ' X':
            remaining_dark_king.append(rem)

    # if there are no more dark pieces
    if len(remaining_dark_king) + len(remaining_dark_men) == 0:
        print('')
        print('There are no more Dark Pieces.')
        empty = 'empty dark'
        end_game()
        win = 'win'

    # if trapped pieces are the only remaining pieces
    elif len(trapped_pieces_list) == len(remaining_dark_king) + len(remaining_dark_men):
        print('')
        print('No more Dark Pieces are able to move.')
        trapped = 'trapped dark'
        end_game()
        win = 'win'

    else:
        remaining_dark_men.clear()
        remaining_dark_king.clear()
        remaining_light_men.clear()
        remaining_light_king.clear()
        trapped_pieces_list.clear()
        trapped_piece.clear()

    # while loop if light player still hasn't captured all capturable and it still his turn
    while who == 'D' and win != 'win':

        # for loop for mandatory capturing by dark pieces
        for h in var_list_rev:

            if vars()[h] == ' x' or h in mandatory_move_dest:

                for i in range(-1, 2, 2):

                    for j in range(-1, 2, 2):
                        possible_dcapture = chr(ord(h[0]) + i) + str(int(h[1]) + j)

                        if possible_dcapture in var_list:

                            if vars()[possible_dcapture] == ' o' or vars()[possible_dcapture] == ' O':
                                dblocked_checker = chr(ord(possible_dcapture[0]) + i) + str(int(possible_dcapture[1]) + j)

                                if dblocked_checker in var_list and vars()[dblocked_checker] == ' -':

                                    if (h not in mandatory_move_src or (h in mandatory_move_src and possible_dcapture not in mandatory_move_capt)) and dblocked_checker not in mandatory_move_src:
                                        mandatory_move_src.append(h)
                                        mandatory_move_capt.append(possible_dcapture)
                                        mandatory_move_dest.append(dblocked_checker)
                                        print('Dark Player must Capture Light Piece at', possible_dcapture.upper(), '.')
                                        print('')

            elif vars()[h] == ' X' or h in mandatory_move_dest:

                for i in range(-7, 8):

                    for j in range(-7, 8):

                        if abs(i) == abs(j) and i != 0 and j != 0:
                            possible_dkcapture = chr(ord(h[0]) + i) + str(int(h[1]) + j)

                            if possible_dkcapture in var_list:

                                for k in range(8):

                                    if vars()[possible_dkcapture] == ' o' or vars()[possible_dkcapture] == ' O':
                                        dblocked_checker = chr(ord(possible_dkcapture[0]) + (i * k // abs(i))) + str(int(possible_dkcapture[1]) + (j * k // abs(j)))

                                        if dblocked_checker in var_list and vars()[dblocked_checker] == ' -':

                                            if (h not in mandatory_move_src or (h in mandatory_move_src and possible_dkcapture not in mandatory_move_capt)) and dblocked_checker not in mandatory_move_src:
                                                mandatory_move_src.append(h)
                                                mandatory_move_capt.append(possible_dkcapture)
                                                mandatory_move_dest.append(dblocked_checker)
                                                print('Dark Player must Capture Light Piece at', possible_dkcapture.upper(), '.')
                                                print('')

        # continue inside while loop while there are still capturable pieces or turn to move
        if len(mandatory_move_capt) != 0 or len(mandatory_move_kcapt) != 0 or dcount == 0:

            mandatory_move_src.clear()
            mandatory_move_dest.clear()
            mandatory_move_capt.clear()
            mandatory_move_kcapt.clear()

            dmove = str(input('Dark Player to play! Enter your move:'))
            dmove_list = dmove.split(' ')
            dsource = dmove_list[0].lower()

            # if input is 'end', game ends immediately
            if dmove.lower() == 'end':

                # lists remaining pieces per color and rank
                for rem in var_list:

                    if vars()[rem] == ' o':
                        remaining_light_men.append(rem)

                    elif vars()[rem] == ' O':
                        remaining_light_king.append(rem)

                    elif vars()[rem] == ' x':
                        remaining_dark_men.append(rem)

                    elif vars()[rem] == ' X':
                        remaining_dark_king.append(rem)

                end_game()
                win = 'win'

            elif len(dmove_list) >= 2 and dsource in var_list:

                for multi_dest in range(1, len(dmove_list)):
                    ddest = dmove_list[multi_dest].lower()

                    for h in var_list:

                        if vars()[h] == ' x':

                            for i in range(-1, 2, 2):

                                for j in range(-1, 2, 2):
                                    possible_dcapture = chr(ord(h[0]) + i) + str(int(h[1]) + j)

                                    if possible_dcapture in var_list:

                                        if vars()[possible_dcapture] == ' o' or vars()[possible_dcapture] == ' O':
                                            dblocked_checker = chr(ord(possible_dcapture[0]) + i) + str(int(possible_dcapture[1]) + j)

                                            if dblocked_checker in var_list and vars()[dblocked_checker] == ' -':
                                                mandatory_move_src.append(h)
                                                mandatory_move_capt.append(possible_dcapture)
                                                mandatory_move_dest.append(dblocked_checker)

                        elif vars()[h] == ' X':

                            for i in range(-7, 8):

                                for j in range(-7, 8):

                                    if abs(i) == abs(j) and i != 0 and j != 0:
                                        possible_dkcapture = chr(ord(h[0]) + i) + str(int(h[1]) + j)

                                        if possible_dkcapture in var_list:

                                            for k in range(8):

                                                if vars()[possible_dkcapture] == ' o' or vars()[possible_dkcapture] == ' O':
                                                    dblocked_checker = chr(ord(possible_dkcapture[0]) + (i * k // abs(i))) + str(int(possible_dkcapture[1]) + (j * k // abs(j)))

                                                    if dblocked_checker in var_list and vars()[dblocked_checker] == ' -':
                                                        mandatory_move_src.append(h)
                                                        mandatory_move_kcapt.append(possible_dkcapture)
                                                        mandatory_move_dest.append(dblocked_checker)

                    if ddest in var_list and ((ddest in mandatory_move_dest and dsource in mandatory_move_src) or mandatory_move_dest == []):

                        # move to left and below; no restriction for both men and king
                        if ddest[0] < dsource[0] and ddest[1] < dsource[1]:

                            if len(mandatory_move_capt) != 0:
                                dcapture = mandatory_move_capt[0]

                                if vars()[dsource] == ' x' and vars()[ddest] == ' -' and (vars()[dcapture] == ' o' or vars()[dcapture] == ' O') and ddest in mandatory_move_dest and abs(int(ddest[1]) - int(dsource[1])) == 2:
                                    vars()[dsource] = ' -'
                                    vars()[ddest] = ' x'
                                    vars()[dcapture] = ' -'
                                    dsource = ddest

                                else:
                                    print('Sorry, Invalid Move! Try again.')
                                    break

                            elif len(mandatory_move_kcapt) != 0:
                                dkcapture = mandatory_move_kcapt[0]

                                if vars()[dsource] == ' X' and ddest in mandatory_move_dest:
                                    vars()[dsource] = ' -'
                                    vars()[ddest] = ' X'
                                    vars()[dkcapture] = ' -'
                                    dsource = ddest

                                else:
                                    print('Sorry, Invalid Move! Try again.')
                                    break

                            elif vars()[dsource] == ' x' and vars()[ddest] == ' -' and ddest == chr(ord(dsource[0]) - 1) + str(int(dsource[1]) - 1):
                                vars()[dsource] = ' -'
                                vars()[ddest] = ' x'

                            elif vars()[dsource] == ' X' and vars()[ddest] == ' -':
                                vars()[dsource] = ' -'
                                vars()[ddest] = ' X'

                            else:
                                print('Sorry, Invalid Move! Try again.')
                                break

                        # move to right and below; no restriction for both men and king
                        elif ddest[0] > dsource[0] and ddest[1] < dsource[1]:

                            if len(mandatory_move_capt) != 0:
                                dcapture = mandatory_move_capt[0]

                                if vars()[dsource] == ' x' and vars()[ddest] == ' -' and (vars()[dcapture] == ' o' or vars()[dcapture] == ' O') and ddest in mandatory_move_dest and abs(int(ddest[1]) - int(dsource[1])) == 2:
                                    vars()[dsource] = ' -'
                                    vars()[ddest] = ' x'
                                    vars()[dcapture] = ' -'
                                    dsource = ddest

                                else:
                                    print('Sorry, Invalid Move! Try again.')
                                    break

                            elif len(mandatory_move_kcapt) != 0:
                                dkcapture = mandatory_move_kcapt[0]

                                if vars()[dsource] == ' X' and ddest in mandatory_move_dest:
                                    vars()[dsource] = ' -'
                                    vars()[ddest] = ' X'
                                    vars()[dkcapture] = ' -'
                                    dsource = ddest

                                else:
                                    print('Sorry, Invalid Move! Try again.')
                                    break

                            elif vars()[dsource] == ' x' and vars()[ddest] == ' -' and ddest == chr(ord(dsource[0]) + 1) + str(int(dsource[1]) - 1):
                                vars()[dsource] = ' -'
                                vars()[ddest] = ' x'

                            elif vars()[dsource] == ' X' and vars()[ddest] == ' -':
                                vars()[dsource] = ' -'
                                vars()[ddest] = ' X'

                            else:
                                print('Sorry, Invalid Move! Try again.')
                                break

                        # move to left and above; only capture for men and no restriction for king
                        elif ddest[0] < dsource[0] and ddest[1] > dsource[1]:

                            if len(mandatory_move_capt) != 0:
                                dcapture = mandatory_move_capt[0]

                                if vars()[dsource] == ' x' and vars()[ddest] == ' -' and (vars()[dcapture] == ' o' or vars()[dcapture] == ' O') and ddest in mandatory_move_dest and abs(int(ddest[1]) - int(dsource[1])) == 2:
                                    vars()[dsource] = ' -'
                                    vars()[ddest] = ' x'
                                    vars()[dcapture] = ' -'
                                    dsource = ddest

                                else:
                                    print('Sorry, Invalid Move! Try again.')
                                    break

                            elif len(mandatory_move_kcapt) != 0:
                                dkcapture = mandatory_move_kcapt[0]

                                if vars()[dsource] == ' X' and ddest in mandatory_move_dest:
                                    vars()[dsource] = ' -'
                                    vars()[ddest] = ' X'
                                    vars()[dkcapture] = ' -'
                                    dsource = ddest

                                else:
                                    print('Sorry, Invalid Move! Try again.')
                                    break

                            elif vars()[dsource] == ' X' and vars()[ddest] == ' -':
                                vars()[dsource] = ' -'
                                vars()[ddest] = ' X'

                            elif vars()[dsource] == ' x' and vars()[ddest] == ' -' and ddest in var_list:
                                print('Sorry, Invalid Move! Men cannot go backwards unless there is a Capture. Try again.')
                                break

                            elif vars()[dsource] == ' x' and vars()[ddest] == ' -' and ddest not in var_list:
                                print('Sorry, Invalid Move! Move out of range. Try again.')
                                break

                            else:
                                print('Sorry, Invalid Move! Try again.')
                                break

                        # move to right and above; only capture for men and no restriction for king
                        elif ddest[0] > dsource[0] and ddest[1] > dsource[1]:

                            if len(mandatory_move_capt) != 0:
                                dcapture = mandatory_move_capt[0]

                                if vars()[dsource] == ' x' and vars()[ddest] == ' -' and (vars()[dcapture] == ' o' or vars()[dcapture] == ' O') and ddest in mandatory_move_dest and abs(int(ddest[1]) - int(dsource[1])) == 2:
                                    vars()[dsource] = ' -'
                                    vars()[ddest] = ' x'
                                    vars()[dcapture] = ' -'
                                    dsource = ddest

                                else:
                                    print('Sorry, Invalid Move! Try again.')
                                    break

                            elif len(mandatory_move_kcapt) != 0:
                                dkcapture = mandatory_move_kcapt[0]

                                if vars()[dsource] == ' X' and ddest in mandatory_move_dest:
                                    vars()[dsource] = ' -'
                                    vars()[ddest] = ' X'
                                    vars()[dkcapture] = ' -'
                                    dsource = ddest

                                else:
                                    print('Sorry, Invalid Move! Try again.')
                                    break

                            elif vars()[dsource] == ' X' and vars()[ddest] == ' -':
                                vars()[dsource] = ' -'
                                vars()[ddest] = ' X'

                            elif vars()[dsource] == ' x' and vars()[ddest] == ' -' and ddest in var_list:
                                print('Sorry, Invalid Move! Men cannot go backwards unless there is a Capture. Try again.')
                                break

                            elif vars()[dsource] == ' x' and vars()[ddest] == ' -' and ddest not in var_list:
                                print('Sorry, Invalid Move! Move out of range. Try again.')
                                break

                            else:
                                print('Sorry, Invalid Move! Try again.')
                                break
                        else:
                            print('Sorry, Invalid Move! Try again.')
                            break

                        mandatory_move_src.clear()
                        mandatory_move_dest.clear()
                        board_print()
                        print('Dark player moved: ', dmove.upper())
                        print('')

                        # if there are still capturable pieces
                        if len(mandatory_move_capt) != 0 or len(mandatory_move_kcapt) != 0:
                            mandatory_move_capt.clear()
                            mandatory_move_kcapt.clear()
                            dcount += 1
                            continue

                        # if there are no more capturable pieces
                        else:
                            mandatory_move_capt.clear()
                            mandatory_move_kcapt.clear()
                            dcount = 0

                            # if final destination is first row, promote to king
                            if ddest[1] == '1' and vars()[ddest] != ' X':
                                vars()[ddest] = ' X'
                                board_print()
                                print('Dark Piece positioned at', ddest.upper(), 'has been promoted to a King.')
                                print('')

                            who = 'L'
                            win = 'no win'

                    elif (ddest not in mandatory_move_dest and dsource not in mandatory_move_src) and (dsource in var_list and ddest in var_list):
                        print('Sorry, you must capture the dark piece! Try again!')
                        break

                    else:
                        print('Sorry, Invalid Move! Try again.')
                        break

            else:
                print('Sorry, Invalid Move! Try again.')
                break

        # if there are no more capturable pieces
        else:
            mandatory_move_capt.clear()
            mandatory_move_kcapt.clear()
            dcount = 0

            # noinspection PyUnboundLocalVariable
            # if final destination is first row, promote to king
            if ddest in var_list and ddest[1] == '1' and vars()[ddest] != ' X':
                vars()[ddest] = ' X'
                board_print()
                print('Dark Piece positioned at', ddest.upper(), 'has been promoted to a King.')
                print('')

            who = 'L'
            win = 'no win'
            break

    # checker for if there are trapped or blocked light pieces
    for h in var_list:

        if vars()[h] == ' O':

            for i in range(-1, 2, 2):

                for j in range(-1, 2, 2):
                    move_trapped_adj = chr(ord(h[0]) + i) + str(int(h[1]) + j)

                    if move_trapped_adj in var_list:

                        if vars()[move_trapped_adj] == ' x' or vars()[move_trapped_adj] == ' X' or vars()[move_trapped_adj] == ' o' or vars()[move_trapped_adj] == ' O':
                            move_trapped_nxt = chr(ord(move_trapped_adj[0]) + i) + str(int(move_trapped_adj[1]) + j)

                            if move_trapped_nxt in var_list and (vars()[move_trapped_nxt] == ' x' or vars()[move_trapped_nxt] == ' x' or vars()[move_trapped_adj] == ' o' or vars()[move_trapped_adj] == ' O'):
                                trapped_piece.append(move_trapped_nxt)

                            elif move_trapped_nxt not in var_list:
                                trapped_piece.append(move_trapped_nxt)

                    elif move_trapped_adj not in var_list:
                        move_trapped_nxt = chr(ord(move_trapped_adj[0]) + i) + str(int(move_trapped_adj[1]) + j)
                        trapped_piece.append(move_trapped_nxt)

            if len(trapped_piece) == 4:
                trapped_pieces_list.append(h)

        elif vars()[h] == ' o':

            for i in range(-1, 2, 2):

                for j in range(-1, 2, 2):
                    move_trapped_adj = chr(ord(h[0]) + i) + str(int(h[1]) + j)

                    if move_trapped_adj in var_list and (move_trapped_adj[0] > h[0] or move_trapped_adj[1] > h[1]):

                        if vars()[move_trapped_adj] == ' x' or vars()[move_trapped_adj] == ' X' or vars()[move_trapped_adj] == ' o' or vars()[move_trapped_adj] == ' O':
                            move_trapped_nxt = chr(ord(move_trapped_adj[0]) + i) + str(int(move_trapped_adj[1]) + j)

                            if move_trapped_nxt in var_list and (vars()[move_trapped_nxt] == ' x' or vars()[move_trapped_nxt] == ' x' or vars()[move_trapped_adj] == ' o' or vars()[move_trapped_adj] == ' O'):
                                trapped_piece.append(move_trapped_nxt)

                            elif move_trapped_nxt not in var_list:
                                trapped_piece.append(move_trapped_nxt)

                    elif move_trapped_adj not in var_list or (move_trapped_adj[0] < h[0] or move_trapped_adj[1] < h[1]):
                        move_trapped_nxt = chr(ord(move_trapped_adj[0]) + i) + str(int(move_trapped_adj[1]) + j)
                        trapped_piece.append(move_trapped_nxt)

            if len(trapped_piece) == 4:
                trapped_pieces_list.append(h)

    # lists remaining pieces per color and rank
    for rem in var_list:

        if vars()[rem] == ' o':
            remaining_light_men.append(rem)

        elif vars()[rem] == ' O':
            remaining_light_king.append(rem)

        elif vars()[rem] == ' x':
            remaining_dark_men.append(rem)

        elif vars()[rem] == ' X':
            remaining_dark_king.append(rem)

    # if there are no more light pieces
    if len(remaining_light_king) + len(remaining_light_men) == 0:
        print('')
        print('There are no more Light Pieces.')
        empty = 'empty light'
        end_game()
        win = 'win'

    # if the only remaining pieces are trapped aready
    elif len(trapped_pieces_list) == len(remaining_light_king) + len(remaining_light_men):
        print('')
        print('No more Light Pieces are able to move.')
        trapped = 'trapped light'
        end_game()
        win = 'win'

    else:
        remaining_dark_men.clear()
        remaining_dark_king.clear()
        remaining_light_men.clear()
        remaining_light_king.clear()
        trapped_pieces_list.clear()
        trapped_piece.clear()