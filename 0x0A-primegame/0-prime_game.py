#!/bin/env/python3

"""
This module computes the
winner of the prime game
"""


def isWinner(x, nums):
    """
    Entry point of the computation
    """
    contestant = {'Maria': 0, 'Ben': 0}
    for i in range(x):
        game_map = list(range(1, nums[i]))
        winner = play(game_map)
        if winner:
            contestant[winner] += 1
    return 'Maria' if contestant['Maria'] > contestant['Ben'] else 'Ben'


def play(game_map: list):
    """
    This function represent a round for the game
    """
    curr_player = 0
    if len(game_map) > 0 and game_map[-1] == 1:
        return 'Maria'
    while(len(game_map) > 0):
        game_map = pick(game_map)
        curr_player = curr_player + 1
        if curr_player > 1:
            curr_player = 0
        if (game_map == []):
            return 'Maria' if curr_player == 0 else 'Ben'


def pick(map: list):
    """
    This function picks a prime number
    from the list and removes its multiples
    """
    num = getprime(map)
    if num is None:
        return []
    max_ = map[-1] if len(map) > 1 else map[0]
    map.remove(num)
    while num < max_:
        num = num * num
        if num in map:
            map.remove(num)
        else:
            return map
    return map


def getprime(map):
    """
    This function picks the next
    prime number from the list
    """
    for i in range(len(map)):
        if isprime(map[i]):
            return map[i]
    return None


def isprime(num):
    """
    This function checks if number is a
    prime number
    """
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
