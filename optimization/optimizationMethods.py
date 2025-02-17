import numpy as np
from typing import Callable
import random
import math

# Define our function and its derivatives
def f(x: float) -> float:
    """The function we want to minimize: f(x) = 3x² + 2x + 1"""
    return 3*x**2 + 2*x + 1

def df(x: float) -> float:
    """First derivative of f(x): f'(x) = 6x + 2"""
    return 6*x + 2

def d2f(x: float) -> float:
    """Second derivative of f(x): f''(x) = 6"""
    return 6

def gradient_descent(
    start_x: float = 0,
    learning_rate: float = 0.1,
    n_iterations: int = 100,
    tolerance: float = 1e-6
) -> tuple[float, list[float]]:
    """
    Implements gradient descent optimization.
    
    Args:
        start_x: Initial guess for x
        learning_rate: Step size for updates
        n_iterations: Maximum number of iterations
        tolerance: Convergence criterion
        
    Returns:
        tuple of (optimal x value, history of x values)
    """
    x = start_x
    history = [x]
    
    for _ in range(n_iterations):
        gradient = df(x)
        new_x = x - learning_rate * gradient
        
        # Check for convergence
        if abs(new_x - x) < tolerance:
            break
            
        x = new_x
        history.append(x)
    
    return x, history

def newtons_method(
    start_x: float = 0,
    n_iterations: int = 100,
    tolerance: float = 1e-6
) -> tuple[float, list[float]]:
    """
    Implements Newton's method for optimization.
    
    Args:
        start_x: Initial guess for x
        n_iterations: Maximum number of iterations
        tolerance: Convergence criterion
        
    Returns:
        tuple of (optimal x value, history of x values)
    """
    x = start_x
    history = [x]
    
    for _ in range(n_iterations):
        # Newton's method update: x = x - f'(x)/f''(x)
        new_x = x - df(x)/d2f(x)
        
        if abs(new_x - x) < tolerance:
            break
            
        x = new_x
        history.append(x)
    
    return x, history

def particle_swarm_optimization(
    n_particles: int = 20,
    n_iterations: int = 100,
    search_space: tuple[float, float] = (-10, 10)
) -> tuple[float, list[float]]:
    """
    Implements Particle Swarm Optimization (PSO).
    
    Args:
        n_particles: Number of particles in the swarm
        n_iterations: Maximum number of iterations
        search_space: Tuple of (min_x, max_x) defining search space
        
    Returns:
        tuple of (optimal x value, history of best positions)
    """
    # Initialize particles and velocities
    particles = np.random.uniform(search_space[0], search_space[1], n_particles)
    velocities = np.zeros(n_particles)
    
    # Initialize best positions
    personal_best = particles.copy()
    global_best = particles[np.argmin([f(p) for p in particles])]
    
    # PSO parameters
    w = 0.7  # inertia weight
    c1 = 1.5  # cognitive parameter
    c2 = 1.5  # social parameter
    
    history = [global_best]
    
    for _ in range(n_iterations):
        for i in range(n_particles):
            # Update velocity
            r1, r2 = random.random(), random.random()
            velocities[i] = (w * velocities[i] + 
                           c1 * r1 * (personal_best[i] - particles[i]) +
                           c2 * r2 * (global_best - particles[i]))
            
            # Update position
            particles[i] += velocities[i]
            
            # Update personal best
            if f(particles[i]) < f(personal_best[i]):
                personal_best[i] = particles[i]
                
            # Update global best
            if f(particles[i]) < f(global_best):
                global_best = particles[i]
                history.append(global_best)
    
    return global_best, history

def simulated_annealing(
    start_x: float = 0,
    temp: float = 1000.0,
    cooling_rate: float = 0.95,
    n_iterations: int = 1000
) -> tuple[float, list[float]]:
    """
    Implements Simulated Annealing optimization.
    
    Args:
        start_x: Initial guess for x
        temp: Initial temperature
        cooling_rate: Rate at which temperature decreases
        n_iterations: Maximum number of iterations
        
    Returns:
        tuple of (optimal x value, history of accepted positions)
    """
    current_x = start_x
    best_x = current_x
    history = [current_x]
    
    for _ in range(n_iterations):
        # Generate neighbor solution
        neighbor_x = current_x + np.random.normal(0, 1)
        
        # Calculate energy difference
        delta_E = f(neighbor_x) - f(current_x)
        
        # Accept worse solutions with probability exp(-delta_E/temp)
        if delta_E < 0 or random.random() < math.exp(-delta_E / temp):
            current_x = neighbor_x
            history.append(current_x)
            
            if f(current_x) < f(best_x):
                best_x = current_x
        
        # Cool down
        temp *= cooling_rate
    
    return best_x, history

# Run all methods and compare results
def runMethods():
    # True minimum (calculated analytically) is at x = -1/3
    true_minimum = -1/3
    
    methods = {
        "Gradient Descent": gradient_descent,
        "Newton's Method": newtons_method,
        "Particle Swarm": particle_swarm_optimization,
        "Simulated Annealing": simulated_annealing
    }
    
    print(f"True minimum is at x = {true_minimum:.6f}")
    print(f"True minimum value is f({true_minimum:.6f}) = {f(true_minimum):.6f}\n")
    
    for name, method in methods.items():
        x_min, history = method()
        print(f"{name}:")
        print(f"Found minimum at x = {x_min:.6f}")
        print(f"Found minimum value = {f(x_min):.6f}")
        print(f"Number of iterations: {len(history)}")
        print()
