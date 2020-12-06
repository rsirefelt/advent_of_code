with open("input.txt", "r") as f:
    all_ans = f.read().split("\n\n")

anyone_count = 0
everyone_count = 0
for grp_ans in all_ans:
    grp_ans = grp_ans.split("\n")
    unq_set, comb_set = set(), set(grp_ans[0])
    for ans in grp_ans:
        unq_set |= set(ans)
        comb_set &= set(ans)
    anyone_count += len(unq_set)
    everyone_count += len(comb_set)

print(f"1) Anyone answered yes count: {anyone_count}")
print(f"2) Everyone answered yes count: {everyone_count}")
