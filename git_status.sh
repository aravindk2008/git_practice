echo "---git repository statistics--"
echo "1.total number of commits:"
git rev-list --count HEAD
echo "2.number of commits per author"
git log --format=%an | sort | uniq -c | sort -rn
echo "3.the recently modified files"
git log --name-only --format="" | grep -v '^$' | awk '!seen[$0]++' | head -3 
echo "4.the file that has been changed in the  most commits"
git log --diff-filter=M --name-only --format="" | grep -v '^$'| sort | uniq -c | sort -rn | head -1
