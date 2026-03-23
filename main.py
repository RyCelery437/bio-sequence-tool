import functions as fun

print("""Welcome to Helix Lab!
Hello! My name is Helix, and I solve molecular biology tasks.
-----------------------------------------------------------""")

choices = [0, 1, 2, 3, 4, 5]

# menu loop
while True:

    print("""What would you like to do?
          
[0] > Exit the program
[1] > Find sDNA / aDNA / mRNA from a given sDNA / aDNA / mRNA
[2] > Find the protein chain from a given mRNA
[3] > Determine the DNA type (template DNA / coding DNA)
[4] > Find the tRNA anticodon from an mRNA / DNA codon
[5] > Count nucleotides in DNA / mRNA
""")
    
    choice = int(input("Your choice: "))

    if choice in choices:

        if choice == 0:   # Exit the program
            print("Exiting program...")
            break


        elif choice == 1:   # Find sDNA / aDNA / mRNA from a given chain

            print("Find sDNA / aDNA / mRNA from a given sDNA / aDNA / mRNA:")

            source_type = input("Input chain type > ").lower()
            target_type = input("Output chain type > ").lower()
            if source_type not in fun.VALID_TYPES or target_type not in fun.VALID_TYPES:
                print("Invalid chain type. Use: 'sDNA', 'aDNA', or 'RNA'")
                continue

            print(fun.convert_chain(source_type, target_type))


        elif choice == 2:   # Find the protein chain from a given mRNA
            
            print("Find the protein chain from a given mRNA:")
            print("")

            mrna = input("Input mRNA > ").lower()

            print(fun.find_protein_chain(mrna))


        elif choice == 3:   # Determine the DNA type (template DNA / coding DNA)
            print("Determine the DNA type (template DNA / coding DNA):")
            print("")

            print("This function is not implemented yet. Check for updates in the future.")


        elif choice == 4:   # Find the tRNA anticodon from an mRNA / DNA codon
            print("Find the tRNA anticodon from an mRNA / DNA codon:")
            print("")

            print("This function is not implemented yet. Check for updates in the future.")

            
        elif choice == 5:   # Count nucleotides in DNA / mRNA
            print("Count nucleotides in DNA / mRNA:")
            print("")

            print("This function is not implemented yet. Check for updates in the future.")

    else:
        print("Unexpected value. Please choose a number from the menu.")