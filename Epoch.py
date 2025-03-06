import numpy as np
def get_epochs_for_new_data(T, T0, P, E0, tra_or_occ):
    """
    T: float
        Mid-time for your new point
    T0: float
        The mid-time of the very first epoch
    P: float
        Orbital period
    E0: int
        The first epoch number. Will be added to make sure initial epoch number is accounted for
    tra_or_occ: str
        If your observation is a transit, "tra". If it is an occultation, "occ".
    """
    N = (T-T0)/P
    if tra_or_occ == "occ":
        N = np.floor(N)
    return int(N + E0)
Epoch= get_epochs_for_new_data(2460493.7856, 2458247.90746, 1.65, -408, "tra")
print(Epoch)