inp_filename, operation, out_filename = input().split()


# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
def read_imagefile(f):
    firstline = f.readline().rstrip()
    tmp = firstline.split()
    img_matrix = []
    lines = []
    type_ = tmp[0]
    width = int(tmp[1])
    height = int(tmp[2])
    res = int(tmp[3])

    for i in range(int(height)):
        fp = f.readline().rstrip()
        lines = fp.split()
        img_matrix.append(lines)

    return img_matrix




def write_imagefile(f, img_matrix):
    f.write(f'P2 {len(img_matrix[0])} {len(img_matrix)} {255}\n')
    for r in range(len(img_matrix)):
        for c in range(len(img_matrix[0])-1):
            f.write(str(img_matrix[r][c]) + ' ')
        f.write(str(img_matrix[r][len(img_matrix[0])-1]))
        f.write('\n')

def misalign(img_matrix):

    for i in range(len(img_matrix[0])):
        if i % 2 == 1:
            toptobottomlist = []
            for a in range(len(img_matrix)):
                toptobottomlist.append(img_matrix[a][i])
            toptobottomlist.reverse()
            for j in range(len(toptobottomlist)):
                img_matrix[j][i] = toptobottomlist[j]
    return img_matrix

def sort_columns(img_matrix):
    for i in range(len(img_matrix[0])):

        toptobottom = []
        for a in range(len(img_matrix)):
            toptobottom.append(int(img_matrix[a][i]))
        toptobottom.sort()
        for j in range(len(img_matrix)):
            img_matrix[j][i] = toptobottom[j]
    return img_matrix

def sort_rows_border(img_matrix):

    height = len(img_matrix)
    width = len(img_matrix[0])
    for i in range(height):
        for a in range(width):
            img_matrix[i][a]  = int(img_matrix[i][a])
    for i in range(height):
        start = 0
        end = 0
        partlist = []
        for el in range(width):
            if el != width-1 and img_matrix[i][el] != 0 :
                end += 1
            elif img_matrix[i][el] == 0 and img_matrix[i][el-1] != 0 :
                sortedlist = sorted(img_matrix[i][start:end])
                for b in sortedlist:
                    partlist.append(b)


                partlist.append(img_matrix[i][el])
                end += 1
                start = end


            elif img_matrix[i][el] == 0 and img_matrix[i][el-1] == 0:
                partlist.append(img_matrix[i][el])
                end += 1
                start = end
            elif el == width-1 and img_matrix[i][el] != 0 :
                end += 1
                lastsorted = sorted(img_matrix[i][start:end])
                lastsorted.sort()
                for b in lastsorted:
                    partlist.append(b)
        img_matrix[i] = partlist
    for i in range(height):
        for a in range(width):
            img_matrix[i][a]  = str(img_matrix[i][a])


    return img_matrix

def convolution(img_matrix, kernel):
    height = len(img_matrix)
    width = len(img_matrix[0])
    convlist = []
    stlist = []
    lastlist = []
    for i in range(width+2):
        stlist.append(0)
    convlist.append(stlist)
    for a in range(height):
        convlist.append([0] +img_matrix[a] + [0])
    for i in range(width+2):
        lastlist.append(0)
    convlist.append(lastlist)

    for i in range(height):
        for a in range(width):
            result =(int(convlist[i][a]) * int(kernel[0][0]) ) + (int(convlist[i][a+1]) * int(kernel[0][1]) ) +(int(convlist[i][a+2]) * int(kernel[0][2]) ) +(int(convlist[i+1][a]) * int(kernel[1][0]) ) +(int(convlist[i+1][a+1]) * int(kernel[1][1]) ) +(int(convlist[i+1][a+2]) * int(kernel[1][2]) ) +(int(convlist[i+2][a]) * int(kernel[2][0]) ) + (int(convlist[i+2][a+1]) * int(kernel[2][1]) ) +(int(convlist[i+2][a+2]) * int(kernel[2][2]) )
            if result > 255:
                result = 255
            if result < 0:
                result = 0
            img_matrix[i][a] = result

    return img_matrix


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
f = open(inp_filename, "r")
img_matrix = read_imagefile(f)
f.close()

if operation == "misalign":
    img_matrix = misalign(img_matrix)

elif operation == "sort_columns":
    img_matrix = sort_columns(img_matrix)

elif operation == "sort_rows_border":
    img_matrix = sort_rows_border(img_matrix)

elif operation == "highpass":
    kernel = [
        [-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]
    ]
    img_matrix = convolution(img_matrix, kernel)

f = open(out_filename, "w")
write_imagefile(f, img_matrix)
f.close()
