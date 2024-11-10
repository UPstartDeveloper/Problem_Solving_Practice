import numpy as np
from numpy.typing import NDArray


class Solution:
    """Source: https://neetcode.io/problems/linear-regression-training"""
    def get_derivative(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64], N: int, X: NDArray[np.float64], desired_weight: int) -> float:
        # note that N is just len(X)
        return -2 * np.dot(ground_truth - model_prediction, X[:, desired_weight]) / N

    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        return np.squeeze(np.matmul(X, weights))

    learning_rate = 0.01

    def train_model(
        self,
        X: NDArray[np.float64],
        Y: NDArray[np.float64],
        num_iterations: int,
        initial_weights: NDArray[np.float64]
    ) -> NDArray[np.float64]:
        """ 'Batch' Gradient Descent (batch = full dataset)."""

        # you will need to call get_derivative() for each weight
        # and update each one separately based on the learning rate!
        # return np.round(your_answer, 5)

        # Pseudocode - DRIVER code
        # prev_weights = pw = initial_weights.copy()
        modified_weights = mw = initial_weights.copy().reshape(1, -1)
        # START: enter training loop - make a for loop
        for _ in range(num_iterations):
            # A: make y_pred
            y_pred = self.get_model_prediction(X, mw.T)

            # B: compute the grad
            grad = np.zeros_like(mw)
            # TODO[vectorize?]
            for weight_index in range(X.shape[1]):
                grad[0, weight_index] = self.get_derivative(
                    y_pred,
                    Y,
                    X.shape[0],
                    X,
                    weight_index
                )

            # C: update the weight vectors
            mw = mw - (self.learning_rate * grad)

        # END: return the final weights
        mw = np.apply_along_axis(lambda x: np.round(x, 5), 1, mw)
        return mw.squeeze()
