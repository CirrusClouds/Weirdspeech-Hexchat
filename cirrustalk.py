import hexchat
import random

__module_name__ = "cirrustalk"
__module_version__ = "1.0"
__module_description__ = "Python module"



def cirrusify(sequence, word_eol, userdata):
    
    exclusions = ("/say", ".tell")

    """
    Editing of message
    """
    
    repeats = 0
    
    for i in range(len(sequence)):
        x = random.uniform(0, 1)
        
        if x < 0.38 and sequence[i] not in exclusions:
            repeats = repeats + 1
            sequence[i] = sequence[i][0] + sequence[i]
    
    if repeats == 0 and (i for i in sequence) not in exclusions and len(sequence) > 4:
        select_word = random.randint(0, (len(sequence) - 1))
        sequence[select_word] = sequence[select_word][0] + sequence[select_word]

    """
    Bringing the statement back together
    """
    acc = ""
        
    for i in range(len(sequence)):
        acc = acc + sequence[i] + " "
    
    hexchat.command("msg #lainchan {0}".format(acc))
                   
    return hexchat.EAT_ALL


hexchat.hook_command("", cirrusify)
