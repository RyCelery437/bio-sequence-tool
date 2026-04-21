import functions as fun

print("""Welcome to Helix Lab!
Hello! My name is Helix, and I solve molecular biology tasks.
-----------------------------------------------------------""")

choices = ["0", "1", "2", "3"]

# menu loop
while True:

    print("""What would you like to do?
          
[0] > Exit the program
[1] > Find sDNA / aDNA / mRNA from a given sDNA / aDNA / mRNA
[2] > Find the protein chain from a given mRNA
[3] > Count nucleotides in DNA / mRNA
-----------------------------------------------------------""")
    
    choice = input("Your choice: ")

    if choice in choices:

        if choice == "0":   # Exit the program
            print("Exiting program...")
            break


        elif choice == "1":   # Find sDNA / aDNA / mRNA from a given chain
            while True:

                print("If you want to back to the menu, print 'back' at any time\nFind sDNA / aDNA / RNA from a given sDNA / aDNA / RNA:")
                # source_type
                source_type = input("Input chain type > ").lower()
                if source_type == "back":
                    print("Returning to menu...\n-----------------------------------------------------------")
                    break

                if source_type not in fun.VALID_TYPES:
                    print("Invalid chain type. Use: 'sDNA', 'aDNA', or 'RNA'\n-----------------------------------------------------------")
                    continue

                    
                else:
                    # target_type
                    target_type = input("Output chain type > ").lower()
                    if target_type == "back":
                        print("Returning to menu...\n-----------------------------------------------------------")
                        break

                    if target_type not in fun.VALID_TYPES:
                        print("Invalid chain type. Use: 'sDNA', 'aDNA', or 'RNA'\n-----------------------------------------------------------")
                        continue

                    if source_type == target_type:
                        print("Chain types are the same. No translation needed\n-----------------------------------------------------------")
                        continue

                    output = fun.convert_chain(source_type, target_type)
                    output = "".join(output).upper()
                    print(f"Result: {output}")
                    print("-----------------------------------------------------------")

                    continue


        elif choice == "2":   # Find the protein chain from a given mRNA
            
            print("If you want to back to the menu, print 'back' at any time\nFind the protein chain from a given mRNA:")

            mrna = input("Input mRNA > ").lower()

            output = fun.find_protein_chain(mrna)
            output = "".join(output)
            print(output)

        elif choice == "3":   # Count nucleotides in DNA / mRNA:
            while True:
                print("If you want to back to the menu, print 'back' at any time\nCount nucleotides in DNA / mRNA:")

                break

            
    else:
        print("Unexpected value. Please choose a number from the menu.\n-----------------------------------------------------------")
        continue