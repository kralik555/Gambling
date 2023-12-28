import random

def spin_wheel():
    return random.randint(0, 36)

colors = {
    'red': [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36],
    'black': [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
}


def reset_loss_streaks(loss_streaks):
    for key in loss_streaks.keys():
        loss_streaks[key] = 0
    return loss_streaks


def reset_bet_values(bet_values):
    for key in bet_values.keys():
        bet_values[key] = 1
    return bet_values


def determine_winning_groups(number):
    groups = []
    if number == 0:
        return groups
    if number in colors['red']:
        groups.append('red')
    else:
        groups.append('black')
    if number % 2 == 0:
        groups.append('even')
    else:
        groups.append('odd')
    if number <= 12:
        groups.append('first')
    elif number <= 24:
        groups.append('second')
    else:
        groups.append('third')
    return groups


def determine_bets_and_double(loss_streaks, bet_values):
    bets = {}
    for bet_type in ['red', 'black', 'odd', 'even']:
        if loss_streaks[bet_type] >= 5:
            bets[bet_type] = bet_values[bet_type]
            bet_values[bet_type] *= 2
    for bet_type in ['first', 'second', 'third']:
        if loss_streaks[bet_type] >= 10:
            bets[bet_type] = bet_values[bet_type]
            bet_values[bet_type] *= 2
    return bets


def update_loss_streaks(loss_streaks, winning_groups):
    for k in loss_streaks.keys():
        loss_streaks[k] += 1
        if k in winning_groups:
            loss_streaks[k] = 0
    return loss_streaks


def update_bet_values(bet_values, winning_groups):
    for k in bet_values.keys():
        if k in winning_groups:
            bet_values[k] = 1
    return bet_values


def update_funds(player_funds, bets, winning_groups):
    for key, value in bets.items():
        player_funds -= min(value, 1000)
        if key in winning_groups:
            if key in ['red', 'black', 'odd', 'even']:
                player_funds += 2 * min(value, 1000)
            else:
                player_funds += 3 * min(value, 1000)
    return player_funds

def play_round(loss_streaks, player_funds, bet_values):
    bets = determine_bets_and_double(loss_streaks, bet_values)
    winning_number = spin_wheel()
    winning_groups = determine_winning_groups(winning_number)
    loss_streaks = update_loss_streaks(loss_streaks, winning_groups)
    bet_values = update_bet_values(bet_values, winning_groups)
    player_funds = update_funds(player_funds, bets, winning_groups)
    return loss_streaks, player_funds, bet_values


if __name__ == "__main__":
    loss_streaks = {
            'red': 0,
            'black': 0,
            'odd': 0.,
            'even': 0,
            'first': 0,
            'second': 0,
            'third': 0
    }
    bet_values = {k: 0 for k in loss_streaks.keys()}
    wins = 0
    losses = 0
    rounds_to_win = 0
    rounds_to_loss = 0
    total_money = 0
    for i in range(10000):
        if (losses + wins) % 100 == 0:
            print(f"Wins: {wins}\nLosses: {losses}")
        player_funds = 1000
        loss_streaks = reset_loss_streaks(loss_streaks)
        bet_values = reset_bet_values(bet_values)
        rounds_played = 0
        while 0 < player_funds < 2000:
            loss_streaks, player_funds, bet_values = play_round(loss_streaks, player_funds, bet_values)
            rounds_played += 1
        total_money += player_funds - 1000
        if player_funds <= 0:
            losses += 1
            rounds_to_loss += rounds_played
        else:
            wins += 1
            rounds_to_win += rounds_played
    print(f" Got to 2 000 {wins} times\n Lost all money {losses} times")
    print(f"Total money: {total_money}")

