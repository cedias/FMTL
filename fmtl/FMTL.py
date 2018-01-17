class FMTL():
    """
    Field-Mappable Tuple List (FMTL) 
    Each field's atomic unit can be mapped to a value. 
    """

    def __init__(self, tuplelist,rows=None, checks=None):
        def check_return(check_fun,field):
            check_fun(field)
            return field

        if isinstance(rows,list) or isinstance(rows,tuple):
            rows = {x:i for i,x in enumerate(rows)}

        self.rows = rows
        
        if checks is not None:
            self.tuplelist = list(check_return(checks,x) for x in tuplelist)
        else:
            self.tuplelist = list(tuplelist)

        self.mappings = {}
        self.unknown = {}
        
    def __len__(self):
        return len(self.tuplelist)

    def __getitem__(self,index):
        """
        Maps field[x]:
            -> if field is a tuple/list maps each element inside, keeping structure
            -> else directly maps
            -> if mapping function return error, tries to map with 'unk' value.
            (see self._rec_apply)
        """
        if len(self.mappings) == 0:
            return self.tuplelist[index]
        else:
            t = list(self.tuplelist[index])

            for i,m in self.mappings.items():
                if isinstance(m,dict):
                    t[i] = self._rec_apply(m.__getitem__,t[i],self.unknown.get(i))
                else:
                    try:
                        t[i] = m(t[i])
                    except Exception:
                        if self.unknown.get(i) is not None:
                            return self.unknown.get(i)
                        else:
                            raise KeyError("No mapping or placeholder for value: {}".format(i))

            return tuple(t)

    def __iter__(self):
        self.iter_idxs = range(len(self.tuplelist)).__iter__()
        return self

    def __next__(self):
        return self[self.iter_idxs.__next__()]

    def _rec_apply(self,f,item,unk=None):
        if isinstance(item,list) or isinstance(item,tuple):
            return type(item)(map(lambda x:self._rec_apply(f,x,unk), item))
        else:
            try:
                return f(item)
            except Exception:
                if unk is not None:
                    return unk
                else:
                    raise KeyError("No mapping or placeholder for value: {}".format(item))


    def f2i(self,field):
        if type(field) == int:
            return field

        if type(field) == str:
            return self.rows[field]

        if type(field) == str and self.rows == None:
            raise IndexError("field {} index is unknown, no rows attribute provided".format(field))

        raise IndexError("field {} doesn't exist".format(field))

        
    def set_mapping(self, field, mapping, unk=None):
        """
        Sets a mapping for a tuple field. Mappings are functions of a field value or dict
        """
        field = self.f2i(field)
        self.mappings[field] = mapping

        if unk is not None:
            self.unknown[field] = unk

        return mapping

    def field_gen(self, field, key_iter=None):

        field = self.f2i(field)
        if key_iter is None:
            key_iter = range(len(self))

        for idx in key_iter:
            yield self[idx][field]