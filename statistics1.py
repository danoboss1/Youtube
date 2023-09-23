import random

UNIT_CIRCLE = 1

def monte_carlo_pi(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        x = random.random()
        y = random.random()

        if x**2 + y**2 <= UNIT_CIRCLE:
            inside_circle += 1
    
    return inside_circle


sample_size = 10000
inside_circle = monte_carlo_pi(sample_size)

estimated_pi = (inside_circle / sample_size) * 4

print(f'Estimated PI is {estimated_pi}')