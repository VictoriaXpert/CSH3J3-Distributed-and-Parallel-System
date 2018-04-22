import time
from mpi4py import MPI


def Pi(num_steps):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    start = time.time()
    step = 1.0/num_steps
    sum = 0
    hasil = 0

    if rank == 0:
        for i in range(1, int((rank+1)*(num_steps/size))):
            x = (i+0.5)*step
            sum += 4.0/(1.0+x*x)
            pi = step * sum
        hasil = pi
        for i in range(1, size):
            hasil += comm.recv(source=i)
        print("Pi: ", hasil)
    else:
        for i in range(int(rank*num_steps/size), int((rank+1)*(num_steps/size))):
            x = (i+0.5)*step
            sum += 4.0/(1.0+x*x)
            pi = step*sum
        comm.send(pi, dest=0)
    end = time.time()
    print("Pi with %d steps is %f in %f secs" % (num_steps, pi, end-start))


if __name__ == '__main__':
    Pi(100000)
