import numpy as np
import matplotlib.pyplot as plt

def metropolis_hastings(target_pdf, proposal_dist, proposal_width, initial_position, n_steps):
    """
    Metropolis-Hastings algorithm for sample generating.

    :param target_pdf: Probability density function of the target distribution.
    :param proposal_dist: Function to generate proposal samples (usually a normal distribution).
    :param proposal_width: Width of the proposal distribution.
    :param initial_position: Starting point for the sampling.
    :param n_steps: Number of sampling steps.
    :return: Generated samples.
    """
    current_position = initial_position
    samples = [current_position]

    for _ in range(n_steps):
        proposed_position = proposal_dist(current_position, proposal_width)
        acceptance_probability = min(target_pdf(proposed_position) / target_pdf(current_position), 1)
        if np.random.rand() < acceptance_probability:
            current_position = proposed_position
        samples.append(current_position)

    return samples

def plot_samples(samples):
    """
    Visualize the samples generated by the Metropolis-Hastings algorithm.

    :param samples: List of samples generated by the Metropolis-Hastings algorithm.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(samples, marker='o', linestyle='none', markersize=2, label='Samples')
    plt.title('Samples generated by Metropolis-Hastings')
    plt.xlabel('Sample index')
    plt.ylabel('Sample value')
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    target_pdf = lambda x: np.exp(-x**2 / 2) / np.sqrt(2 * np.pi)
    proposal_dist = lambda current, width: np.random.normal(current, width)
    samples = metropolis_hastings(target_pdf, proposal_dist, proposal_width=1.0, initial_position=0.0, n_steps=10000)
    plot_samples(samples)
