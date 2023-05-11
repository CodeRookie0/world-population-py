import numpy as np
import matplotlib.pyplot as plt

continentName = ["Asia", "Africa", "SouthAmerica", "NorthAmerica", "Europe", "Oceania"]
DataBase = []
columnNames = []
continentPopulation1970To2022 = np.zeros((6, 8))
changeInPopulation1970To2022 = [0] * 6
changeInPopulation2020To2022 = [0] * 6
percentPopulationShareWorld = [0] * 6
worldPopulation2022=0

def ReadFile(fileNameToRead):
    try:
        if not fileNameToRead.endswith('.txt'):
            raise ValueError("Invalid file type. The file type must be .txt.")
        
        fileReading = open(fileNameToRead,"r")
        column_names = fileReading.readline().strip().split(';')
        for line in fileReading:
            data = line.strip().split(';')
            for i in range(5, 16):
                data[i] = data[i].replace('.', ',')
            DataBase.append(data)
        return DataBase
    except ValueError as e:
        print("\nError:", e)
    except FileNotFoundError:
        print("\nError: The specified file to read does not exist!")
    except Exception as ex:
        print("\nError:", ex)

def ContinentPopulation1970To2022():
    try:
        for row in DataBase:
            for i in range(len(continentName)):
                if row[4] == continentName[i]:
                    continentPopulation1970To2022[i][0] += float(row[12])
                    continentPopulation1970To2022[i][1] += float(row[11])
                    continentPopulation1970To2022[i][2] += float(row[10])
                    continentPopulation1970To2022[i][3] += float(row[9])
                    continentPopulation1970To2022[i][4] += float(row[8])
                    continentPopulation1970To2022[i][5] += float(row[7])
                    continentPopulation1970To2022[i][6] += float(row[6])
                    continentPopulation1970To2022[i][7] += float(row[5])
                    break
        return continentPopulation1970To2022
    except ValueError:
        print("\nError: The population number cannot be converted to float!")
    except IndexError:
        print("\nError: Index out of range!")
    except Exception as ex:
        print("\nError: "+str(ex))

def PercentChangePopulation1970To2022():
    try:
        continent_population_1970 = [0] * 6
        continent_population_2022 = [0] * 6
        for i in range(len(continentName)):
            continent_population_1970[i] += continentPopulation1970To2022[i][0]
            continent_population_2022[i] += continentPopulation1970To2022[i][7]
        # Calculate percentage change in population 1970/2022
        for i in range(len(continent_population_1970)):
            changeInPopulation1970To2022[i] = ((continent_population_2022[i] * 100.0) / continent_population_1970[i]) - 100.0
        return changeInPopulation1970To2022
    except IndexError:
        print("\nError: The index to an array element is out of range!")
    except ZeroDivisionError:
        print("\nError: Trying to divide by zero!")
    except Exception as ex:
        print("\nError: " + str(ex))

def PercentChangePopulation2020To2022():
    try:
        continent_population_2020 = [0] * 6
        continent_population_2022 = [0] * 6
        for i in range(len(continentName)):
            continent_population_2020[i] += continentPopulation1970To2022[i][6]
            continent_population_2022[i] += continentPopulation1970To2022[i][7]
        # Calculate percentage change in population 2020/2022
        for i in range(len(continent_population_2020)):
            changeInPopulation2020To2022[i] = ((continent_population_2022[i] * 100.0) / continent_population_2020[i]) - 100.0
        return changeInPopulation2020To2022
    except IndexError:
        print("\nError: The index to an array element is out of range!")
    except ZeroDivisionError:
        print("\nError: Trying to divide by zero!")
    except Exception as ex:
        print("\nError: " + str(ex))

def PercentWorldPopulationShare2022():
    try:
        worldPopulation2022 = 0
        for i in range(len(continentName)):
            worldPopulation2022 += continentPopulation1970To2022[i][7]
        # Calculate percentage share of each continent's population in the world population
        for i in range(len(continentName)):
            percentPopulationShareWorld[i] = ((continentPopulation1970To2022[i][7] * 100.0) / worldPopulation2022)
        return percentPopulationShareWorld, worldPopulation2022
        
    except IndexError:
        print("\nError : The index to an array element is out of range!")
    except ZeroDivisionError:
        print("\nError : Trying to divide by zero!")
    except Exception as ex:
        print("\nError : ", ex)

def SaveToFile(fileNameToSave):
    try:
        if not fileNameToSave.endswith('.txt'):
            raise ValueError("Invalid file type. The file type must be .txt.")
        
        fileSaving=open(fileNameToSave,"w")
        fileSaving.write("continentName;continentPopulation1970;continentPopulation2022;changeInPopulation1970To2022(%)\n")
        for i in range(len(continentName)):
            fileSaving.write(f"{continentName[i]};{continentPopulation1970To2022[i][0]};{continentPopulation1970To2022[i][7]};{changeInPopulation1970To2022[i]}\n")
        
        fileSaving.write("\ncontinentName;continentPopulation2020;continentPopulation2022;changeInPopulation2020To2022(%)\n")
        for i in range(len(continentName)):
            fileSaving.write(f"{continentName[i]};{continentPopulation1970To2022[i][6]};{continentPopulation1970To2022[i][7]};{changeInPopulation2020To2022[i]}\n")
        
        fileSaving.write(f"worldPopulation2022 : {worldPopulation2022}\n")
        fileSaving.write("\ncontinentName;continentPopulation2022;percentPopulationShareWorld(%)\n")
        for i in range(len(continentName)):
            fileSaving.write(f"{continentName[i]};{continentPopulation1970To2022[i][6]};{percentPopulationShareWorld[i]}\n")
        
        fileSaving.write("\ncontinentName;continentPop1970;pop1980;pop1990;pop2000;pop2010;pop2015;pop2020;pop2022\n")
        for i in range(len(continentName)):
            line = f"{continentName[i]};"
            for j in range(len(continentPopulation1970To2022[i])):
                line += f"{continentPopulation1970To2022[i][j]};"
            fileSaving.write(line + '\n')   
    except ValueError as e:
        print("\nError:", e)
    except PermissionError:
        print("\nError: Does not have permission to write to the file!")
    except IOError as e:
        print("\nError:", e)
    except Exception as ex:
        print("\nError:", ex)

def PlotChangePopulation1970To2022():
    contynenty=continentName
    pop1970=[continentPopulation1970To2022[i][0] for i in range(len(continentPopulation1970To2022))]
    pop2022=[continentPopulation1970To2022[i][7] for i in range(len(continentPopulation1970To2022))]
    x = np.arange(len(contynenty))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, pop1970, width, label='Population 1970')
    rects2 = ax.bar(x + width/2, pop2022, width, label='Population 2022')

    ax.set_xticks(x)
    ax.set_xticklabels(contynenty)
    ax.legend()

    fig.set_figwidth(10)
    plt.savefig('Pop1970To2022.jpg')
    plt.show()

def PlotChangePopulation2020To2022():
    contynenty=continentName
    pop2020=[continentPopulation1970To2022[i][6] for i in range(len(continentPopulation1970To2022))]
    pop2022=[continentPopulation1970To2022[i][7] for i in range(len(continentPopulation1970To2022))]
    x = np.arange(len(contynenty))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, pop2020, width, label='Population 2020')
    rects2 = ax.bar(x + width/2, pop2022, width, label='Population 2022')

    ax.set_xticks(x)
    ax.set_xticklabels(contynenty)
    ax.legend()


    fig.set_figwidth(10)
    plt.savefig('Pop2020To2022.jpg')
    plt.show()

def PlotPercentPopulationShareWorld2022():
    contynenty=continentName
    pop_share=percentPopulationShareWorld
    plt.pie(pop_share,labels=contynenty,autopct='%1.1f%%')

    plt.savefig('PopWorldShare.jpg')
    plt.show()

def ShowPlots():
    PlotChangePopulation1970To2022()
    PlotChangePopulation2020To2022()
    PlotPercentPopulationShareWorld2022()


def main():
    print("Enter the name of the file with the type of extension (e.g.txt) to read the data")
    file_name_read = input()
    print("\nEnter a file name with the type of extension (e.g.txt) for saving results.")
    file_name_saving = input()

    ReadFile(file_name_read)
    ContinentPopulation1970To2022()
    PercentChangePopulation1970To2022()
    PercentChangePopulation2020To2022()
    PercentWorldPopulationShare2022()
    SaveToFile(file_name_saving)

    ShowPlots()

if __name__ == "__main__":
    main()