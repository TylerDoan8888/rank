# program.py
import sys

# Đường dẫn đến file txt
FILE_PATH = "results.txt"

try:
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
except FileNotFoundError:
    print(f"❌ Không tìm thấy file: {FILE_PATH}")
    print("Vui lòng tạo file results.txt cùng thư mục và thử lại.")
    sys.exit()

# Lấy tất cả các dòng hợp lệ
matches = [line.strip() for line in lines if line.strip()]

if not matches:
    print("❌ File results.txt trống!")
    sys.exit()

# Từ điển lưu thông tin các đội
teams = {}

# Xử lý tất cả các trận
for match in matches:
    parts = match.split()
    if len(parts) != 4:
        print(f"⚠️ Dòng không hợp lệ (bỏ qua): {match}")
        continue
    
    team1 = parts[0]
    score1 = int(parts[1])
    score2 = int(parts[2])
    team2 = parts[3]
    
    # Khởi tạo đội nếu chưa tồn tại
    for team in [team1, team2]:
        if team not in teams:
            teams[team] = {'points': 0, 'pf': 0, 'pa': 0, 'wins': 0, 'losses': 0}
    
    # Cập nhật điểm số
    teams[team1]['pf'] += score1
    teams[team1]['pa'] += score2
    teams[team2]['pf'] += score2
    teams[team2]['pa'] += score1
    
    # Tính thắng thua (1 điểm cho thắng)
    if score1 > score2:
        teams[team1]['wins'] += 1
        teams[team1]['points'] += 1
        teams[team2]['losses'] += 1
    else:
        teams[team2]['wins'] += 1
        teams[team2]['points'] += 1
        teams[team1]['losses'] += 1

# In bảng xếp hạng
print("BẢNG XẾP HẠNG (tất cả các trận)\n")
print(f"{'Đội':<15} {'Trận':<6} {'Thắng':<6} {'Thua':<6} {'Điểm':<6} {'Hiệu số':<8}")
print("-" * 55)

# Sắp xếp theo: Điểm cao nhất → Hiệu số cao nhất
sorted_teams = sorted(teams.items(), 
                     key=lambda x: (x[1]['points'], x[1]['pf'] - x[1]['pa']), 
                     reverse=True)

for team, stats in sorted_teams:
    gd = stats['pf'] - stats['pa']
    matches_played = stats['wins'] + stats['losses']
    print(f"{team:<15} {matches_played:<6} {stats['wins']:<6} {stats['losses']:<6} "
          f"{stats['points']:<6} {gd:+4}")