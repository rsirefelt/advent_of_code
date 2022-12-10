import pandas as elf_panda

df_elf = elf_panda.read_excel(r'C:\Users\Tovea\PycharmProjects\AdventOfCode\ElfInput4.xlsx')
df_elf['E1Numb1'] = df_elf.elf1.str.extract('(\d+)').astype(int)
df_elf['E1Numb2'] = df_elf.elf1.str.extract('(-\d+)').astype(int)*-1
df_elf['E2Numb1'] = df_elf.elf2.str.extract('(\d+)').astype(int)
df_elf['E2Numb2'] = df_elf.elf2.str.extract('(-\d+)').astype(int)*-1
df_elf.loc[(df_elf['E1Numb1'] >= df_elf['E2Numb1']) & (df_elf['E1Numb2'] <= df_elf['E2Numb2']), 'contains_the_other'] = True
df_elf.loc[(df_elf['E2Numb1'] >= df_elf['E1Numb1']) & (df_elf['E2Numb2'] <= df_elf['E1Numb2']), 'contains_the_other'] = True

print(df_elf['contains_the_other'].sum())
