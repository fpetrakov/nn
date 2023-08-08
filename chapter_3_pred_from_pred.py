import numpy as np


def vect_mat_mul(vect, matrix):
    assert len(vect) == len(matrix)

    output = [0, 0, 0]

    for i in range(len(vect)):
        output[i] = np.dot(vect, matrix[i])

    return output


def neural_network(input, weights):
    hid = vect_mat_mul(input, weights[0])
    pred = vect_mat_mul(hid, weights[1])
    return pred


toes = np.array([8.5, 9.5, 9.9, 9.0])
wlrec = np.array([0.65, 0.8, 0.8, 0.9])
nfans = np.array([1.2, 1.3, 0.5, 1.0])

input = np.array([toes[0], wlrec[0], nfans[0]])

ih_weights = np.array(
    [np.array([0.1, 0.2, 0]), np.array([0.1, 0.1, -0.3]), np.array([0.0, 1.3, 0.1])]
)
hp_weights = np.array(
    [np.array([0.1, 0.2, 0]), np.array([0.1, 0.1, -0.3]), np.array([0.0, 1.3, 0.1])]
)

weights = [ih_weights, hp_weights]

pred = neural_network(input, weights)
print(pred)
