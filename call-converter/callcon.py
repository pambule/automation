import sys
import re

def fun1(arr, base_url):
    where_arr = []
    query = ''
    simple = 1
    if "select" in arr[-1].lower():
        simple = 0
    else:
        simple = 1
    if simple == 1:
        x = arr[3].split(r"/")
        x = x[-1]
        url = base_url + x
    else:
        query = arr[-1].split(":")[-1]
        query = query.lower()
        if "where" in query:
            matchObj = re.match(r"select (.*) from (.*) where (.*)", query)
            select_arr = matchObj.group(1)
            from_arr = matchObj.group(2)
            where_arr = arr[-1].split(":")[-1].split(" where ")[-1]
            itr_arr = where_arr.split(" and ")
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

        else:
            matchObj = re.match(r"select (.*) from (.*)", query)
            select_arr = matchObj.group(1)
            from_arr = matchObj.group(2)
            if select_arr == str("*"):
                x = arr[3].split(r"/")
                x = x[-1]
                url = base_url + x
                print url
            else:
                x = arr[3].split(r"/")
                x = x[-1]
                url=base_url+x+"?"
                select_arr = re.match(r"Select (.*) from .*",arr[-1].split(":")[-1])
                select_arr= select_arr.group(1).split(",")
                for a in select_arr:
                    url=url+"-"+a
                print url                


if __name__ == "__main__":
    arr = sys.argv
    if len(arr)<2:
    	print "no arguments provided"
    else:
		base_url = "https://localhost:5000/"
		fun1(arr, base_url)
