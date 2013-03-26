import random

def cardgame (placeholder):
    
    num_cards = 0
    while int(num_cards) < 4 or int(num_cards) > 24 or int(num_cards) % 2 != 0:
    	num_cards = raw_input("How many cards would you like? Enter an even number between 4 and 24.\n")
    
    num_cards = int(num_cards)
    
    cards = []
    user_score = 0
    computer_score = 0
    
    count = 1
    while count <= num_cards:
        cards.append(random.randint(1,50))
        count = count + 1
    
    diff_matrix = [[0 for x in xrange(num_cards + 1)] for x in xrange(num_cards + 1)]
    ans_matrix = [[0 for x in xrange(num_cards + 1)] for x in xrange(num_cards + 1)]
   
 
    i = 1
    while i <= num_cards:
        diff_matrix[i][i] = cards[i-1]
        ans_matrix[i][i] = 'F'
        i += 1

    diff = 1
    while diff <= num_cards:
        i = 1
        j = 1
        while i <= num_cards-diff:
            j = i + diff
            diff_matrix[i][j] = max(cards[j-1] - diff_matrix[i][j-1], cards[i-1] - diff_matrix[i+1][j])
            if(cards[j-1] - diff_matrix[i][j-1] > cards[i-1] - diff_matrix[i+1][j]):
                ans_matrix[i][j] = 'L'
            if(cards[j-1] - diff_matrix[i][j-1] <= cards[i-1] - diff_matrix[i+1][j]):
                ans_matrix[i][j] = 'F'
            i += 1
        diff += 1
    print cards

    i = 1
    j = num_cards

    while cards:

        #user enters choice
        user_card = raw_input("choose the first or the last card.(Enter 'F' or 'L')")
    
        if (user_card == 'F' or user_card == 'f'):
            print "First card chosen for a score of", cards[0], ". Your total score is now", (user_score + cards[0])
            user_score += cards.pop(0)
            i = i + 1

        if (user_card =='L' or user_card == 'l'):
            print "Last card chosen for a score of", cards[len(cards)-1], ". Your total score is now", (user_score + cards[len(cards)-1])
            user_score += cards.pop()
            j = j - 1      
       
        print cards, "\n"    
        
        #computer selects choice
        if ans_matrix[i][j] == 'F':
            print "The algorithm selects the first card for a score of", cards[0], ". Computer's total score is now", (computer_score + cards[0])
            computer_score += cards.pop(0)
            i = i + 1
        else:
            print "The algorithm selects the last card for a score of", cards[len(cards)-1], ". Computer's total score is now", (computer_score + cards[len(cards)-1])
            computer_score += cards.pop()
            j = j - 1
         
        if cards:
            print cards, "\n"

    if user_score > computer_score:
        print "You won! Your total score is", user_score, "and the computer's score is", computer_score

    if user_score < computer_score:
        print "The algorthim has won! Your total score is", user_score, "and the computer's score is", computer_score

    if user_score == computer_score:
        print "The game is a draw! Both earned", user_score, "points"

cardgame (1)
