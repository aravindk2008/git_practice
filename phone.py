#!/usr/bin/env python3
import json,csv,re
def load():
    try:
        with open("contacts.json","r") as f:
            return json.load(f)
    except:
        return []

def save(cs):
    try:
        with open("contacts.json","w") as f:
            json.dump(cs,f,indent=2)
    except:
        print("Save error")

def valid(ph):
    return re.match(r"^[0-9]{10}$",ph)

def add(cs):
    try:
        n=input("Name: ")
        ph=input("Phone: ")
        e=input("Email: ")

        if not valid(ph):
            print("Invalid phone")
            return

        c={"name":n,"phone":ph,"email":e}
        cs.append(c)
        print("Added")
    except:
        print("Add error")

def search(cs):
    try:
        q=input("Search: ").lower()
        found=False

        for c in cs:
            if q in c["name"].lower():
                print(c)
                found=True

        if not found:
            print("No match")
    except:
        print("Search error")

def edit(cs):
    try:
        n=input("Name to edit: ")

        for c in cs:
            if c["name"].lower()==n.lower():
                ph=input("New phone: ")
                e=input("New email: ")

                if not valid(ph):
                    print("Invalid phone")
                    return

                c["phone"]=ph
                c["email"]=e
                print("Updated")
                return

        print("Not found")
    except:
        print("Edit error")

def delete(cs):
    try:
        n=input("Name to delete: ")

        for c in cs:
            if c["name"].lower()==n.lower():
                cs.remove(c)
                print("Deleted")
                return

        print("Not found")
    except:
        print("Delete error")

def show(cs):
    try:
        s=sorted(cs,key=lambda x:x["name"].lower())
        for c in s:
            print(c)
    except:
        print("List error")

def export(cs):
    try:
        with open("contacts.csv","w",newline="") as f:
            w=csv.DictWriter(f,fieldnames=["name","phone","email"])
            w.writeheader()
            w.writerows(cs)
        print("Exported")
    except:
        print("Export error")
cs=load()
while True:
    print("\n1.Add")
    print("2.Search")
    print("3.Edit")
    print("4.Delete")
    print("5.List")
    print("6.Export")
    print("7.Exit")
    ch=input("Choice: ")
    if ch=="1":
        add(cs)
    elif ch=="2":
        search(cs)
    elif ch=="3":
        edit(cs)
    elif ch=="4":
        delete(cs)
    elif ch=="5":
        show(cs)
    elif ch=="6":
        export(cs)
    elif ch=="7":
        save(cs)
        print("Saved")
        break
    else:
        print("Invalid")
