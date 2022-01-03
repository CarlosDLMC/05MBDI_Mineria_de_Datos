def modify_lines(line):
    data = line.split(',')
    # return f"data[2],data[3][:10],data[4],data[5],data[6],data[7]\n"
    return "{},{},{:.2f},{:.2f},{:.2f},{:.2f}\n".format(data[2], data[3][:10], float(data[4]), float(data[5]), float(data[6]), float(data[7]))

def get_lines(file):
    with open(file, "r") as coin:
        lines = coin.readlines()
        return ["Symbol,Date,High,Low,Open,Close\n"] + [modify_lines(line) for line in lines[1::]]


with open("bitcoin_modificado.csv", "w") as coin:
    coin.writelines(get_lines("coin_Bitcoin.csv"))