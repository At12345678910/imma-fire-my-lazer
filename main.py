def on_on_overlap(sprite, otherSprite):
    info.change_score_by(755775)
    EAAAAAAAAAAAD.set_position(randint(2, 1), randint(2, 1))
    info.start_countdown(10)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

EAAAAAAAAAAAD: Sprite = None
scene.set_background_color(6)
bwaaaw = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . 1 1 1 . 1 1 1 . . . . . . 
            . . . 1 f 1 . 1 f 1 . . . . . . 
            . . . 1 1 1 . 1 1 1 . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . 2 2 2 2 2 2 2 . . . . . . 
            . . . 2 1 1 1 1 1 2 . . . . . . 
            . . . 2 f f f f f 2 . . . . . . 
            . . . 2 f f f f f 2 . . . . . . 
            . . . 2 f f f f f 2 . . . . . . 
            . . . 2 f f f f f 2 . . . . . . 
            . . . 2 1 1 1 1 1 2 . . . . . . 
            . . . 2 2 2 2 2 2 2 . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(bwaaaw)
EAAAAAAAAAAAD = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.food)