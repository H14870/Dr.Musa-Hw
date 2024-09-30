import random

# إنشاء رزمة البطاقات
cards = [(suit, rank) for suit in ["m","k","p","w"] for rank in range(1, 11)]

# توزيع البطاقات
def distribute_cards(deck):
    random.shuffle(deck)
    player1 = deck[:4]
    player2 = deck[4:8]
    table = deck[8:12]
    deck = deck[12:]
    return player1, player2, table, deck

# عرض البطاقات
def show_cards(player, player_num):
    print(f"بطاقات اللاعب {player_num}:")
    for card in player:
        print(f"{card[1]} من {card[0]}")

# اللعبة الأساسية
def play_game():
    deck = cards.copy()
    player1, player2, table, deck = distribute_cards(deck)
    
    print("البطاقات على الطاولة:")
    for card in table:
        print(f"{card[1]} من {card[0]}")
    print("\n")
    
    show_cards(player1, 1)
    print("\n")
    show_cards(player2, 2)
    
    # اللاعب 1 يقوم بلعب بطاقة
    card_played = player1.pop(0)  # على سبيل المثال
    print(f"\nاللاعب 1 يلعب: {card_played[1]} من {card_played[0]}")

# بدء اللعبة
play_game()