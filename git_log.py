#!/usr/bin/env python3
import os
import zlib

def read_object(obj_hash):
    path = os.path.join(".git/objects", obj_hash[:2], obj_hash[2:])
    with open(path, "rb") as f:
        data = f.read()
    return zlib.decompress(data)

def parse_commit(data):
    text = data.decode(errors="ignore")
    header, message = text.split("\x00", 1)
    lines = message.split("\n")
    commit = {
        "tree": "",
        "parent": None,
        "author": "",
        "message": ""
    }
    msg_started = False
    msg_lines = []
    for line in lines:
        if not msg_started:
            if line.startswith("tree "):
                commit["tree"] = line.split()[1]
            elif line.startswith("parent "):
                commit["parent"] = line.split()[1]
            elif line.startswith("author "):
                commit["author"] = line[7:]
            elif line == "":
                msg_started = True
        else:
            msg_lines.append(line)
    commit["message"] = "\n".join(msg_lines).strip()
    return commit

def find_head():
    with open(".git/HEAD", "r") as f:
        ref = f.read().strip()
    if ref.startswith("ref:"):
        ref_path = ".git/" + ref.split(" ")[1]
        with open(ref_path, "r") as f:
            return f.read().strip()
    return ref

def git_log():
    commit_hash = find_head()
    while commit_hash:
        data = read_object(commit_hash)
        commit = parse_commit(data)
        print(commit_hash[:7], commit["message"].split("\n")[0])
        commit_hash = commit["parent"]

if __name__ == "__main__":
    git_log()
