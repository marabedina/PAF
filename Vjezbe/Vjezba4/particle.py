import math
import matplotlib.pyplot as plt
class particle:
    def __init__(self,v0,theta,x0=0,y0=0):
        self.v0=v0
        self.theta=math.radians(theta)
        self.x0=x0
        self.y0=y0
        self.reset()
    def reset (self):
        self.x=x0
        self.y=y0
        self.vx=self.v0=math.cos(self.theta)
        self.vy=self.v0=math.sin(self.theta)
        self.t=0
        self.trajectory_x=[self.x]
        self.trajectory_y=[self.y]
    def __move (self,dt):
        g=9.81
        self.t+=dt
        self.x+=self.vx*dt
        self.y+=self.vy*dt
        self.trajectory_x.append(self.x)
        self.trajectory_y.append(self.y)

    def range(self,dt=0.01):
        self.reset()
        while self.y>=0:
            self.__move(dt)
            return self.x
    def plot_trajectory(self, dt=0.01):
        self.reset()
        while self.y>=0:
            self.__move(dt)
        traj = np.array(self.trajectory)
        xs = traj[:, 0]
        ys = traj[:, 1]

        plt.plot(xs,ys)
        plt.xlabel("x(m)")
        plt.ylabel("y(m)")
        plt.title("putanja cestice")
        plt.grid()
        plt.show()


        