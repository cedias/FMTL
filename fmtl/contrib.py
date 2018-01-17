from collections import Counter
import itertools



def indexed_iter(fmtl,idxs):
    """
    Simple indexed iterator on FMTL:
    returns a FMTL_iterator object which is the same FMTL instance which only iterates on the idxs slice.
    """
    class FMTL_iterator():		
        def __init__(self, fmtl, idxs):
            self.fmtl = fmtl
            self.idxs = idxs

        def __getitem__(self, i):
            return self.fmtl[self.idxs[i]]

        def __len__(self):
            return len(self.idxs)

        def __iter__(self):
            self.iter_idx = self.idxs.__iter__()
            return self

        def __next__(self):
            idx = self.iter_idx.__next__()
            return self.fmtl[idx]

    return FMTL_iterator(fmtl,idxs)


def get_stats(fmtl, field, key_iter=None, verbose=False):
    """
    helper for stats on a field. Field values should be hashable.
    """
    field = fmtl.f2i(field)
    d =  dict(Counter(fmtl.field_gen(field,key_iter=key_iter)))
    sumv = sum([v for k,v in d.items()])
    class_per = {k:(v/sumv) for k,v  in d.items()}

    if verbose:
        print(d)
        print(class_per)

    return d,class_per


def get_field_dict(fmtl, field, offset=0, max_count=-1, key_iter=None, iter_func=None):
    """
    Helper to create a dict from a field.
    """
    field_gen = fmtl.field_gen(fmtl.f2i(field),key_iter=key_iter)

    if iter_func is not None:
        field_gen = itertools.chain.from_iterable((x for x in iter_func(field_gen)))
        
    d =  Counter(field_gen)

    if max_count > -1:
        d_keys = (k for k,v in d.most_common(max_count))
    else:
        d_keys = d.keys()

    d2k = {c:i for i,c in enumerate(d_keys,offset)}
    return d2k


