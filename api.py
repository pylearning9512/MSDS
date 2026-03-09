import webbrowser

sku = input("please enter your product id: \n")

def msds():
    
    
    list_of_products = []

    for i in sku.split(","):
        base = f"https://buyat.ppg.com/EHSDocumentManagerPublic/documentSearchInnerFrame.aspx?NameCondition=BeginsWith&NameValue=&CodeCondition=Contains&CodeValue={i}&CompCondition=Contains&CompValue=&Form=5a6203a3352c2bce0000&SortBy=ProductName&Language=es-MX&SBU=&From=&To=&SuppressSearchControls=False&AlwaysShowSearchResults=False&PageSize=20&FolderID1=0&FolderID2=0&FolderID3=0&FolderID4=0&FolderID5=0&FolderID6=0&FolderID7=0&FolderID8=0&FolderID9=0&FolderID10=0&SearchAllPublicFolders=True"
        
        list_of_products.append(base)
        
    return list_of_products
    
msds_file = msds()
for link in msds_file:
    webbrowser.open(link)



