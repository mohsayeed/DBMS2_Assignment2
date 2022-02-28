import csv
with open ('source.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
contents = contents.split('\n\n')
numb_entries = (len(contents))
# print((contents[0]))


def contents_csv(contents):
    papers = open('papers.csv', 'w', encoding='UTF8', newline='')
    year = open('year.csv', 'w', encoding='UTF8', newline='')
    venue = open('venue.csv', 'w', encoding='UTF8', newline='')
    mainauthor = open('mainauthor.csv', 'w', encoding='UTF8', newline='')
    coauthor = open('coauthor.csv', 'w', encoding='UTF8', newline='')
    referenceslist = open('referenceslist.csv', 'w', encoding='UTF8', newline='')
    hpapers = ['id', 'title', 'abstract']
    hyear = ['id', 'year']
    hvenue = ['id', 'venue']
    hmainauthor = ['id','mainauthor']
    hcoauthor = ['id','coauthor']
    hreferenceslist = ['id','referenceid']
    wpapers = csv.writer(papers)
    wyear = csv.writer(year)
    wvenue = csv.writer(venue)
    wmainauthor = csv.writer(mainauthor)
    wcoauthor = csv.writer(coauthor)
    wreferenceslist = csv.writer(referenceslist)
    wpapers.writerow(hpapers)
    wyear.writerow(hyear)
    wvenue.writerow(hvenue)
    wmainauthor.writerow(hmainauthor)
    wcoauthor.writerow(hcoauthor)
    wreferenceslist.writerow(hreferenceslist)
    dpapers = {}
    dyear = {}
    dvenue = {}
    dmainauthor = {}
    dcoauthor = {}
    dreferenceslist = {}
    for x in hpapers:
        y = dpapers.setdefault(x)
    for x in hyear:
        y = dyear.setdefault(x)
    for x in dvenue:
        y = dvenue.setdefault(x)
    for x in hmainauthor:
        y = dmainauthor.setdefault(x)
    for x in hcoauthor:
        y = dcoauthor.setdefault(x)
    for x in hreferenceslist:
        y = dreferenceslist.setdefault(x)

    for x in contents:
        tpapers = dpapers
        tyear = dyear
        tvenue = dvenue
        tmainauthor = dmainauthor
        tcoauthor = dcoauthor
        treferenceslist = dreferenceslist
        temp_coauthor_dict = []
        x_lines = x.split('\n')
        index_crecord = 0
        for y in x_lines:
            if(y.startswith('#*')):
                if(y[2:]):
                    tpapers['title'] = y[2:]
            elif(y.startswith('#index')):
                tpapers['id'] = int(y[6:])
                index_crecord = int(y[6:])
                # print(index_crecord)
            elif(y.startswith('#!')):
                if(y[2:]):
                    tpapers['abstract'] = y[2:]
            elif(y.startswith('#t')):
                if(y[2:]):
                    tyear['year'] = int(y[2:])
            elif(y.startswith('#c')):
                if(y[2:]):
                    tvenue['venue'] = (y[2:])
            elif(y.startswith('#%')):
                if(y[2:]):
                    treferenceslist['id'] = index_crecord
                    treferenceslist['referenceid'] = int(y[2:])
                    res = list(map(treferenceslist.get, hreferenceslist))
                    wreferenceslist.writerow(res)
                    treferenceslist = dreferenceslist
            elif(y.startswith('#@')):
                if(y[2:]):
                    list_authors = y[2:].split(',')
                    tmainauthor['mainauthor'] = list_authors[0]
                    for la in range(1,len(list_authors)):
                        if(list_authors[la]):
                            tcoauthor['coauthor'] = list_authors[la]
                            temp_coauthor_dict.append(tcoauthor)
                            tcoauthor = dcoauthor
        for tt in temp_coauthor_dict:
            tt['id'] = index_crecord
            wcoauthor.writerow(list(map(tt.get,hcoauthor)))
        tyear['id'] = index_crecord
        tvenue['id'] = index_crecord
        tmainauthor['id'] = index_crecord
        # print(list(map(tpapers.get, hpapers)))
        wpapers.writerow(list(map(tpapers.get, hpapers)))
        wmainauthor.writerow(list(map(tmainauthor.get, hmainauthor)))
        wyear.writerow(list(map(tyear.get, hyear)))
        wvenue.writerow(list(map(tvenue.get, hvenue)))
contents_csv(contents)


# # filt_keys= ['gfg','is','best']
# # test_dict = {'gfg' : 'sdafljk', 'is' : '', 'best' : 3}
# # res = list(map(test_dict.get, filt_keys))
# # print(res)


# # d = {}
# # header = ['title', 'authors', 'year','venue','index','references','abstract']
# # for x in header:
# #     y = d.setdefault(x)
# # print(d)





# # content1 = contents[0].split('\n')
# # count = 1
# # header = ['title', 'authors', 'year','venue','index','references','abstract']
# # with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
# #     writer = csv.writer(f)
# #     writer.writerow(header)
# #     data = []
# #     writer.writerow(data)
# #     for c in contents:
# #         if(count == 1):
# #             chunk = c.split('\n')
# #             print(chunk)
# #             count+=1





#  elif(y.startswith('#@')):
#                 temp = y[2:].split(',')
#             elif(y.startswith('#t')):
#                 temp['year'] = int(y[2:])
#             elif(y.startswith('#c')):
#                 temp['venue'] = y[2:]
#             elif(y.startswith('#index')):
#                 temp['index'] = int(y[6:])
#             elif(y.startswith('#%')):
#                 temp['index'] = 





# import time

# start = time.time()
# count = 0
# line = ''
# with open("source.txt", encoding='utf-8') as file:
#     for line in file:
#         count = count + 1
# end = time.time()
# print("Execution time in seconds: ",(end-start))
# print("No of lines printed: ",line)
