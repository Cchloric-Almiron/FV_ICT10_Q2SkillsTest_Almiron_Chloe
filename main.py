#Skills Test Q2
from pyscript import document, display


def search_element(e):

    #Dictionary of nonmetals
    nonmetals = {"H":("Hydrogen", 1, 1.008), "He":("Helium", 2, 4.0026), "C":("Carbon", 6, 12.011), "N":("Nitrogen", 7, 14.007), "O":("Oxygen", 8, 15.999), "F":("Fluorine", 9, 18.998), "Ne":("Neon", 10, 20.180), "P":("Phosphorus", 15, 30.974), "S":("Sulfur", 16, 32.06), "Cl":("Chlorine", 17, 35.45), "Ar":("Argon", 18, 39.948), "Se":("Selenium", 34, 78.971), "Br":("Bromine", 35, 79.904), "Kr":("Krypton", 36, 83.798), "I":("Iodine", 53, 126.90), "Xe":("Xenon", 54, 131.29), "Rn":("Radon", 86, 222), "Og":("Oganesson", 118, 294)}
    
    #Get the input value from the user
    Element1 = document.getElementById("element").value

    #Input is equals to the dictionary, regardless of the capitalization

    Element0 = Element1.capitalize()
    
    #retrieve the element information from the dictionary
    element_result = nonmetals.get(Element0, ('Element not found', 0, 0))

    document.getElementById("symbol").innerText = Element0
    document.getElementById("name").innerText = element_result[0]
    document.getElementById("atomic_number").innerText = element_result[1]
    document.getElementById("atomic_mass").innerText = element_result[2]
