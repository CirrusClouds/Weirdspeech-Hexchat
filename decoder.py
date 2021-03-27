import hexchat
import random

__module_name__ = "weirdspeech decoder"
__module_version__ = "1.0"
__module_description__ = "Python module"



def decode(sequence, word_eol, userdata):

    realwords = ("llama", "eel", "ooze", "oomph", "oops", "eerie")

    for i in range(len(sequence)):
        if sequence[i] not in realwords and len(sequence[i]) > 1:
            if sequence[i][0] == sequence[i][1]:
                sequence[i] = sequence[i][1:]
    acc = ""
        
    for i in range(len(sequence)):
        acc = acc + sequence[i] + " "

    # Actually creating and posting the message with context
    
    channel = hexchat.get_info("channel")
    hexchat.command("msg {0} {1}".format(channel, acc))
                   
    return hexchat.EAT_ALL



# Intervenes in any kind of action and sends the input to the function above
hexchat.hook_command("", decode)
