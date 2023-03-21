#SCHEMAT LINKÓW DO WKLEJENIA
# C: HOST PORT USER PASSWORD

def getName():
    print("Wpisz nazwę czytnika:\n")
    return input()

def getLinks():
    text = []
    print("\n\nWklej linki do czytników:\n")
    while True:
        try:

            line = input()
            if line == "" or len(line) <= 1:
                break

            line.split(" ")
            text.append(line)

        except:
            break

    return text

def createReader(name, links):

    readers = ""
    for index, i in enumerate(links):

        link = i.split(" ")
        reader = f"%40s\n" % ("[Reader]")
        reader += f"%29s = %s\n" % ("label", name+"_"+str(index+1))
        reader += f"%29s = %s\n" % ("protocol", "cccam_mcs")
        reader += f"%29s = %s , %s\n" % ("device", link[1], link[2])
        reader += f"%29s = %s\n" % ("user", link[3])
        reader += f"%29s = %s\n" % ("password", link[4])
        reader += f"%29s = %i\n" % ("inactivitytimeout", 30)
        reader += f"%29s = %i\n" % ("fallback", 1)
        reader += f"%29s = %i\n" % ("group", 6)
        reader += f"%29s = %s\n" % ("cccversion", "2.0.11")
        reader += f"%29s = %i\n" % ("ccckeepalive", 1)
        reader += f"\n\n"

        readers += reader

    return readers


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    outputText = createReader(getName(), getLinks())

    print("\n\nCzytniki gotowe do wklejenia:\n\n")
    print(outputText)
    print("\n\nCzytniki zostały zapisane również w pliku links_output.txt")

    f = open("links_output.txt", "w")
    f.write(outputText)
    f.close()


