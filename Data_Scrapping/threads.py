from get_links import * 

#tried to incorporate threads but didn't succeded 
#was wsorking with the number of pages but didn't figured it out with provinces
def pool(numbers_drivers,driver):

    urls = len(get_links())
    # 1 driver by thread (we have four thread here)
    drivers = [driver  for _ in range(numbers_drivers)]
    division = npurl.array_split(npurl.arange(1,urls),numbers_drivers)
    #creation of a pool of threads
    list_of_result = []
    with ThreadPoolExecutor(max_workers= 10) as executor :
        #it is where it needs refinement
        results = executor.map(get_links,division,drivers)
        for result in results :
            for x in result : 
                #print(x)
                link_file(x)
            return 
        