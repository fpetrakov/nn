# weight = 0.5
# goal_pred = 0.8
# input = 0.5

# for iteration in range(20):
#     pred = input * weight
#     error = (pred - goal_pred) ** 2
#     direction_and_amount = (pred - goal_pred) * input
#     weight = weight - direction_and_amount

#     print("Error: " + str(error) + " Prediction: " + str(pred))

# weight = 0.1

# alpha = 0.01


# def neural_network(input, weight):
#     prediction = input * weight
#     return prediction


# number_of_toes = [8.5]
# win_or_lose_binary = [1]

# input = number_of_toes[0]
# goal_pred = win_or_lose_binary[0]

# pred = neural_network(input, weight)

# error = (pred - goal_pred) ** 2

# delta = pred - goal_pred

# weight_delta = input * delta

# weight -= weight_delta * alpha

weight, goal_pred, input = (0.0, 0.8, 1.1)

for iteration in range(4):
    pred = input * weight
    error = (pred - goal_pred) ** 2
    delta = pred - goal_pred
    weight_delta = delta * input
    weight -= weight_delta

    print("Error: " + str(error) + " Prediction: " + str(pred))
    print("Delta: " + str(delta) + " Weight Delta: " + str(weight_delta))
