def com_fn(passline):
    def in_fn(val):
        if val > passline:
            return 'pass'
        else:
            return 'failed'

    return in_fn


fn_100 = com_fn(60)
fn_150 = com_fn(90)

print fn_100(89)
print fn_150(89)
