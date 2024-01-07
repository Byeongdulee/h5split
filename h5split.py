import h5py
import sys
def split(fn='', mykey=''):
    if len(fn)==0:
        return False
    with h5py.File(fn, "r") as f:
        kys = list(f.keys())
        for k in kys:
            if len(mykey)>0:
                if k != mykey:
                    continue
            a = f[k]
            nfn = k+".h5"
            f2 = h5py.File(nfn, "w")
            f.copy(a, f2)
            f2.close()
            print(f"{k} is saved.")
    f.close()

if __name__ == "__main__":
    #import argparse
    #parser = argparse.ArgumentParser()
    #parser.add_argument("-f", "--fn", type=str, default='Holder_2.h5')
    #parser.add_argument("-k", "--mykey", type=str, default='')
    #ns = parser.parse_args()
    #split(**ns.__dict__)
    if len(sys.argv)==3:
        split(sys.argv[1], sys.argv[2])
    elif len(sys.argv)==2:
        split(sys.argv[1])