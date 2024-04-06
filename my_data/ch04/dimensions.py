# Basic looping
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)


# Doing more with looping
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician.title() + ", that was a great trick!")


magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")


# Doing something after a for loop
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wai to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")
