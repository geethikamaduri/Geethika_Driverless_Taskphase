import numpy as np
from scipy.optimize import minimize

#initial conditions

x = 0.1
y = 3.1
theta = np.radians(90)
v = 5.5
v_desired = 10

# way points

A = np.array([0.9,3.0])
B = np.array([1.0,4.1])

#time interval

dt = 0.02
steps = 3

#heading

dx = B[0] - A[0]
dy = B[1] - A[1]

theta_desired = np.arctan2(dy,dx)

#cross-track error

def cross_track_error(x,y):
    numerator = abs((B[0] - A[0]) * (y - A[1]) - (B[1] - A[1]) * (x - A[0]))
    denominator = np.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)
    return numerator / denominator

#cost function

def cost_function(controls):
    a, omega = controls
    x_sim = x
    y_sim = y
    theta_sim = theta
    v_sim = v
    total_cost = 0
    w_heading = 10.0
    w_cross_track = 1.0
    w_velocity = 0.1
    for i in range(steps):
        x_sim += v_sim * np.cos(theta_sim)*dt
        y_sim += v_sim * np.sin(theta_sim)*dt
        theta_sim += omega * dt
        v_sim += a * dt
        heading_error = theta_desired - theta_sim
        heading_error = np.arctan2(
            np.sin(heading_error),
            np.cos(heading_error)
        )
        cte = cross_track_error(x_sim, y_sim)
        velocity_error = v_desired - v_sim
        step_cost = (
            w_heading * heading_error**2
            + w_cross_track * cte**2
            + w_velocity * velocity_error**2
        )
        total_cost += step_cost
    return total_cost / steps

#initial guess

initial_guess = [1.3, 0.23]
initial_cost = cost_function(initial_guess)
bounds = [
    (-13, 13),  #acceleration
    (-1.5, 1.5)  #yaw rate
]
result = minimize(
    cost_function,
    initial_guess,
    method = "L-BFGS-B",
    bounds=bounds
)

print("Initial cost: ",initial_cost)
print("Optimised cost: ",result.fun)
print("Optimal acceleration: ",result.x[0], "m/s^2")
print("Optimal yaw rate: ",result.x[1],"rad/s")
print("Optimisation successul: ",result.success)