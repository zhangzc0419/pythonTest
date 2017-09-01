def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        print total/len(series)
        return total/len(series)

    return averager

if __name__ == '__main__':
    avg = make_averager()
    avg(10)
    avg(11)
    avg(12)