import os
import math

class Data:    
    def ListFilesInDirectory(self, dirpath):
        files = os.listdir(dirpath)
        print(files)
        return files
        
    def CalculatePlayerOneWinRate(self, files, filepath):
        w = 0
        for f in files:
            file = open(filepath + f, 'r')
            lines = file.readlines()
            lastline = lines[len(lines)-1]
            file.close()
            if(lastline == "victor is player: 1" or lastline == "victor is player:1"): w += 1
            else: w += 0
        return w

        

    def CalculatePlayerTwoWinRate(self, files, filepath):
        w = 0
        for f in files:
            file = open(filepath + f, 'r')
            lines = file.readlines()
            lastline = lines[len(lines)-1]
            file.close()
            if(lastline == "victor is player: 2" or lastline == "victor is player:2"): w += 1
            else: w += 0
        return w
        

    def CalculateDrawRate(self, files, filepath):
        w = 0
        for f in files:
            file = open(filepath + f, 'r')
            lines = file.readlines()
            lastline = lines[len(lines)-1]
            file.close()
            if(lastline ==  "draw"): w += 1
            else: w += 0
        return w
    
    def PrintLastLine(self, files, filepath):
        for f in files:
            file = open(filepath + f, 'r')
            lines = file.readlines()
            file.close()
            lastline = lines[len(lines)-1]
            print(lastline)
        

def _print(directory, filename, writemode, text, newline):
    with open(directory+filename, writemode) as file:
        if(newline):
            file.write('\n')
        file.write(text)

if __name__ == "__main__":
    global filepath 
    filepath = "D:/Robert/OneDrive/Documents/University of Essex/CE888/CE888-Assignments/Assignment Two/game_data/"
    files = Data.ListFilesInDirectory(None, filepath)
    
    _1 = 0
    _2 = 0
    _3 = 0
    
    _1 = Data.CalculatePlayerOneWinRate(None, files, filepath)
    _2 = Data.CalculatePlayerTwoWinRate(None, files, filepath)
    _3 = Data.CalculateDrawRate(None, files, filepath)

    winrate = round((100/len(files) * _1))     
    print("Player one won "+ str(winrate) + "%")
    _print(filepath, "results.dat", "a", "Player one won "+ str(winrate) + "%", False)
    winrate = round((100/len(files) * _2))     
    print("Player two won "+ str(winrate) + "%")
    _print(filepath, "results.dat", "a", "Player two won "+ str(winrate) + "%", True)
    winrate = round((100/len(files) * _3))  
    print("draw "+ str(winrate) + "%")
    _print(filepath, "results.dat", "a", "Draw "+ str(winrate) + "%", True)
    _print(filepath, "results.dat", "a", "Total games played: "+ str(len(files)), True)