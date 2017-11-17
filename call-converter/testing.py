import re
def function_one(array):    
    #query = arr[-1].split(":")[-1]
    # query=query[1:]
    base_url = "https://localhost:5000/"
    query = query.lower()
    if "where" in query:
        matchObj = re.match(r"select (.*) from (.*) where (.*)", query)
        select_arr = matchObj.group(1)
        from_arr = matchObj.group(2)
        where_arr = arr[-1].split(":")[-1].split(" where ")[-1]
        itr_arr = where_arr.split(" and ")
        # print itr_arr
        if select_arr == str("*"):
            x = arr[3].split(r"/")
            x = x[-1]
            url = base_url + x
            url = url + "?"
            for where_string in range(len(itr_arr)):
                if where_string != 0:
                    url = url + "&" + itr_arr[where_string]
                else:
                    url = url + itr_arr[where_string]
            print url.replace("'", "").replace(" ", "")
        else:
            x = arr[3].split(r"/")
            x = x[-1]
            url = base_url + x
            url = url + "?"
            for where_string in range(len(itr_arr)):
                if where_string != 0:
                    url = url + "&" + itr_arr[where_string]
                else:
                    url = url + itr_arr[where_string]
            url= url.replace("'", "").replace(" ", "")
            select_arr = re.match(r"Select (.*) from .*",arr[-1].split(":")[-1])
            select_arr= select_arr.group(1).split(",")
            for a in select_arr:
                url=url+"-"+a
            print url

if __name__ == "__main__":
    array=[]
    with open(r"C:\Users\pranil_ambule\Documents\wsman-simulator-dev\automation\call-converter\filter-file.txt","r") as ff:
        for f in ff:
            array.append(f.strip())
        ff.close()
    print array
    #function_one(array)
