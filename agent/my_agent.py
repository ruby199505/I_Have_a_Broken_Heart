
# coding: utf-8

# In[1]:


import random
from agent import Agent
from card import ALL_CARDS


class MyAgent(Agent):
    '''
    You have to decide which card to play in this round.
    cards_you_have: list of cards in your hand
    cards_played: cards that has been played this round
    heart_broken: heart is broken or not
    info: score information and cards played in previous rounds
    '''
    def play(self, cards_you_have, cards_played, heart_broken, info):

        good_moves = get_good_moves(cards_you_have, cards_played, heart_broken)
        all_numbers = [int(card[1:]) for card in good_moves]
        if cards_played:
            ##跟首家花色 全都是同花色牌
            if _suit[card[0]] in good_moves == 0 or _suit[card[0]] in good_moves == 1 or _suit[card[0]] in good_moves == 2 or _suit[card[0]] in good_moves == 3:
                if _suit[card[0]] in good_moves == 2: ##全黑桃
                    if '♠12' in info:
                        min_num = min(all_numbers, key=lambda x: _number[x]) ##找黑桃數字最小的丟
                        return [card for card in good_moves if card[1:] == min_num]
                    elif '♠12' not in info:
                        if '♠12' not in cards_you_have:
                            numbers_noAK = [num for num in all_numbers if num != 1 and num != 13]
                            max_num = max(numbers_noAK, key=lambda x: _number[x]) ##丟黑桃12以下最大的
                            return [card for card in good_moves if card[1:] == max_num]
                        else:
                            if '♠1' in cards_played or '♠13' in cards_played:
                                return '♠12'
                            else:
                                min_num = min(all_numbers, key=lambda x: _number[x]) ##找黑桃數字最小的丟
                                return [card for card in good_moves if card[1:] == min_num]
                else: ##其他花色
                    min_num = min(all_numbers, key=lambda x: _number[x]) ##找數字最小的丟
                    return [card for card in good_moves if card[1:] == min_num]
            else: ##缺門
                if '♠12' in info:
                        moves_heart = [card for crad in good_moves if card.startswith('♥')]
                        if moves_heart:
                            numbers_heart = [int(card[1:]) for card in moves_heart]
                            max_num = max(numbers_heart, key=lambda x: _number[x]) ##找紅心數字最大的丟
                            return [card for card in moves_heart if card[1:] == max_num] 
                        else:
                            max_num = max(all_number, key=lambda x: _number[x]) ##找其他花色數字最大的丟
                            cards = [card for card in good_moves if card[1:] == max_num]
                            return random.choice(cards)
                elif '♠12' not in info:
                    if '♠12' not in cards_you_have:
                        if '♠1' in good_moves:
                            return '♠1'
                        elif '♠13' in good_moves:
                            return '♠13'
                        else:
                            moves_heart = [card for crad in good_moves if card.startswith('♥')]
                            if moves_heart:
                                numbers_heart = [int(card[1:]) for card in moves_heart]
                                max_num = max(numbers_heart, key=lambda x: _number[x]) ##找紅心數字最大的丟
                                return [card for card in moves_heart if card[1:] == max_num]
                            else:
                                max_num = max(all_numbers, key=lambda x: _number[x]) ##找非紅心數字最大的丟
                                cards = [card for card in good_moves if card[1:] == max_num]
                                return random.choice(cards)
                    else:
                        return '♠12'

        else:    
            if '♠12' not in info:
                if '♠1' in good_moves or '♠13' in good_moves:
                    no_AK = [card for card in good_moves if card != '♠1' and card != '♠13']
                    if no_AK:
                        moves_heart = [card for card in no_AK if card.startswith('♥')]
                        if moves_heart:
                            numbers_heart = [int(card[1:]) for card in moves_heart]
                            min_num = min(numbers_heart, key=lambda x: _number[x]) ##找紅心數字最小的丟
                            return [card for card in moves_heart if card[1:] == min_num]
                        else:
                            numbers_noAK = [int(card[1:]) for card in no_AK]
                            max_num = max(numbers_noAK, key=lambda x: _number[x]) ##找非紅心數字最大的丟
                            cards = [card for card in no_AK if card[1:] == max_num]
                            return random.choice(cards)
                    else:
                        if '♠1' in good_moves and '♠13' in good_moves:
                            return '♠13'
                        elif '♠13' in good_moves:
                            return '♠13'
                        else:
                            return '♠1'
                else:
                    moves_heart = [card for card in good_moves if card.startswith('♥')]
                    if moves_heart:
                        numbers_heart = [int(card[1:]) for card in moves_heart]
                        min_num = min(numbers_heart, key=lambda x: _number[x]) ##找紅心數字最小的丟
                        return [card for card in moves_heart if card[1:] == min_num]
                    else:
                        max_num = max(all_numbers, key=lambda x: _number[x]) ##找非紅心數字最大的丟
                        cards = [card for card in good_moves if card[1:] == max_num]
                        return random.choice(cards)
            else:
                moves_heart = [card for card in good_moves if card.startswith('♥')]
                if moves_heart:
                    numbers_heart = [int(card[1:]) for card in moves_heart]
                    min_num = min(numbers_heart, key=lambda x: _number[x]) ##找紅心數字最小的丟
                    return [card for card in moves_heart if card[1:] == min_num]
                else:
                    max_num = max(all_numbers, key=lambda x: _number[x]) ##找非紅心數字最大的丟
                    cards = [card for card in good_moves if card[1:] == max_num]
                    return random.choice(cards)


    def get_legal_moves(cards_you_have, cards_played, heart_broken=False):
    # write your code ...
        if cards_played:
            suit = cards_played[0][0]
            cards_you_can_play = [card for card in cards_you_have if card.startswith(suit)]
            if cards_you_can_play:
                return cards_you_can_play
            else:
                if  cards_you_have == 13:
                    cards_you_can_play = [card for card in cards_you_have if not card.startswith('♥') and card != '♠12']
                    if cards_you_can_play:
                        return cards_you_can_play
                    else:
                        return cards_you_have
                else:
                    return cards_you_have
        else:
            if '♣2' in cards_you_have:
                return ['♣2']
            else:
                if heart_broken:
                    return cards_you_have
                else:
                    cards_you_can_play = [card for card in cards_you_have if not card.startswith('♥')]               
                    if cards_you_can_play:
                        return cards_you_can_play
                    else:
                        return cards_you_have


    def compute_score(cards):
        score = sum(1 for card in cards if card.startswith('♥'))
        if '♠12' in cards:
            score += 13    
        return score

    def get_good_moves(cards_you_have, cards_played, heart_broken=False):
    # write your code ...
        candidates = get_legal_moves(cards_you_have, cards_played, heart_broken=False)
        if cards_played:
            suit = cards_played[0][0]
            all_numbers = [int(card[1:]) for card in cards_played if card.startswith(suit)]
            max_number = max(all_numbers, key=lambda x: _number[x])
            
            card_score = {}
            for card in candidates:
                card_num = int(card[1:])
                if card.startswith(suit) and (max_number != 1 and card_num > max_number):
                    score = compute_score(cards_played + [card])
                else:
                    score = 0
                card_score[card] = score
            min_score = min(card_score.values())
            return [card for card in candidates if card_score[card] == min_score]
        else:
            card_score = {}
            score_played = compute_score(cards_played)
            for card in candidates:
                card_num = int(card[1:])
                score = compute_score([card])
                card_score[card] = score + score_played
            min_score = min(card_score.values())
            return [card for card in candidates if card_score[card] == min_score]

    '''
    decide cards you want to pass to the player next to you
    0->1, 1->2, 2->3, 3->0

    cards: list of cards in your hand
    '''
    def pass_cards(self, cards):
        JQKA_account, heartJQKA_account = self.JQKA_counter(cards)
        heart_cards = []
        spade_cards = []
        diamond_cards = []
        club_cards = []
        heart_account = 0
        spade_account = 0
        diamond_account = 0
        club_account = 0
        spade_Q = 0
        print('cards=', cards)
        for card in cards:
            card = str(card)
            if card.startswith('♥'):
                heart_account += 1
                heart_cards.append(card)
            if card.startswith('♠'):
                spade_account += 1
                spade_cards.append(card)
            if card.startswith('♦'):
                diamond_account += 1
                diamond_cards.append(card)
            if card.startswith('♣'):
                club_account += 1
                club_cards.append(card)
            if card=='♠12':
                spade_Q = 1
                
        if heart_account>=6 and spade_Q==1 and spade_account==1 and heartJQKA_account>=2:
            mixed_cards = diamond_cards + club_cards
            if heart_account>=2:
                largest_two = sorted(heart_cards)[:2]
                cards_return = largest_two + ['♠12']
            elif heart_account==1:
                largest = self.max_one(mixed_cards)
                cards_return = largest + ['♠12'] + heart_cards
            else:
                largest_two = self.max_two(mixed_cards)
                cards_return = largest_two + ['♠12']
                
        elif spade_account>=4 and spade_Q==0:
            mixed_cards = diamond_cards + club_cards
            if heart_account>=3:
                largest = self.max_one(heart_cards)
                largest_two = self.max_two(heart_cards)
                largest_three = self.max_three(heart_cards)
                if ('♠13'and'♠1') in cards:
                    cards_return = largest + ['♠13', '♠1']
                elif '♠13' in cards and '♠1' not in cards:
                    cards_return = largest_two + ['♠13']
                elif '♠1' in cards and '♠13' not in cards:
                    cards_return = largest_two + ['♠1']
                else:
                    cards_return = largest_three
            elif heart_account==2:
                largest = self.max_one(heart_cards)
                largest_two = self.max_two(heart_cards)
                largest_three = self.max_three(mixed_cards)
                if ('♠13'and'♠1') in cards:
                    cards_return = largest + ['♠13', '♠1']
                elif '♠13' in cards and '♠1' not in cards:
                    cards_return = largest_two + ['♠13']
                elif '♠1' in cards and '♠13' not in cards:
                    cards_return = largest_two + ['♠1']
                else:
                    cards_return = largest_three
            elif heart_account==1:
                largest = sorted(heart_cards)[:1]
                largest_two = self.max_two(mixed_cards)
                largest_three = self.max_three(mixed_cards)
                if ('♠13'and'♠1') in cards:
                    cards_return = largest + ['♠13', '♠1']
                elif '♠13' in cards and '♠1' not in cards:
                    cards_return = largest_two + ['♠13']
                elif '♠1' in cards and '♠13' not in cards:
                    cards_return = largest_two + ['♠1']
                else:
                    cards_return = largest_three
            else:
                largest = self.max_one(mixed_cards)
                largest_two = self.max_two(mixed_cards)
                largest_three = self.max_three(mixed_cards)
                if ('♠13'and'♠1') in cards:
                    cards_return = largest + ['♠13', '♠1']
                elif '♠13' in cards and '♠1' not in cards:
                    cards_return = largest_two + ['♠13']
                elif '♠1' in cards and '♠13' not in cards:
                    cards_return = largest_two + ['♠1']
                else:
                    cards_return = largest_three
        else:
            mixed_account = [heart_account, spade_account, diamond_account, club_account]
            mixed_account.sort()
            if mixed_account[0]==mixed_account[1]==mixed_account[2]:
                if mixed_account[0]==0:
                    cards_return = sorted(cards)[:3]
                elif mixed_account[0]==1:
                    if mixed_account[3]==heart_account:
                        cards_return = spade_cards + diamond_cards + club_cards
                    elif mixed_account[3]==spade_account:
                        cards_return = heart_cards + diamond_cards + club_cards
                    elif mixed_account[3]==diamond_account:
                        cards_return = heart_cards + spade_cards + club_cards
                    else:
                        cards_return = heart_cards + spade_cards + diamond_cards
                elif mixed_account[0]==(2 or 3):
                    if mixed_account[3]==heart_account:
                        cards_return = self.max_three(spade_cards + diamond_cards + club_cards)
                    elif mixed_account[3]==spade_account:
                        cards_return = self.max_three(heart_cards + diamond_cards + club_cards)
                    elif mixed_account[3]==diamond_account:
                        cards_return = self.max_three(heart_cards + spade_cards + club_cards)
                    else:
                        cards_return = self.max_three(heart_cards + spade_cards + diamond_cards)
            elif mixed_account[0]==mixed_account[1]:
                if mixed_account[0]==0:
                    if mixed_account[2]==heart_account:
                        cards_return = self.max_three(heart_cards)
                    elif mixed_account[2]==spade_account:
                        cards_return = self.max_three(spade_cards)
                    elif mixed_account[2]==diamond_account:
                        cards_return = self.max_three(diamond_cards)
                    else:
                        cards_return = self.max_three(club_cards)
                elif mixed_account[0]==1:
                    if mixed_account[2]==heart_account:
                        if mixed_account[3]==spade_account:
                            cards_return = self.max_one(heart_cards) + diamond_cards + club_cards
                        elif mixed_account[3]==diamond_account:
                            cards_return = self.max_one(heart_cards) + spade_cards + club_cards
                        elif mixed_account[3]==club_account:
                            cards_return = self.max_one(heart_cards) + spade_cards + diamond_cards

                    elif mixed_account[2]==spade_account:
                        if mixed_account[3]==heart_account:
                            cards_return = self.max_one(spade_cards) + diamond_cards + club_cards
                        elif mixed_account[3]==diamond_account:
                            cards_return = self.max_one(spade_cards) + heart_cards + club_cards
                        elif mixed_account[3]==club_account:
                            cards_return = self.max_one(spade_cards) + heart_cards + diamond_cards

                    elif mixed_account[2]==diamond_account:
                        if mixed_account[3]==heart_account:
                            cards_return = self.max_one(diamond_cards) + spade_cards + club_cards
                        elif mixed_account[3]==spade_account:
                            cards_return = self.max_one(diamond_cards) + heart_cards + club_cards
                        elif mixed_account[3]==club_account:
                            cards_return = self.max_one(diamond_cards) + heart_cards + spade_cards
                            
                    else:
                        if mixed_account[3]==heart_account:
                            cards_return = self.max_one(club_cards) + spade_cards + diamond_cards
                        elif mixed_account[3]==spade_account:
                            cards_return = self.max_one(club_cards) + heart_cards + diamond_cards
                        elif mixed_account[3]==diamond_account:
                            cards_return = self.max_one(club_cards) + heart_cards + spade_cards

                else:
                    if mixed_account[0]==0 and mixed_account[0]==heart_account:
                        cards_return = self.max_three(spade_cards + diamond_cards + club_cards)
                    elif mixed_account[0]==0 and mixed_account[0]==spade_account:
                        cards_return = self.max_three(heart_cards + diamond_cards + club_cards)
                    elif mixed_account[0]==0 and mixed_account[0]==diamond_account:
                        cards_return = self.max_three(heart_cards + spade_cards + club_cards)
                    elif mixed_account[0]==0 and mixed_account[0]==club_account:
                        cards_return = self.max_three(heart_cards + spade_cards + diamond_cards)

                    if mixed_account[0]==1 and mixed_account[0]==heart_account:
                        cards_return = self.max_two(spade_cards + diamond_cards + club_cards) + heart_cards
                    elif mixed_account[0]==1 and mixed_account[0]==spade_account:
                        cards_return = self.max_two(heart_cards + diamond_cards + club_cards) + spade_cards
                    elif mixed_account[0]==1 and mixed_account[0]==diamond_account:
                        cards_return = self.max_two(heart_cards + spade_cards + club_cards) + diamond_cards
                    elif mixed_account[0]==1 and mixed_account[0]==club_account:
                        cards_return = self.max_two(heart_cards + spade_cards + diamond_cards) + club_cards
                        
                    if mixed_account[0]==2 and mixed_account[0]==heart_account:
                        cards_return = self.max_one(spade_cards + diamond_cards + club_cards) + heart_cards
                    elif mixed_account[0]==2 and mixed_account[0]==spade_account:
                        cards_return = self.max_one(heart_cards + diamond_cards + club_cards) + spade_cards
                    elif mixed_account[0]==2 and mixed_account[0]==diamond_account:
                        cards_return = self.max_one(heart_cards + spade_cards + club_cards) + diamond_cards
                    elif mixed_account[0]==2 and mixed_account[0]==club_account:
                        cards_return = self.max_one(heart_cards + spade_cards + diamond_cards) + club_cards

            else:
                if mixed_account[0]==0:
                    if mixed_account[0]==heart_account:
                        cards_return = self.max_three(spade_cards + diamond_cards + club_cards)
                    elif mixed_account[0]==spade_account:
                        cards_return = self.max_three(heart_cards + diamond_cards + club_cards)
                    elif mixed_account[0]==diamond_account:
                        cards_return = self.max_three(heart_cards + spade_cards + club_cards)
                    elif mixed_account[0]==club_account:
                        cards_return = self.max_three(heart_cards + spade_cards + diamond_cards)
                    
                elif mixed_account[0]==1:
                    if mixed_account[0]==heart_account:
                        cards_return = self.max_two(spade_cards + diamond_cards + club_cards) + heart_cards
                    elif mixed_account[0]==spade_account:
                        cards_return = self.max_two(heart_cards + diamond_cards + club_cards) + spade_cards
                    elif mixed_account[0]==diamond_account:
                        cards_return = self.max_two(heart_cards + spade_cards + club_cards) + diamond_cards
                    elif mixed_account[0]==club_account:
                        cards_return = self.max_two(heart_cards + spade_cards + diamond_cards) + club_cards

                elif mixed_account[0]==2:
                    if mixed_account[0]==heart_account:
                        cards_return = self.max_one(spade_cards + diamond_cards + club_cards) + heart_cards
                    elif mixed_account[0]==spade_account:
                        cards_return = self.max_one(heart_cards + diamond_cards + club_cards) + spade_cards
                    elif mixed_account[0]==diamond_account:
                        cards_return = self.max_one(heart_cards + spade_cards + club_cards) + diamond_cards
                    elif mixed_account[0]==club_account:
                        cards_return = self.max_one(heart_cards + spade_cards + diamond_cards) + club_cards

                else:
                    if mixed_account[0]==heart_account:
                        cards_return = self.max_three(heart_cards)
                    elif mixed_account[0]==spade_account:
                        cards_return = self.max_three(spade_cards)
                    elif mixed_account[0]==diamond_account:
                        cards_return = self.max_three(diamond_cards)
                    elif mixed_account[0]==club_account:
                        cards_return = self.max_three(club_cards)
    
        print(type(cards_return))
        return cards_return


    def JQKA_counter(self, cards):
        JQKA_account = 0
        heartJQKA_account = 0
        for card in cards:
            card = str(card)
            card_numb = int(card[1:])
            if card_numb==1:
                card_numb = 14
            if card_numb>=11:
                JQKA_account += 1
            if card.startswith('♥') and card_numb>=11:
                heartJQKA_account += 1
        return (JQKA_account, heartJQKA_account)


    def max_three(self, cards):
        all_numbs = [14 if int(card[1:])==1 else int(card[1:]) for card in cards]
        max_three_numbs = sorted(all_numbs)[-3:]
        ans = []

        for card in cards:
            if 14 in max_three_numbs:
                if int(card[1:])==1:
                    ans.append(card)
            if int(card[1:]) in max_three_numbs:
                ans.append(card)

        return random.sample(set(ans), 3)


    def max_two(self, cards):
        all_numbs = [14 if int(card[1:])==1 else int(card[1:]) for card in cards]
        max_two_numbs = sorted(all_numbs)[-2:]
        ans = []

        for card in cards:
            if 14 in max_two_numbs:
                if int(card[1:])==1:
                    ans.append(card)
            if int(card[1:]) in max_two_numbs:
                ans.append(card)

        return random.sample(set(ans), 2)


    def max_one(self, cards):
        all_numbs = [14 if int(card[1:])==1 else int(card[1:]) for card in cards]
        max_one_numb = sorted(all_numbs)[-1:]
        ans = []

        for card in cards:
            if 14 in max_one_numb:
                if int(card[1:])==1:
                    ans.append(card)
            if int(card[1:]) in max_one_numb:
                ans.append(card)

        return random.sample(set(ans), 1)

