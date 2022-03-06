import datetime

def file_lineCounter(content):
    conList = content.split("\n")
    num_counter = 1
    for line in conList:
        if line:
            num_counter += 1
    return num_counter  # Returns the number of lines [INT]


def inputEditor(numSec, nameSec):
    nameSec = nameSec.title()
    while len(numSec) < 4:
        numSec += " "
    while len(nameSec) < 15:
        nameSec += " "
    return numSec, nameSec  # Returns a modified string [STRING]


def dateToday():
    now = datetime.datetime.now()
    formatedDate = now.strftime("%d/%m/%Y %H:%M")  # dd/mm/YYYY H:M
    return formatedDate


def pathGenerate(content, numId):
    conList = content.split("\n")
    selectedLine = str(conList[numId])  # Will get the line of the selected ID
    customerId = selectedLine[0:4].strip()
    customerName = selectedLine[5:20].strip().replace(" ", "_")
    generatedPath = customerId + "." + customerName + ".txt"
    return generatedPath  # [STRING]


# ====== ====== =========

def inputEditor2(quantity, productName, totalPrice):
    while len(quantity) < 4:
        quantity += " "
    while len(productName) < 20:
        productName += " "
    while len(totalPrice) < 6:
        totalPrice += " "
    fullLine = quantity + "|" + productName + "|" + totalPrice + "|"
    return fullLine  # Returns a [STRING]


def file_TotalCalculator(fileContent):
    # To list, still need to exclude the header
    conList = fileContent.split("\n") 
    
    # Will exclude the header
    final_conList = []
    i = 2
    while i < len(conList):
        final_conList.append(conList[i])  
        i += 1
    
    # Will calculate the prices
    total = 0
    final_conList.pop()  # Exclude the blank line at the ending.
    try:
        for line in final_conList:
            subPrice = int(line[26:32].strip())
            total += subPrice
    except:
        print("\nCommand unsuccessful.")
        print("Use [VIEW] to check if the profile is already fully paid.\n")
        return ""
    else: return total

def statusAdder(content, customerId):
    conList = content.split("\n")
    conList[customerId] = str(conList[customerId]) + "fully paid!"
    conList.pop()  # Will remove the last item of the list which is /blank/
    newContent = ""
    for line in conList:
        newContent += line + "\n"
    return newContent  # [STRING]
