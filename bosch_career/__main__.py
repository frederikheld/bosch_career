#!/usr/bin/python

import sys
import getopt

def main (argv=sys.argv[1:]):
    print ("usage: bosch_career [-h|-?|--help]")
    print("")
        
    try:
        opts, args = getopt.getopt(argv, 'h?', ['help'])
    except getopt.GetoptError:
        print("Illegal argument!")
        sys.exit(2)


    for opt, arg in opts:
        if opt in ["-h", "-?", "--help"]:
            print("+------------------------------------------------------------------------------+")
            print("|                            A T T E N T I O N   ! ! !                         |")
            print("+------------------------------------------------------------------------------+")
            print("")
            print("Software developers!")
            print("")
            print("Did you follow a fancy ad on social media that promised you the next step in")
            print("your software career? Did you believe what it said and installed the")
            print("'bosch_career' apt package?")
            print("")
            print("Be warned! A fancy PR department does not make up for the lack of software")
            print("expertise! If you are looking for the next level in your software career, you")
            print("should better look at a real software company!")
            print("")
            print("Real software companies!")
            print("")
            print("This is your chance to hijack some lousy competitor's failed PR stunt! This")
            print("project is open for contributions at")
            print("")
            print("    https://github.com/frederikheld/bosch_career")
            print("")
            print("Send a PR with your company's name and contact for job applications and you")
            print("might be mentioned here in the next release!")
            print("")
            print("Bosch HR!")
            print("")
            print("I told you several times already that fancy pseudo-code does not make for an")
            print("interesting job ad. Using fancy real code without owning the package makes it")
            print("even dangerous! This package could come with any kind of malware while you are")
            print("naively promoting it and calling yourself a respectable software company.")
            print("Please stop making a fool out of yourself! Your developers don't deserve this!")
            print("")
            print("End of message.")

if __name__ == "__main__":
    main(sys.argv[1:])
