# สร้างโดย ณกฤช เลขไวฑูรย์ ^_^
import random
import datetime
import pytz

bangkok_tz = pytz.timezone('Asia/Bangkok')
nowtime1 = datetime.datetime.now(bangkok_tz)
nowtime2 = nowtime1.strftime("%H:%M:%S")
choices = ['Paper','Rock','Scissors']
choices2 = ['แมว','หมา','หมู','ไก่']
player = False
Com_score = 0
player_score = 0
count = 0
summ = 0

def game_rating():
    print('\nกรุณากรอกคะแนนความชอบให้เกมนี้หน่อยครับ\n(1) แย่มาก       (2) แย่\n(3) ดี           (4) ดีมาก')
    inpoint = int(input('กรุณากรอกคะแนนความชอบของเกมนี้: '))
    if inpoint == 1:
        print('ทางเราขออภัยด้วยที่ทำเกมออกมา แย่มาก :(')
    elif inpoint == 2:
        print('ทางเราขออภัยด้วยที่ทำเกมออกมา แย่ :(')
    elif inpoint == 3:
        print('ทางเราขอขอบคุณคะแนนของท่าน :)')
    elif inpoint == 4:
        print('ทางเราขอขอบคุณคะแนนของท่าน :)')


print(f'-----------------ยินดีต้อนรับสู่ร้านเกม-----------------\n1) เกมเป่ายิงฉุบ         2) เกมทายตัวเลข\n3) เกมทายสัตว์          4) เกม XO\nตอนนี้เวลา {nowtime2}')

inint1 = int(input('กรณากรอกตัวเลข: '))
if inint1 == 1:        
        print('-------------เกมเป่ายิ่งฉุบ-------------\n\nตัวเลือกมี : Paper , Rock , Scissors\nพิมพ์คำว่า Exit เพื่อหยุด')
        while True:        
            player = str(input('เลือกตัวเลือก: ')).capitalize()
            computer = random.choice(choices)
            if player == computer:
                print('Tie!')
                player_score += 1
                Com_score += 1
            else:
                if player == choices[0] and computer == choices[1]: # กระดาษ
                    print(f'You Win Computer คอมออก {computer} แต่คุณออก {player} เลยชนะ')
                    player_score += 1
                elif player == choices[0] and computer == choices[2]: # กระดาษ
                    print(f'You Lose Computer! คอมออก {computer} แต่คุณออก {player} เลยแพ้')
                    Com_score += 1
                else:
                    if player == choices[1] and computer == choices[2]: # ค้อน
                        print(f'You Win Computer คอมออก {computer} แต่คุณออก {player} เลยชนะ')
                        player_score += 1
                    elif player == choices[1] and computer == choices[0]: # ค้อน
                        print(f'You Lose Computer! คอมออก {computer} แต่คุณออก {player} เลยแพ้')
                        Com_score += 1
                    else:
                        if player == choices[2] and computer == choices[0]: # กระดาษ
                            print(f'You Win Computer คอมออก {computer} แค่คุณออก {player} เลยชนะ')
                            player_score += 1
                        elif player == choices[2] and computer== choices[1]: # กระดาษ
                            print(f'Your Lose Computer! คอมออก {computer} แต่คุณออก {player} เลยแพ้')
                            Com_score += 1
                        else:
                            if player == 'Exit':
                                if Com_score > player_score:
                                    print(f'คอมชนะคุณ!\nคะแนนคอมคือ {Com_score}\nคะแนนของคุณคือ {player_score} !')
                                    game_rating();break                      
                                elif Com_score < player_score:
                                    print(f'คอมแพ้คุณ!\nคะแนนคอมคือ {Com_score}\nคะแนนของคุณคือ {player_score} !')
                                    game_rating();break
                                elif Com_score == player_score:
                                    print(f'คอมเสมอกับคุณ!\nคะแนนคอมคือ {Com_score}\nคะแนนของคุณคือ {player_score} !')
                                    game_rating();break 
if inint1 == 2:
    print('-------------เกมทายตัวเลข-------------\n\nตัวเลือกมี : (1) Mode Easy (2) Mode Normal \n          (3) Mode Hard (00) Exit')
    modein = int(input('กรอกโหมด: '))
    if modein == 1:
        print('\nโหมดนี้จะมีตัวเลขให้เลือก 1-10')
        while True:
            computer = random.randint(1,10)
            modeinint = int(input('กรอกหมายเลขที่ต้องการจะทาย: '))
            if modeinint == computer:
                print(f'คุณทายถูก คำตอบก็คือ: {modeinint}')
                player_score += 1
                modein1 = str(input('อยากจะเล่นอีกรอบไหม? (Yes/No) : '))
                if modein1 == 'Yes':
                    count == 0 
                elif modein1 == 'No':
                    print(f'คุณตอบผิดไป: {count} ครั้ง') 
                    if count == 0:
                        print('ระดับของคุณคือ: เก่งมาก และ ดวงดีมาก')
                        game_rating();break 
                    elif count <= 5:
                        print('ระดับของคุณคือ: ระดับปางกลาง ดวงปกติ ')
                        game_rating();break 
                    elif count > 5:
                        print('ระดับของคุณคือ: ดวงแย่มาก')
                        game_rating();break 
            elif modeinint == 00:
                print(f'\nขอบคุณที่เล่นเกมของเรา')
                game_rating();break
            elif modeinint > computer:
                print(f'คุณทายไม่ถูก คำตอบมีค่ามากกว่าคำตอบ คำตอบก็คือ {computer}')
                count += 1
            elif modeinint < computer:
                print(f'คุณทายไม่ถูก คำตอบมีค่าน้อยกว่าคำตอบ คำตอบก็คือ {computer}')
                count += 1
            elif modeinint == 0:
                print('คุณต้องกรอกใหม่น่ะ เกมนี้ไม่มี 0')
            elif modeinint < 0:
                print('คุณต้องกรอกใหม่น่ะ เกมนี้ไม่มีเลข จำนวนเต็มลบ')
            else:
                print('คุณกรอกผิดน่ะ ต้องกรอกใหม่!')
    if modein == 2:
        print('\nโหมดนี้จะมีตัวเลขให้เลือก 1-40')
        while True:
            computer = random.randint(1,40)
            modeinint = int(input('กรอกหมายเลขที่ต้องการจะทาย: '))
            if modeinint == computer:
                print(f'คุณทายถูก คำตอบก็คือ: {modeinint}')
                player_score += 1
                modein1 = str(input('อยากจะเล่นอีกรอบไหม? (Yes/No) : '))
                if modein1 == 'Yes':
                    count == 0 
                elif modein1 == 'No':
                    print(f'คุณตอบผิดไป: {count} ครั้ง') 
                    if count == 0:
                        print('ระดับของคุณคือ: เก่งมาก และ ดวงดีมาก')
                        game_rating();break
                    elif count <= 20:
                        print('ระดับของคุณคือ: ระดับปางกลาง ดวงปกติ ')
                        game_rating();break
                    elif count > 20:
                        print('ระดับของคุณคือ: ดวงแย่มาก')
                        game_rating();break 
            elif modeinint == 00:
                print(f'\nขอบคุณที่เล่นเกมของเรา')
                game_rating();break
            elif modeinint > computer:
                print(f'คุณทายไม่ถูก คำตอบมีค่ามากกว่าคำตอบ คำตอบก็คือ {computer}')
                count += 1
            elif modeinint < computer:
                print(f'คุณทายไม่ถูก คำตอบมีค่าน้อยกว่าคำตอบ คำตอบก็คือ {computer}')
                count += 1
            elif modeinint == 0:
                print('คุณต้องกรอกใหม่น่ะ เกมนี้ไม่มี 0')
            elif modeinint < 0:
                print('คุณต้องกรอกใหม่น่ะ เกมนี้ไม่มีเลข จำนวนเต็มลบ')
            else:
                print('คุณกรอกผิดน่ะ ต้องกรอกใหม่!')
    if modein == 3:
        print('\nโหมดนี้จะมีตัวเลขให้เลือก 1-80')
        while True:
            computer = random.randint(1,80)
            modeinint = int(input('กรอกหมายเลขที่ต้องการจะทาย: '))
            if modeinint == computer:
                print(f'คุณทายถูก คำตอบก็คือ: {modeinint}')
                player_score += 1
                modein1 = str(input('อยากจะเล่นอีกรอบไหม? (Yes/No) : '))
                if modein1 == 'Yes':
                    count == 0 
                elif modein1 == 'No':
                    print(f'คุณตอบผิดไป: {count} ครั้ง') 
                    if count == 0:
                        print('ระดับของคุณคือ: เก่งมาก และ ดวงดีมาก')
                        game_rating();break
                    elif count <= 40:
                        print('ระดับของคุณคือ: ระดับปางกลาง ดวงปกติ ')
                        game_rating();break
                    elif count > 40:
                        print('ระดับของคุณคือ: ดวงแย่มาก')
                        game_rating();break
            elif modeinint == 00:
                print(f'\nขอบคุณที่เล่นเกมของเรา')
                game_rating();break
            elif modeinint > computer:
                print(f'คุณทายไม่ถูก คำตอบมีค่ามากกว่าคำตอบ คำตอบก็คือ {computer}')
                count += 1
            elif modeinint < computer:
                print(f'คุณทายไม่ถูก คำตอบมีค่าน้อยกว่าคำตอบ คำตอบก็คือ {computer}')
                count += 1
            elif modeinint == 0:
                print('คุณต้องกรอกใหม่น่ะ เกมนี้ไม่มี 0')
            elif modeinint < 0:
                print('คุณต้องกรอกใหม่น่ะ เกมนี้ไม่มีเลข จำนวนเต็มลบ')
            else:
                print('คุณกรอกผิดน่ะ ต้องกรอกใหม่!')       
if inint1 == 3:
    while True:
        print('-------------เกมทายสัตว์------------\n\nตัวเลือกมี : แมว,หมา,หมู,ไก่')
        intin1 = str(input('คุณพร้อมหรือยัง? (Yes/No): '))
        if intin1 == 'Yes':
            computer = random.choice(choices2)
            if computer == choices2[0]:
                print('เป็นสัตว์ตัวเล็ก น่ารัก ชอบร้อง meow meow')
                strin2 = str(input('กรอกว่าเป็นสัตว์อะไร: '))
                if strin2 != computer:
                    print(f'คุณตอบผิด คำตอบที่แท้จริงคือ {computer}')
                    strin3 = str(input('คุณอยากเล่นใหม่ไหม? (Yes/No): '))                
                    if strin3 == 'Yes':
                        count += 0
                    elif strin3 == 'No':
                        print(f'ขอบคุณที่เล่น\nคะแนนของคุณคือ {count}')
                        game_rating();break
                elif strin2 == computer:
                    print('คำตอบของคุณถูกต้อง!')
                    count += 1    
                    strin3 = str(input('คุณอยากเล่นใหม่ไหม? (Yes/No): '))                
                    if strin3 == 'Yes':
                        count += 0
                    elif strin3 == 'No':
                        print(f'ขอบคุณที่เล่น\nคะแนนของคุณคือ {count}')
                        game_rating();break
            elif computer == choices2[1]:
                print('เป็นสัตว์ที่ รักเจ้าของ ซื่อสัตย์ และชอบเห่า')
                strin2 = str(input('กรอกว่าเป็นสัตว์อะไร: '))
                if strin2 != computer:
                    print(f'คุณตอบผิด คำตอบที่แท้จริงคือ {computer}')
                    strin3 = str(input('คุณอยากเล่นใหม่ไหม? (Yes/No): '))                
                    if strin3 == 'Yes':
                        count += 0
                    elif strin3 == 'No':
                        print(f'ขอบคุณที่เล่น\nคะแนนของคุณคือ {count}')
                        game_rating();break
                elif strin2 == computer:
                    print('คำตอบของคุณถูกต้อง!')
                    count += 1    
                    strin3 = str(input('คุณอยากเล่นใหม่ไหม? (Yes/No): '))              
                    if strin3 == 'Yes':
                        count += 0
                    elif strin3 == 'No':
                        print(f'ขอบคุณที่เล่น\nคะแนนของคุณคือ {count}')
                        game_rating();break
            elif computer == choices2[2]:
                print('เป็นสัตว์ที่ ตัวอ้วน คนส่วนมากกินกัน มี สี่ขา')
                strin2 = str(input('กรอกว่าเป็นสัตว์อะไร: '))
                if strin2 != computer:
                    print(f'คุณตอบผิด คำตอบที่แท้จริงคือ {computer}')
                    strin3 = str(input('คุณอยากเล่นใหม่ไหม? (Yes/No): '))                
                    if strin3 == 'Yes':
                        count += 0
                    elif strin3 == 'No':
                        print(f'ขอบคุณที่เล่น\nคะแนนของคุณคือ {count}')
                        game_rating();break
                elif strin2 == computer:
                    print('คำตอบของคุณถูกต้อง!')
                    count += 1    
                    strin3 = str(input('คุณอยากเล่นใหม่ไหม? (Yes/No): '))                
                    if strin3 == 'Yes':
                        count += 0
                    elif strin3 == 'No':
                        print(f'ขอบคุณที่เล่น\nคะแนนของคุณคือ {count}')
                        game_rating();break
            elif computer == choices2[3]:
                print('เป็นสัตว์ที่ มีปีก แต่บินไม่ได้ อร่อย ยืนสองขา')
                strin2 = str(input('กรอกว่าเป็นสัตว์อะไร: '))
                if strin2 != computer:
                    print(f'คุณตอบผิด คำตอบที่แท้จริงคือ {computer}')
                    strin3 = str(input('คุณอยากเล่นใหม่ไหม? (Yes/No): '))                
                    if strin3 == 'Yes':
                        count += 0
                    elif strin3 == 'No':
                        print(f'ขอบคุณที่เล่น\nคะแนนของคุณคือ {count}')
                        game_rating();break
                elif strin2 == computer:
                    print('คำตอบของคุณถูกต้อง!')
                    count += 1    
                    strin3 = str(input('คุณอยากเล่นใหม่ไหม? (Yes/No): '))                
                    if strin3 == 'Yes':
                        count += 1
                    elif strin3 == 'No':
                        print(f'ขอบคุณที่เล่น\nคะแนนของคุณคือ {count}')
                        game_rating();break
        elif intin1 == 'No':
            print('ถ้าคุนจะไม่เล่นแล้วจะกดเล่นเกมนี้ทำไม?')
            break
if inint1 == 4:
    def print_board(board):
        print("\n".join(["|".join(row) for row in board]))

    def check_win(board, player):
        for i in range(3):
            if board[i][0] == player and board[i][1] == player and board[i][2] == player:
                return True
            if board[0][i] == player and board[1][i] == player and board[2][i] == player:
                return True
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return True
        if board[2][0] == player and board[1][1] == player and board[0][2] == player:
            return True
        return False

    def main():
        board = [[" ", " ", " "] for i in range(3)]
        players = ["X", "O"]
        player_names = []
        for i in range(2):
            player_name = input(f"กรุณากรอกชื่อผู้เล่น {players[i]}: ")
            player_names.append(player_name)
        turn = 0
        while True:
            print_board(board)
            player = players[turn % 2]
            move = input(f"{player_names[turn % 2]} เป็นคนเลือก (แถวแนวนอน, แถวแนวตั้ง (0 - 2)): ")
            row, col = move.split(",")
            row, col = int(row), int(col)
            if board[row][col] != " ":
                print("โปรดกรอกอีกรอบ!")
                continue
            board[row][col] = player
            if check_win(board, player):
                print_board(board)
                print(f"ยินดีด้วย {player_names[turn % 2]} คุณชนะเกมนี้!\nเสียใจด้วย {player_names[(turn + 1) % 2]} คุณแพ้เกมนี้!")
                break
            if all([cell != " " for row in board for cell in row]):
                print_board(board)
                print(f"{player_names[0]} และ {player_names[1]} เสมอกัน!")
                break
            turn += 1 
    if __name__ == "__main__":
        main()