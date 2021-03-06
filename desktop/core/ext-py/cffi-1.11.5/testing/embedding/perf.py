import cffi

ffi = cffi.FFI()

ffi.embedding_api("""
    int add1(int, int);
""")

ffi.embedding_init_code(r"""
    from _perf_cffi import ffi

    @ffi.def_extern()
    def add1(x, y):
        return x + y
""")

ffi.set_source("_perf_cffi", """
""")

fn = ffi.compile(verbose=True)
print('FILENAME: %s' % (fn,))
