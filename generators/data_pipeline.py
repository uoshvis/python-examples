def main():
    file_name = 'data.csv'
    lines = (line for line in open(file_name))
    list_line = (s.rstrip().split(",") for s in lines)
    # uses next() to store the column names in a list.
    cols = next(list_line)
    company_dicts = (dict(zip(cols, data)) for data in list_line)
    funding = (
        int(company_dict["raisedAmt"])
        for company_dict in company_dicts
        if company_dict["round"] == "a"
    )
    # iteration works only here
    #  begins the iteration process by calling sum()
    total_series_a = sum(funding)
    print(total_series_a)


if __name__ == '__main__':
    main()
