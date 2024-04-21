import main as main

def test_1(): #checking number of url
    url = main.call_pickle("save_url.pickle")
    print(f"Number of sites: {len(url)}")
    print(url)

def test_2(): #
    inv = main.call_pickle("inv_index.pickle")
    print(inv)

test_1()
#test_2()