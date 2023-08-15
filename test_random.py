import random
dice_dict = {
    'one':0,
    'two':0,
    'three':0,
    'four':0,
    'five':0,
    'six':0
}
counter = 0
while counter<1_000_000:
    dice = random.randint(1,6)
    if dice == 1:
        dice_dict['one'] = dice_dict['one']+1
    elif dice == 2:
        dice_dict['two'] = dice_dict['two']+1
    elif dice == 3:
        dice_dict['three'] = dice_dict['three']+1
    elif dice == 4:
        dice_dict['four'] = dice_dict['four']+1
    elif dice == 5:
        dice_dict['five'] = dice_dict['five']+1
    else:
        dice_dict['six'] = dice_dict['six']+1 
    counter += 1

print(dice_dict)