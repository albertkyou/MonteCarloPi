# MonteCarloPi
Monte Carlo simulation to approximate the value of pi

Given a unit circle (r=1) inscribed inside a square of side length 2, we can calculate the areas of each shape as follows:

A_square = (2r)^2 = 4
A_circle = pi(r)^2 = pi

Using a Monte Carlo simulation, we can then assess how many random points land within the circle compared to how many points land outside of the circle.

Proportion of points inside circle = A_circle/A_square = pi/4.

Therefore, we approximate pi as 4 x proportion.
