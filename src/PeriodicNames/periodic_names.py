'''
Ezra Brooker
2021

Goofing around with string manipulations, list comprehensions, and whatnot.

This actually comes from a problem I was posed where one takes a name and
attempts, using the symbols of the periodic table of elements, to construct
as many combinations of that name in a sorted order.

I originally bombed it when trying to answer this question and was told an
initial way I was going to do this was too complicated and that I should 
solve it with a recursive function. 

This script is mostly to show that the non-recursive way is not actually 
complicated at all and reveals some nice structure to how the names are
constructed in a tree-like fashion.

'''
import sys,os,time
import openpyxl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from IPython import embed

ELEMENTS_STRING = "H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti \
                   V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo \
                   Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm \
                   Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb \
                   Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No \
                   Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og"

ELEMENTS_SET = set(ELEMENTS_STRING.split())


def convert_to_datalist(file,dfs):
        outfile = file.split('/')
        outfile = outfile[-1].split('.')
        outfile = 'data/'+outfile[0]+'.dat'
        with open(outfile, 'w') as fout:
            for name in dfs['name']:
                fout.write(f"{name}\n")


def recursive_string(name,partial,i,nameset,elems):

    # Try to advance by a 1-string
    if i < len(name) and name[i] in elems.keys():
        elem = elems[name[i]]

        # If builds more of the name, call this function again for the next substring
        if partial.lower()+elem.lower() in name:
            nameset = recursive_string(name, partial+elem, i+1, nameset, elems)

    # Try to advance by a 2-string
    if i < len(name)-1 and name[i:i+2] in elems.keys():
        elem = elems[name[i:i+2]]

        # If builds more of the name, call this function again for the next substring
        if partial.lower()+elem.lower() in name:
            nameset = recursive_string(name, partial+elem, i+2, nameset, elems)

    # Will only work if we hit the end of a recursion chain, add new name if == real name
    if partial.lower() == name:
        nameset.add(partial)

    return nameset

def periodic_names_recursive(name):
    ''' Periodic Names Builder using RECURSION '''
    tstart = time.perf_counter()
    name = name.lower()

    # Fine symbols that fit in name for compactness
    elems = {elem.lower():elem for elem in ELEMENTS_SET if elem.lower() in name} 
    
    # Recursively build names if possible
    nameset = recursive_string(name,"",0,set(),elems)
    nameset = list(nameset)
    nameset.sort()
    t = time.perf_counter() - tstart
    return len(nameset), t


def periodic_names(name):
    ''' Periodic Names Builder using For-loops and List Comprehensions '''
    tstart = time.perf_counter()
    name = name.lower()
    # Get all possible symbols that appear in NAME
    elems = {elem.lower():elem for elem in ELEMENTS_SET if elem.lower() in name}
    ekeys = list(elems.keys()) # Handy list for IF blocks

    # Get length of name and initialize a list with an empty string starter
    n     = len(name)
    names = [""]
    for i in range(n):

        # Check for 1-character symbols at position name[i]
        s1 = name[i]
        if s1 in ekeys:
            elem = elems[s1]
            # Any subnames plus the 1-character string in the provided name? Append to list
            [names.append(c+elem) for c in names if c.lower()+s1 in name]

        # Check for 2-character symbols at position name[i:i+2] except for last iteration
        if (i < n-1):
            s2 = name[i:i+2]
            if s2 in ekeys:
                elem = elems[s2]
                # Any subnames plus the 2-character string in the provided name? Append to list
                [names.append(c+elem) for c in names if c.lower()+s2 in name]

        # Clear out dead pathways; this preserves any subnames with a new 2-character addition
        # as they can grow at least once every two iterations before becoming a dead path.
        # Temporarily turning into a set also clears out duplicates, reducing future operations.
        names = set(names)
        names = list([c for c in names if len(c) > i])

        # If no pathways survive, exit
        # print(count,names)
        if len(names) == 0:
            t = time.perf_counter() - tstart
            return 0, t


    # Sort ASCII-betically
    names.sort()
    t = time.perf_counter() - tstart
    return len(names), t


def test_lists(func,fdict):

    hline= " -----------|-------------|---------------|---------------------------------------"
    print(f"\n{hline}\n{hline}")
    print(f"   CPU Time | Names Found | Average Found |          Source of Names              ")
    print(f"{hline}\n{hline}")

    for key,file in fdict.items():
        tmfn = []
        nmfn = []

        if ".dat" in file:
            with open(file, "r") as f:
                for line in f:
                    name = line.strip()
                    nt,tt = func(name)
                    nmfn.append(nt)
                    tmfn.append(tt)

            tt = sum(tmfn)    # Total time to process list
            nn = sum(nmfn)    # Total number of periodic names found
            nl = len(tmfn)    # Number of names processed
            mn = nn/float(nl) # PeriodicNames/ProcessedNames

            string = f"   {tt:1.2e} | {nn:11d} | {mn:13.4f} | {nl:8d} {key}"
            print(f"{string}")
            print(f"{hline}")
 
        # Read in files that needed to be converted first
        elif ".txt" in file:
            dfs = {}
            with open(file, "r") as f:
                header = f.readline()
                for header in f.readline():
                    h = header.strip().split()
                    dfs[h] = []
                for line in f.readlines():
                    l = line.strip().split()
                    dfs['name'].append(l[0])

            convert_to_datalist(file,dfs)

        elif ".csv" in file:
            tmp = pd.read_csv(file, sep=r'\s{1,}', engine='python')
            dfs = {'name': [str(s) for s in tmp['name'].values]}
            convert_to_datalist(file,dfs)
            
        elif ".xlsx" in file:
            tmp = pd.read_excel(file)
            dfs = {'name': [str(s) for s in tmp['name'].values]}
            convert_to_datalist(file,dfs)

        else:
            pass

    print(f"{hline}\n")


def test_single(func,name):
    nt, tt = func(name)
    string = f"   {tt:1.2e} | {nt:11d} | {nt:13.4f} | {name}"
    print(f"{string}")
    print(f"{hline}")
 
    

if __name__ == '__main__':

    # hline= " -----------|-------------|---------------|---------------------------------------"
    # print(f"\n{hline}\n{hline}")
    # print(f"   CPU Time | Names Found | Average Found |          Source of Names              ")
    # print(f"{hline}\n{hline}")
    # test_single(periodic_names,"Cococococococococococococococo")
    # test_single(periodic_names_recursive,"Cococococococococococococococo")
    # print(f"{hline}\n")


    files = [
        "../../data/Independent_Country_Names.dat",
        "../../data/Forenames_Male_1990_US_Census.dat",
        "../../data/Forenames_Female_1990_US_Census.dat",
        "../../data/Surnames_1990_US_Census.dat",
        "../../data/Surnames_2000_US_Census.dat",
        "../../data/Surnames_2010_US_Census.dat",
        "../../data/Coco.dat",
    ]

    fkeys = [
        "Independent Country Names",
        "US Census 1990 Forenames (male)",
        "US Census 1990 Forenames (female)",
        "US Census 1990 Surnames",
        "US Census 2000 Surnames",
        "US Census 2010 Surnames",
        "Coco  Names"
    ]


    fdict = dict(zip(fkeys,files))

    print("\nPeriodic Names Builder w/ For-Loop and List Comprehensions")
    test_lists(periodic_names,fdict)
    print("\nPeriodic Names Builder w/ Recursive If-statements")
    test(periodic_names_recursive,fdict)
    print("\n")


