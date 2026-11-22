"""Roofline and Amdahl models; these are mathematical ceilings, not timings."""
import numpy as np

def roofline(peak_gflops,bandwidth_gbytes_per_s,intensity_flops_per_byte):
    p=float(peak_gflops);beta=float(bandwidth_gbytes_per_s);I=float(intensity_flops_per_byte)
    if not all(np.isfinite(x) for x in (p,beta,I)) or p<=0 or beta<=0 or I<0:
        raise ValueError("peak and bandwidth positive, intensity nonnegative, all finite")
    return min(p,beta*I)

def amdahl(serial_fraction,processors):
    f=float(serial_fraction)
    if not np.isfinite(f) or not (0<=f<=1):
        raise ValueError("serial fraction must be in [0,1]")
    if not isinstance(processors,int) or processors<1:
        raise ValueError("processor count must be positive integer")
    return 1./(f+(1.-f)/processors)

if __name__=="__main__":
    for I in (1,2,4,8):
        print("I",I,"roofline hypothetical GFLOP/s",roofline(200,50,I))
    for n in (1,2,4,16):
        print("cores",n,"Amdahl S with f=0.2",amdahl(0.2,n))
