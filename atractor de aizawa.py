from manim import *

class atractor_aizawa_largo(ThreeDScene):
    config.disable_caching=True
    config.frame_width = 9
    config.frame_height = 16

    config.pixel_width = 420
    config.pixel_height = 854
    def construct(self):
        
        dot = Sphere(radius=0.005,fill_color=BLUE).move_to(0.1*RIGHT + 0*UP + 0*OUT)
        self.move_camera(zoom=1.75,run_time=0.001)
        self.set_camera_orientation(phi=65 * DEGREES,theta=30*DEGREES,gamma = 90*DEGREES)  
        self.begin_ambient_camera_rotation(rate=0.3)
        self.begin_ambient_camera_rotation(rate=0.2, about="gamma")         #Start move camera

        dtime = 0.01
        numsteps = 30

        self.add(dot)

        def lorenz(x, y, z, a=0.95,b=0.3,c=0.6,d=3.5,e=0.25,f=0.1):
            x_dot = ((z - b) * x - d * y)
            y_dot = (d * x + (z - b) * y)
            z_dot = (c + a * z - (z ** 3 / 3*d) - (x ** 2) + f * z * (x ** 3))
            return x_dot, y_dot, z_dot

        def update_trajectory(self, dt):
            new_point = dot.get_center()
            if np.linalg.norm(new_point - self.points[-1]) > 0.01:
                self.add_smooth_curve_to(new_point)
#(new_point - self.points[-1])/np.linalg.norm(new_point - self.points[-1]) > 0.01
        traj = VMobject()
        traj.start_new_path(dot.get_center())
        traj.set_stroke(BLUE, 2, opacity=0.8)
        traj.add_updater(update_trajectory)
        self.add(traj)

        def update_position(self,dt):
            x_dot, y_dot, z_dot = lorenz(dot.get_center()[0], dot.get_center()[1], dot.get_center()[2])
            x = x_dot * dt*4
            y = y_dot * dt*4
            z = z_dot * dt*4
            
            self.shift(x/10*RIGHT + y/10*UP + z/10*OUT)
            

        dot.add_updater(update_position)
        self.wait(60*8)

        