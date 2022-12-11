import pandas as elf_panda

df_elf = elf_panda.read_excel(r'C:\Users\Tovea\PycharmProjects\AdventOfCode\ElfInput5.xlsx', sheet_name='Procedure')
df_elf2 = elf_panda.read_excel(r'C:\Users\Tovea\PycharmProjects\AdventOfCode\ElfInput5.xlsx', sheet_name='Crates')
crate_dict = {}
for (colname,colval) in df_elf2.iteritems():
    crate_dict[colname] = colval.tolist()[::-1]
for index, row in df_elf.iterrows():
    crate_dict[row.To] = crate_dict[row.To] + crate_dict[row.From][-row.Move:][::-1]
    # crate_dict[row.To] = crate_dict[row.To] + crate_dict[row.From][-row.Move:] #Part 2
    crate_dict[row.From] = crate_dict[row.From][:-row.Move]
print(crate_dict)


