HEIGHT = 500
WIDTH = 500

bg = 'blue_bg'

femAdv_obj = Actor('character_female_adventurer_idle',(100,100))
maleAdv_obj = Actor('character_male_adventurer_idle',(200,200))
malePer_obj = Actor('character_male_person_idle',(300,300))

def draw():
    screen.blit(bg,(0,0))

    femAdv_obj.draw()
    maleAdv_obj.draw()
    malePer_obj.draw()

def update():
    femAdv_obj.y -= 2
    maleAdv_obj.x += 2
    malePer_obj.x -= 2
    repeat_fun()

def repeat_fun():
    if malePer_obj.right < 0:
        malePer_obj.left = WIDTH
    if femAdv_obj.y < 0:
        femAdv_obj.y = HEIGHT
    if maleAdv_obj.left > WIDTH:
        maleAdv_obj.right = 0
def on_mouse_down(pos,button):
    if malePer_obj.collidepoint(pos) and button == mouse.LEFT:
        malePer_obj.image = 'character_zombie_idle'
        clock.schedule_unique(reset_malePer,2.0)

    if maleAdv_obj.collidepoint(pos) and button == mouse.LEFT:
        maleAdv_obj.image = 'character_zombie_idle'
        clock.schedule_unique(reset_maleAdv,2.0)

    if femAdv_obj.collidepoint(pos) and button == mouse.LEFT:
        femAdv_obj.image = 'character_zombie_idle'
        clock.schedule_unique(reset_femAdv,2.0)

def reset_malePer():
    malePer_obj.image = 'character_male_person_idle'
def reset_maleAdv():
    maleAdv_obj.image = 'character_male_adventurer_idle'
def reset_femAdv():
    femAdv_obj.image = 'character_female_adventurer_idle'
