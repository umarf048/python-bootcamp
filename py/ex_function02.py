def kira_jumlah_markah(*args):
    return sum(args)



kuiz_sains = kira_jumlah_markah(80, 90, 75)
kuiz_sejarah = kira_jumlah_markah(60, 85, 70, 95, 80)

print(f"Jumlah markah sains: {kuiz_sains}")
print(f"Jumlah markah sejarah: {kuiz_sejarah}")