# Introducing lists
# 1
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Accessing elements in a list
# 2
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])

# 3
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())

# Index positions start at 0, not 1
# 4
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])

# 5
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])

# Using individual values from a list
# 6
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."

print(message)