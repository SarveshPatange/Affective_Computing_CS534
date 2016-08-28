import os

root_path = "C:\\USC\\CS-534 Affective Computing\\PokerDataFACET\\PokerDataFACET"

dirs = os.listdir(root_path)
game = "java_gamedata.txt"
frame = "java_framedata.txt"
for folders in dirs:
    folder_path = os.path.join(root_path,folders)
    if game in os.listdir(folder_path) and frame in os.listdir(folder_path):
        file_path = os.path.join(folder_path,"Combined_game_frame_data.txt")
        out_file = open( file_path, 'w')
        with open(os.path.join(folder_path,game), 'r') as g:
            for line in g:
                print("game data")
                out_file.write(line)
            out_file.write(",")

        with open(os.path.join(folder_path,frame), 'r') as f:
            for line in f:
                out_file.write(line)
        out_file.close()
