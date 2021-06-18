import requests
import os
import re
url=f"https://upload.wikimedia.org/wikipedia/en/thumb/e/e7/W._S._Gilbert_-_Alice_B._Woodward_-_The_Pinafore_Picture_Book_-_Frontispiece.jpg/450px-W._S._Gilbert_-_Alice_B._Woodward_-_The_Pinafore_Picture_Book_-_Frontispiece.jpg"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
    }
response=requests.get(url=url,headers=headers)
image=response.content
f=open("C://Users//Asus//Desktop//New folder//test1.jpg","wb")
f.write(image)
print("Success")
