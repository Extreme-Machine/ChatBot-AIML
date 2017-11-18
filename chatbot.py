'''
AIML - Artificial Intelligence Markup Language
Prophecy Bot
'''

import aiml
import os

kernel = aiml.Kernel()

if os.path.isfile("bot_data.dump"):
    print ("Loading form Brain file.")
    kernel.bootstrap(brainFile = "bot_data.dump")
else:
    print ("Parsing Dataset AIML Files")
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_data.dump")

while True:
    input_message = raw_input("User > ")
    if input_message.lower() == "quit":
        exit()
    elif input_message == "save":
        kernel.saveBrain("bot_data.dump")
    else:
        bot_response = kernel.respond(input_message)
        print "Bot > "+ bot_response