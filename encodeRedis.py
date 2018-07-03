# from redis_protocol import decode, encode
# a = encode("set key89 value89 set key90 value90 set key91 value91 set key92 value92 set key93 value93")
# print(a)
# a = decode(a)
# print(a)

with open("dataraw.txt", "rt") as fin:
    with open("out.txt", "wt") as fout:
        for line in fin:
            if line != "\n":
                fout.write(line.replace("\t", '\n'))