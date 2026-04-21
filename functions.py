from itertools import chain


VALID_TYPES = {"sdna", "adna", "rna"}

nucleotides_list = ["a", "t", "g", "c", "u"]

rna_list = ["a", "u", "g", "c"]

ADNA_TO_SDNA_PAIRS_AND_BACK = {"c":"g", "t":"a", "g":"c", "a":"t"}

SDNA_TO_RNA_PAIRS = {"a":"a", "t":"u", "g":"g", "c":"c"}
ADNA_TO_RNA_PAIRS = {"a":"u", "t":"a", "g":"c", "c":"g"}

RNA_TO_ADNA_PAIRS = {"u":"a", "a":"t", "c":"g", "g":"c"}
RNA_TO_SDNA_PAIRS = {"u":"t", "a":"a", "c":"c", "g":"g"}


TRANSLATIONS = {
    ("sdna", "adna"): ADNA_TO_SDNA_PAIRS_AND_BACK,
    ("adna", "sdna"): ADNA_TO_SDNA_PAIRS_AND_BACK,

    ("sdna", "rna"): SDNA_TO_RNA_PAIRS,
    ("adna", "rna"): ADNA_TO_RNA_PAIRS,

    ("rna", "sdna"): RNA_TO_SDNA_PAIRS,
    ("rna", "adna"): RNA_TO_ADNA_PAIRS
}

proteids = {
    "uuu": "Phenylalanine", "uuc": "Phenylalanine",
    "uua": "Leucine", "uug": "Leucine",
    "ucu": "Serine", "ucc": "Serine", "uca": "Serine", "ucg": "Serine",
    "uau": "Tyrosine", "uac": "Tyrosine",
    "uaa": "Stop", "uag": "Stop",
    "ugu": "Cysteine", "ugc": "Cysteine",
    "uga": "Stop", "ugg": "Tryptophan",

    "cuu": "Leucine", "cuc": "Leucine", "cua": "Leucine", "cug": "Leucine",
    "ccu": "Proline", "ccc": "Proline", "cca": "Proline", "ccg": "Proline",
    "cau": "Histidine", "cac": "Histidine",
    "caa": "Glutamine", "cag": "Glutamine",
    "cgu": "Arginine", "cgc": "Arginine", "cga": "Arginine", "cgg": "Arginine",

    "auu": "Isoleucine", "auc": "Isoleucine", "aua": "Isoleucine",
    "aug": "Methionine",
    "acu": "Threonine", "acc": "Threonine", "aca": "Threonine", "acg": "Threonine",
    "aau": "Asparagine", "aac": "Asparagine",
    "aaa": "Lysine", "aag": "Lysine",
    "agu": "Serine", "agc": "Serine",
    "aga": "Arginine", "agg": "Arginine",

    "guu": "Valine", "guc": "Valine", "gua": "Valine", "gug": "Valine",
    "gcu": "Alanine", "gcc": "Alanine", "gca": "Alanine", "gcg": "Alanine",
    "gau": "Aspartic acid", "gac": "Aspartic acid",
    "gaa": "Glutamic acid", "gag": "Glutamic acid",
    "ggu": "Glycine", "ggc": "Glycine", "gga": "Glycine", "ggg": "Glycine"
}

# replacing nucleotides in a chain based on the principle of complementarity
    
def convert_chain(source_type, target_type): # finding sDNA / aDNA / mRNA from a given sDNA / aDNA / mRNA
    result = []

    while True:
        chain = input("Enter chain: ").lower()

        if chain == "back":
            print("Returning to menu...")
            return None

        invalid_found = False 

        for n in chain:
            if n not in nucleotides_list:
                print(f"Invalid nucleotide {n} in chain. Check your input\nIf you want to back to the menu, print 'back' at any time")
                print("-----------------------------------------------------------")

                invalid_found = True
                break

        if not invalid_found:
            break

    translator = TRANSLATIONS[(source_type, target_type)]

    for n in chain:
        result.append(translator[n])

    return result
  
            
def find_protein_chain(mrna): # finding the protein chain from a given mRNA
    result = []

    while True:

        if mrna == "back":
            print("Returning to menu...")
            return None

        invalid_found = False

        for n in mrna:
            if n not in rna_list:
                print(f"Invalid nucleotide {n} in chain. Check your input\nIf you want to back to the menu, print 'back' at any time")
                print("-----------------------------------------------------------")
            

                invalid_found = True
                break

        if not invalid_found:
            break

        translator = proteids[n]

        for n in chain:
        result.append(translator[n])


        if invalid_found:
            mrna = input("Enter mRNA chain: ").lower()
            continue

        break

    result = []

    for n in mrna:
        result.append(proteids[n])

    return result
