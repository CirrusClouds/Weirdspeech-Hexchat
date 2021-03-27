import hexchat
import random

__module_name__ = "cirrustalk"
__module_version__ = "1.0"
__module_description__ = "Python module"



def cirrusify(sequence, word_eol, userdata):
    
    exclusions = ("/say", ".tell")

    
    # Editing of message with a lot of conditional junk
    
    
    repeats = 0
    
    for i in range(len(sequence)):
        x = random.uniform(0, 1)
        
        if x < 0.38 and sequence[i] not in exclusions:
            repeats = repeats + 1
            sequence[i] = sequence[i][0] + sequence[i]
    
    if repeats == 0 and (i for i in sequence) not in exclusions and len(sequence) > 4:
        select_word = random.randint(0, (len(sequence) - 1))
        sequence[select_word] = sequence[select_word][0] + sequence[select_word]


    # Bringing the statement back together with a foldl, lisp style!
    
    
    acc = ""
        
    for i in range(len(sequence)):
        acc = acc + sequence[i] + " "

    # Actually creating and posting the message with context
    
    channel = hexchat.get_info("channel")
    hexchat.command("msg {0} {1}".format(channel, acc))
                   
    return hexchat.EAT_ALL



# Intervenes in any kind of action and sends the input to the function above
hexchat.hook_command("", cirrusify)
