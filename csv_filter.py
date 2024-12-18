import csv

input_file = 'cicddos2019_dataset.csv'  # 替換為你的 CSV 文件路徑
output_file = 'preprocessed_data_UDP_attack.csv'  # 輸出的 CSV 文件名
target_column_1 = 'Label'  # 替換為要查詢的欄位名稱
target_column_2 = 'Class'
filter_value_1 = 'UDP'  # 替換為過濾條件
filter_value_2 = 'Attack'
filter_value_3 = 'Benign'
# 指定要保留的欄位
selected_fields = ['Label', 'Class', 'Flow Packets/s','Flow Bytes/s','Fwd Packets/s','Flow Duration']  # 根據需求添加所需的欄位名稱

# 打開輸入和輸出文件
with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
        open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    reader = csv.DictReader(infile)  # 讀取 CSV 文件，使用列名來查找欄位
    writer = csv.DictWriter(outfile, fieldnames=selected_fields)

    writer.writeheader()  # 寫入表頭

    # 過濾和寫入符合條件的行，只寫入所需欄位
    for row in reader:
        if row[target_column_1] == filter_value_1:
            filtered_row = {field: row[field] for field in selected_fields}  # 只保留指定欄位
            writer.writerow(filtered_row)  # 寫入符合條件的行

print(f'Filtering complete. Results written to {output_file}')
