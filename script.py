import os

def test():
    file_name = "index.html"
    print(f"Memulakan semakan pada: {file_name}")

    # Menyemak jika fail index.html wujud dalam folder
    if os.path.exists(file_name):
        print("PENGESAHAN: Fail index.html ditemui.")
    else:
        print("RALAT: Fail index.html tidak dijumpai!")
        exit(1)

    # Menyemak jika fungsi alert() telah ditulis dalam kod
    with open(file_name, "r") as f:
        kandungan = f.read()
        if "alert(" in kandungan:
            print("PENGESAHAN: Fungsi alert dikesan dalam kod.")
        else:
            print("RALAT: Fungsi alert tidak dijumpai!")
            exit(1)

if __name__ == "__main__":
    test()
