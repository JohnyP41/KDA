import lbg

testdata = [(-1.5, 2.0, 5.0),
            (-2.0, -2.0, 0.0),
            (1.0, 1.0, 2.0),
            (1.5, 1.5, 1.2),
            (1.0, 2.0, 5.6),
            (1.0, -2.0, -2.0),
            (1.0, -3.0, -2.0),
            (1.0, -2.5, -4.5)]

for cb_size in (1, 2, 4, 8):
    print('generating codebook for size', cb_size)
    cb, cb_abs_w, cb_rel_w = lbg.generate_codebook(testdata, cb_size)
    print('output:')
    for i, c in enumerate(cb):
        print('> %s, abs_weight=%d, rel_weight=%f' % (c, cb_abs_w[i], cb_rel_w[i]))

