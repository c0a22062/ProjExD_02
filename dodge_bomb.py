import pygame as pg
import sys
import random


delta = {
        pg.K_UP: (0, -1),
        pg.K_DOWN: (0, 1),
        pg.K_RIGHT: (1, 0),
        pg.K_LEFT: (-1, 0)
        }


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02-20230425/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02-20230425/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = (900, 400)


    bb_img = pg.Surface((20, 20))  # 黒い四角を作成
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)  # 半径10、赤色の円
    bb_img.set_colorkey((0, 0, 0))  # 黒の背景を透過
    x, y = random.randint(0,1600), random.randint(0, 900)  # ランダムなｘ、ｙを設定
    vx, vy = +1, +1  # x,y移動値
    screen.blit(bb_img, [x, y])  # 最初の位置の表示
    bb_rct = bb_img.get_rect()  # moveを使うためにrect作成
    bb_rct.center = (x, y)  # centerにランダムなｘ、ｙを設定

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1

        key_lst = pg.key.get_pressed()
        for k,mv in delta.items():
            if key_lst[k]:
                kk_rct.move_ip(mv)


        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)  # 練習３
        bb_rct.move_ip(vx, vy)
        screen.blit(bb_img, bb_rct)
        



        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()