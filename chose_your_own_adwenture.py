def lose_point(points):
    points -= 1
    if points <= 0:
        print("\nYou grew weaker with every wrong choice. Dehydration claims you as you collapse to the ground. You forgot to drink water. This is the end of your story.")
        quit()
    return points

points = 3  # Player starts with 3 points
name = input("Type your name: ")
print(f"Welcome, {name}, to this adventure!")

print(f"\n{name}, you wake up covered in dirt and mud. Your head throbs, and your body aches. You look around. The place is unfamiliar, surrounded by twisted trees and a thick, unnatural fog. Suddenly, a strange noise comes from the south...")

while True:
    answer = input("Do you dare to check it out? (yes/no): ").lower()
    if answer == "yes":
        print("\nWith every step, the noise grows louder. Your heart races. You push through the undergrowth and suddenly see it—a beast, towering and grotesque, covered in blood. Its glowing eyes lock onto you.")
        while True:
            answer = input("The beast lets out a deafening roar and leaps into the sky! Your life hangs in the balance... Do you follow the beast or run away? (follow/run): ").lower()

            if answer == "follow":
                print("\nDriven by a strange compulsion, you follow the beast. But it was a trap! The creature swoops down and bites your head clean off. This is the end of your story, brave soul.")
                quit()

            elif answer == "run":
                print("\nYou manage to escape, but your heart pounds and your ankle twists painfully. You limp slowly through the forest, each step agonizing.")
                while True:
                    answer = input("Will you rest and risk being caught, or press on despite your injury? (rest/press on): ").lower()

                    if answer == "rest":
                        print("\nYou decide to rest, leaning against a tree. As you close your eyes for just a moment... the beast finds you. Its claws tear into you, and darkness falls. This is the end of your story.")
                        quit()

                    elif answer == "press on":
                        print("\nDespite the pain, you keep moving. But suddenly, you trip on a root and tumble down a steep hill. Rolling uncontrollably, you plunge into a raging river. The current pulls you under, and you drown. This is the end of your story.")
                        quit()

                    else:
                        print("Not a valid option. You lose 1 point.")
                        points = lose_point(points)

            else:
                print("Not a valid option. You lose 1 point.")
                points = lose_point(points)

    elif answer == "no":
        print("\nYou decide against investigating the noise. The world around you is vast and filled with mystery. You must choose your own path.")
        while True:
            answer = input("Which direction will you go? NORTH, SOUTH, EAST, or WEST? ").lower()

            if answer == "north":
                print("\nYou venture north, where the air grows colder, and the sky darkens. A shadow looms in the distance... it's a crumbling castle. You approach the gates, but they swing open on their own. Inside, a ghostly figure watches your every move...")
                # Continue the story for the NORTH path
                quit()

            elif answer == "south":
                print("\nHeading south, you find yourself in a desolate wasteland. The ground cracks beneath your feet. Suddenly, a deep rumble shakes the earth. A monstrous worm bursts from the ground and begins chasing you!")
                # Continue the story for the SOUTH path
                quit()

            elif answer == "east":
                print("\nWalking east, you find a forgotten ruin. The walls are covered in ancient runes, and you feel a strange energy in the air. You see a glowing amulet on a pedestal. Do you dare take it?")
                # Continue the story for the EAST path
                quit()

            elif answer == "west":
                print("\nYou travel west, where the forest thickens. The trees seem to watch your every move. A soft whisper reaches your ears, but you can't tell if it's the wind or something else. Suddenly, you hear footsteps behind you...")
                # Continue the story for the WEST path
                quit()

            else:
                print("Not a valid option. You lose 1 point.")
                points = lose_point(points)

    else:
        print("Not a valid option. You lose 1 point.")
        points = lose_point(points)
