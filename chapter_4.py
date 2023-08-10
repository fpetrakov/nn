# knob_weight = 0.5
# input = 0.5
# goal_pred = 0.8

# pred = input * knob_weight

# error = (pred - goal_pred) ** 2

# print(error)


weight = 0.1
lr = 0.01


def neural_network(input, weight):
    prediction = input * weight
    return prediction


number_of_toes = [8.5]
win_or_lose_binary = [1]

input = number_of_toes[0]
true = win_or_lose_binary[0]

pred = neural_network(input, weight)

error = (pred - true) ** 2
print(error)


p_up = neural_network(input, weight + lr)
e_up = (p_up - true) ** 2
print(e_up)


p_down = neural_network(input, weight - lr)
e_down = (p_down - true) ** 2
print(e_down)

if error > e_down or error > e_up:
    if e_down < e_up:
        weight -= lr

    if e_down > e_up:
        weight += lr
