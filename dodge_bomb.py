import pygame as pg
import sys
import random

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02-20230425/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02-20230425/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    bb_img = pg.Surface((20, 20))  # 黒い四角を作成
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)  # 半径10、赤色の円
    bb_img.set_colorkey((0, 0, 0))  # 黒の背景を透過
    x, y = random.randint(0,1600), random.randint(0, 900)
    vx, vy = +1, +1
    screen.blit(bb_img, [x, y])
    bb_rct = bb_img.get_rect()
    bb_rct.center = (x, y)

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        bb_rct.move_ip(vx, vy)
        screen.blit(bb_img, bb_rct)
        



        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()