import turtle as tur
import colorsys as cs

# Daftar warna ungu dan pink dalam format HSV
purple_pink_colors = [(0.8, 1, 1), (0.85, 1, 1), (0.9, 1, 1), (0.9, 0.9, 1), (0.95, 1, 1)]

tur.setup(800, 800)
tur.speed(0)
tur.width(2)
tur.bgcolor("black")

color_index = 0  # Indeks untuk mengambil warna dari daftar

for j in range(25):
    for i in range(15):
        hue, saturation, value = purple_pink_colors[color_index]
        tur.color(cs.hsv_to_rgb(hue, saturation, value))
        tur.right(90)
        tur.circle(200 - j * 4, 90)
        tur.left(90)
        tur.circle(200 - j * 4, 90)
        tur.right(180)
        tur.circle(50, 24)
        
        # Pindah ke warna berikutnya dalam daftar
        color_index = (color_index + 1) % len(purple_pink_colors)

tur.hideturtle()
tur.done()
