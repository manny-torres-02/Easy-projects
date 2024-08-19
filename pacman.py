"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - can a ghost be eaten?
    """

    if power_pellet_active and touching_ghost == True:
        print("the ghost can be eaten") 
        return True
    elif power_pellet_active == False and touching_ghost == True:
        print("The ghost cannot be eaten")
    elif power_pellet_active == True and touching_ghost == False:
        print("The ghost cannot be eaten")
    else:
        print("The ghost cannot be eaten")

    


def score(touching_power_pellet, touching_dot):
    """Verify that Pac-Man has scored when a power pellet or dot has been eaten.

    :param touching_power_pellet: bool - is the player touching a power pellet?
    :param touching_dot: bool - is the player touching a dot?
    :return: bool - has the player scored or not?
    """
    if touching_power_pellet == True:
        print("The player has scored")
        return True
    elif touching_dot == True:
        print("The player has scored")
        return True 
    else:
        return False 
    
def lose(power_pellet_active, touching_ghost):
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player lost the game?
    """
    if power_pellet_active == False and touching_ghost ++ True:
        print("The player has lost the game")
        return True




def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Trigger the victory event when all dots have been eaten.

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player won the game?
    """

    if has_eaten_all_dots == True and touching_ghost == False and power_pellet_active == True:
        print("The player has won the game")
        return True
    elif has_eaten_all_dots == True and touching_ghost == False and power_pellet_active == False:
        print("The player has won the game")
        return True
    else:
        return False

eat_ghost(True, True)