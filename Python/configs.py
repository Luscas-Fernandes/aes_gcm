class checkLibraries:
    from sys import exit

    def checkInterferingLibraries(debug_mode: int = 0):
        libraries = ['pycryptodome', 'pycrypto']
        
        try:
            __import__(libraries[1])
            pyCryptoCheck = 1
            if debug_mode:
                print("PyCrypto found!")
        except ImportError:
            pyCryptoCheck = 0


        if(not pyCryptoCheck):
            try:
                __import__("pycryptodome") # not detecting library :c
                if debug_mode:
                    print("PyCryptodome found!")

            except ImportError:
                print(f"Library {libraries[0]} not found. Wish to install it ?")
                
                decisionInstall = input('y\\n: ')

                if(decisionInstall == 'y'):
                    import subprocess
                    subprocess.check_call(["pip3", "install", libraries[0]])
                else:
                    print("Program may crash unexpectedly")
                    """ print("Exiting program") # detect import not working as it should :c, can't make it work proper
                    print("Library not installed")
                    exit(1) """

        else:
            print("PyCrypto library installed, they may interfere with each other")
            print("Please uninstall pyCrypto to avoid conflicts.")
            print("Program exiting with status code 1")
            exit(1)