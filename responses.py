import random


def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'salut':
        return 'salut connard'
    
    if p_message == 'roll':
        return str(random.randint(1,6))
    
    if p_message == '!help': 
        return "voici la liste des différente commande possible :\n salut : le bot te salurat \n roll choisi un chiffre entre 1 et 6 "
    return "j'ai pas compris retente"
    
