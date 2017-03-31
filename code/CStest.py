import numpy as np                  # Numeric methods and data structures
import matplotlib.pyplot as plt     # Plotting functionality
import seaborn as sns               # Prettier plots
from basic_algs import OMP          # Algorithm for solving P1


def main():
    N = 100
    s = 5
    m = 4*s

    # Generate s-sparse vector
    true_sparse_vector = np.asmatrix(np.zeros([N, 1]))
    non_sparse_indexes = np.random.randint(low=0, high=N, size=s)
    for i in non_sparse_indexes:
        true_sparse_vector[i,0] = np.random.rand()

    # Drawing random sensing matrix \in R^{m, N} from N(0, 1)
    sensing_matrix = np.asmatrix(np.random.randn(m, N))

    # Sampling vector with sensing matrix
    sampled_vector = np.matmul(sensing_matrix, np.asmatrix(true_sparse_vector));

    # Reconstructing vector using the simplex method
    reconstructed_vector = OMP(sensing_matrix, sampled_vector)

    # Plot vectors. Create new figure
    plt.figure()

    ## True vector 
    plt.subplot(3, 1, 1)
    plt.stem(true_sparse_vector[:,0])

    ## Sampled vector
    plt.subplot(3, 1, 2)
    plt.stem(sampled_vector)

    ## Reconstructed vector
    plt.subplot(3, 1, 3)
    plt.stem(reconstructed_vector[0])

    plt.show()
    

if __name__ == '__main__':
    main()
