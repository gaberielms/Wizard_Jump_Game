import pygame, random


class Particles:
    
    def __init__(self, display):
        self.particles = []
        self.display = display

    def emit(self):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                particle[0][0] += particle[2][0]
                particle[0][1] += particle[2][1]
                particle[1] -= 0.5
                pygame.draw.circle(self.display, '#CBD8E1', particle[0], particle[1])

    def add_particles(self, x_pos, y_pos, x_dir, y_dir):
        radius = 3
        direction_y = random.randint(-y_dir * 10, 0) / 10
        if x_dir > 0:
            direction_x = random.randint(-x_dir * 10, 0) / 10
        else:
            direction_x = random.randint(0, -x_dir * 10) / 10
        particle_circle = [[x_pos, y_pos], radius, [direction_x, direction_y]]
        self.particles.append(particle_circle)

    def delete_particles(self):
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy
    