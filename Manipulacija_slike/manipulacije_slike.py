from PIL import Image


def apply_blur(img):
    width,height=img.size
    pix = img.load()

    kopija_slike = {}
    listaxy=[-2, -1, 0, 1, 2]


    for x in range(0, width):
        for y in range(0, height):
            kopija_slike[x, y] = pix[x, y]
    
    for x in   range(2, width -2):
        for y in range(2, height -2,):
            prosjek_r=0
            prosjek_b=0
            prosjek_g=0
            for r in listaxy:
                for z in listaxy:
                    prosjek_r=prosjek_r+kopija_slike[x+r,y+z][0]
                    prosjek_g=prosjek_g+kopija_slike[x+r,y+z][1]
                    prosjek_b=prosjek_b+kopija_slike[x+r,y+z][2]
            prosjek_r=int(prosjek_r/25)
            prosjek_g=int(prosjek_g/25)
            prosjek_b=int(prosjek_b/25)
            pix[x, y] = (prosjek_r,prosjek_g,prosjek_b)     


def apply_blur2(slika):
    apply_kernel_convolution_filter(slika, [[1, 1, 1],[1, 1, 1],[1, 1, 1]], 9)
def edge_detect3(slika):
    apply_kernel_convolution_filter(slika, [[1, 1, -1],[1, -4, 1],[-1, 1, 1]], 9)
def apply_sharpner(slika):
    apply_kernel_convolution_filter(slika, [[0, -1, 0],[-1, 5, -1],[0, -1, 0]], 1)

def apply_edge_detection1(slika):
    apply_kernel_convolution_filter(slika, [[1, 0, -1],[0,0,0],[-1, 0, 1]], 1)

def apply_kernel_convolution_filter(img, kernel, coeff):

    width,height=img.size
    pix = img.load()

    kopija_slike = {}
    listaxy=[-2, -1, 0, 1, 2]


    for x in range(0, width):
        for y in range(0, height):
            kopija_slike[x, y] = pix[x, y]

    listaxy=[-1,0,1,]
    for x in range(1 , width-1):
        for y in range(1 , height-1):
            prosjek_r=0
            prosjek_b=0
            prosjek_g=0
            for kernel_row in listaxy:
                for kernel_col in listaxy:
                    prosjek_r=prosjek_r+ kopija_slike[x+kernel_row,y+kernel_col][0]*kernel[kernel_row+1][kernel_col+1]
                    prosjek_g=prosjek_g+ kopija_slike[x+kernel_row,y+kernel_col][1]*kernel[kernel_row+1][kernel_col+1]
                    prosjek_b=prosjek_b+ kopija_slike[x+kernel_row,y+kernel_col][2]*kernel[kernel_row+1][kernel_col+1]

            prosjek_r=int(prosjek_r/coeff)
            prosjek_g=int(prosjek_g/coeff)
            prosjek_b=int(prosjek_b/coeff)
            pix[x, y] = (prosjek_r,prosjek_g,prosjek_b)

                    

    pass

def edge_detection(img):

    width,height=img.size
    pix = img.load()
    kopija_slike = {}
    listaxy=[ -1, 0, 1]

    for x in range(0, width):
        for y in range(0, height):
            kopija_slike[x, y] = pix[x, y]
    
    for x in   range(1, width -1):
        for y in range(1, height -1):

            current_sum = [0, 0, 0]
            coeff = None

            for red in listaxy:
                for stupac in listaxy:
                    if red == 0 and stupac == 0:
                        coeff = 8
                    else:
                        coeff = -1
                    
                    current_sum[0] = current_sum[0] + coeff * kopija_slike[x + red, y + stupac][0]
                    current_sum[1] = current_sum[1] + coeff * kopija_slike[x + red, y + stupac][1]
                    current_sum[2] = current_sum[2] + coeff * kopija_slike[x + red, y + stupac][2]

            pix[x, y] = ( current_sum[0], current_sum[1], current_sum[2] )




def apply_sepia_filter(img):
    width, height = img.size
    pix = img.load()

    for x in range(0, width):
        for y in range(0, height):
            R, G, B = pix[x, y]
            
            tr = round(0.393*R + 0.769*G + 0.189*B)
            tg = round(0.349*R + 0.686*G + 0.168*B)
            tb = round(0.272*R + 0.534*G + 0.131*B)

            tr = min(255, tr)
            tg = min(255, tg)
            tb = min(255, tb)

            pix[x, y] = (tr, tg, tb)


def main():
    """ Ovo je glavni program """
    image_path = "E:\Projekti\Image-manipulation\sample.jpg"#Ovaj se dio mjenja ovisno o lokaciji slike
    im = Image.open(image_path)
    #im.show()#metoda
    im.show()
    edge_detect3(im)
    im.show()
    pass

if __name__ == "__main__":
    main()#funkcija