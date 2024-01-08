# id.txt file contains every 10ht titleId from originl file - title_ratings_tsv.tsv
titles = None
with open('id.txt') as id :
    titles = id.read().split('\n')
id.close()
titles = set(titles)

# scrape basics
with open ("title_basics_scraped.tsv",'w',encoding="utf8") as w:
    with open("title_basics_tsv.tsv",'r',encoding="utf8") as f:
        header = f.readline().split('\t')
        w.write('\t'.join ([header[0],header[1],header[2],header[5],header[7],header[8]]))
        i = 0
        count = 0
        for line in f:
            if i % 100000 == 0 : print(i)
            line = line.split('\t')
            if line[0] in titles:
                count += 1
                row = '\t'.join ([line[0],line[1],line[2],line[5],line[7],line[8]])
                w.write(row)
            i += 1
print(count)
w.close()
f.close()

# scrape crew
with open ("title_crew_scraped.tsv",'w',encoding="utf8") as w:
    with open("title_crew_tsv.tsv",'r',encoding="utf8") as f:
        header = f.readline().split('\t')
        w.write('\t'.join ([header[0],header[1],header[2]]))

        count,i = 0,0
        for line in f:
            if i % 100000 == 0 : print(i)
            line = line.split('\t')
            if line[0] in titles:
                count += 1
                row = '\t'.join ([line[0],line[1],line[2]])
                w.write(row)
            i += 1
w.close()
f.close()

# scrape akas 
with open ("title_akas_scraped.tsv",'w',encoding="utf8") as w:
    with open("title_akas_tsv.tsv",'r',encoding="utf8") as f:
        header = f.readline().split('\t')
        w.write('\t'.join ([header[0],header[2],header[3],header[4] + '\n']))
        
        i,count = 0,0
        for line in f:
            if i % 100000 == 0 : print(i)
            line = line.split('\t')
            if line[0] in titles:
                count += 1
                row = '\t'.join ([line[0],line[2],line[3],line[4] + '\n'])
                w.write(row)
            i += 1
w.close()
f.close()

#scrape princpals
with open ("title_principals_scraped.tsv",'w',encoding="utf8") as w:
    with open("title_principals_tsv.tsv",'r',encoding="utf8") as f:
        header = f.readline().split('\t')
        w.write('\t'.join ([header[0],header[2],header[3],header[4],header[5]]))
        
        i,count = 0,0
        for line in f:
            if i % 100000 == 0 : print(i)
            line = line.split('\t')
            if line[0] in titles:
                count += 1
                row = '\t'.join ([line[0],line[2],line[3],line[4],line[5]])
                w.write(row)
            i += 1
w.close()
f.close()

# scrape ratings
with open ("title_ratings_scraped.tsv",'w',encoding="utf8") as a:
    with open("title_ratings_tsv.tsv",'r',encoding="utf8") as b: 
        header = b.readline().split('\t')
        a.write('\t'.join ([header[0],header[1],header[2]]))
        
        i = 0
        for line in b:
            if i % 100000 == 0 : print(i)
            line = line.split('\t')
            if line[0] in titles:
                row = '\t'.join ([line[0],line[1],line[2]])
                a.write(row)
            i += 1
a.close()
b.close()

# find every person(nconst) asociated with titleId in id.txt
persons = set()
with open ("title_crew_scraped.tsv",'r',encoding="utf8") as w:
     w.readline()
     for line in w:
        line = line.split('\t')
        if line[0] in titles:
            if repr(line[1]) != "'\\\\N'":
                 for p in line[1].split(',') : persons.add(p)
            
            l = line[2].strip()
            if repr(l) != "'\\\\N'":
                 for p in l.split(',') : persons.add(p)

with open("title_principals_scraped.tsv",'r',encoding="utf8") as f:
        f.readline()
        for line in f:
            line = line.split('\t')
            if line[0] in titles:
                 persons.add(line[1])
w.close()
f.close()

# scrape persons
with open ("name_basics_scraped.tsv",'w',encoding="utf8") as a:
    with open("name_basics_tsv_gz.tsv",'r',encoding="utf8") as b: 
        header = b.readline().split('\t')
        a.write('\t'.join ([header[0],header[1],header[2],header[4],header[5]]))
        
        i = 0
        for line in b:
            if i % 100000 == 0 : print(i)
            line = line.split('\t')
            if line[0] in persons:
                row = '\t'.join ([line[0],line[1],line[2],line[4],line[5]])
                a.write(row)
            i += 1
a.close()
b.close()
