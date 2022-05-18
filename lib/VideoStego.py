from PIL import Image
import shutil,cv2,os
from ast import literal_eval
from threading import Thread

def frame_extract(video):
    temp_folder = 'lib/temp'
    try:
        os.mkdir(temp_folder)
    except OSError:
        remove(temp_folder)
        os.mkdir(temp_folder)

    vidcap = cv2.VideoCapture(str(video))
    count = 0

    while True:
        success, image = vidcap.read()
        if not success:
            break
        cv2.imwrite(os.path.join(temp_folder, "{:d}.png".format(count)), image)
        count += 1


def remove(path):
    """ param <path> could either be relative or absolute. """
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)
    else:
        raise ValueError("file {} is not a file or dir.".format(path))



def split2len(s, n):
    def _f(s, n):
        while s:
            yield s[:n]
            s = s[n:]
    return list(_f(s, n))

def caesar_ascii(char,mode,n):
    if mode == "enc" :
        ascii = ord(char)
        return chr((ascii + n) % 128)
    elif mode == "dec" :
        ascii = ord(char)
        return chr((ascii - n) % 128)
    

def encode_frame(frame_dir,text_to_hide):


    m = text_to_hide
    text_to_hide_open = open(text_to_hide, "rb")
    #text_to_hide = repr(text_to_hide_open.read())
    text_to_hide = text_to_hide_open.read()
    text_to_hide_open.close()
    #print(text_to_hide)


    text_to_hide_chopped =  split2len(text_to_hide,255)
  

    for text in text_to_hide_chopped:
    
        try:
            ind = len(text_to_hide_chopped)+1
            frame = Image.open(str(frame_dir) +"/" + str(ind+1) + ".png")
        except FileNotFoundError:
            print("Data file too large, provide a different video...")
            return -1
        length = len(text)
        chopped_text_index = text_to_hide_chopped.index(text)
        frame = Image.open(str(frame_dir) +"/" + str(chopped_text_index+1) + ".png")

        if frame.mode != "RGB":
            print("Source frame must be in RGB format")
            return False



        encoded = frame.copy()
        width, height = frame.size

        index = 0
        a = object
        for row in range(height):
            for col in range(width):
                r,g,b = frame.getpixel((col,row))


                if row == 0 and col == 0 and index < length:
                    asc = length
                    if text_to_hide_chopped.index(text) == 0 :
                        total_encoded_frame = len(text_to_hide_chopped)
                    else:
                        total_encoded_frame = g
                elif index <= length:
                    c = text[index -1]

                    #asc = ord(c)
                    asc = c

                    total_encoded_frame = g
                else:
                    asc = r
                    total_encoded_frame = g
                encoded.putpixel((col,row),(asc,total_encoded_frame,b))
                index += 1
        if encoded:
            encoded.save(str(frame_dir)+"/"+str(chopped_text_index+1) + ".png",compress_level=0)


def decode_frame(frame_dir, outputFile="lib/output/decrypted.txt"):
    first_frame = Image.open(str(frame_dir)+ "/" + "1.png")
    r,g,b = first_frame.getpixel((0,0))
    total_encoded_frame = g
    msg = b""
    perc = 0
    for i in range (1,total_encoded_frame+1):
        new_perc = round(i/total_encoded_frame, 1)
        if new_perc!=perc:
            perc=new_perc
            print("Processing..." + str(perc))
        frame = Image.open(str(frame_dir) + "/" + str(i) + ".png")
        width, height = frame.size
        index = 0
        for row in range(height):
            for col in range(width):
                try :
                    r,g,b = frame.getpixel((col,row))
                except ValueError:
                    r, g, b, a = frame.getpixel((col, row))
                if row == 0 and col == 0:
                    length = r
                elif index <= length:
                    # put the decrypted character into string
                    msg += r.to_bytes(1, "big")
                index +=1
               
    #msg = str(msg[1:-1])
    #print(msg)
    recovered_txt = open(outputFile, "wb")
    recovered_txt.write(msg)
    recovered_txt.close()
    

