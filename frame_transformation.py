import numpy as np

x0 = 10.0
y0 = 5.0
theta0 = np.radians(30)

v = 5.0
a = 1.0
omega = np.radians(10)  # Convert degrees to radians

T = 0.2
dt = 0.0001
n = int(T / dt)

x = x0
y = y0
theta = theta0

for i in range(n):

    theta_mid = theta + omega * dt / 2
    v_mid = v + a * dt / 2

    x += v_mid * np.cos(theta_mid) * dt
    y += v_mid * np.sin(theta_mid) * dt

    theta += omega * dt
    v += a * dt

print("New car pose:")
print("x =", x)
print("y =", y)
print("theta =", np.degrees(theta), "degrees")

cones = {
    "B1": (12, 7),
    "B2": (8, 6),
    "Y1": (13, 4),
    "Y2": (9, 3)
}

def global_to_car(cone_x, cone_y, car_x, car_y, theta):

    dx = cone_x - car_x
    dy = cone_y - car_y

    R = np.array([
    [np.cos(theta), np.sin(theta)],
    [-np.sin(theta), np.cos(theta)]
    ])

    relative_position = np.array([dx, dy])

    local_position = R @ relative_position

    x_local = local_position[0]
    y_local = local_position[1]
    return x_local, y_local


print("\nCone coordinates at initial pose:")

for name, (cx, cy) in cones.items():

    local_x, local_y = global_to_car(
        cx, cy, x0, y0, theta0
    )

    print(name, ":", local_x, local_y)


print("\nCone coordinates at new pose:")

for name, (cx, cy) in cones.items():

    local_x, local_y = global_to_car(
        cx, cy, x, y, theta
    )

    print(name, ":", local_x, local_y)