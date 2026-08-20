import hashlib

def get_hash(data, algorithm):
    if algorithm == "md5":
        return hashlib.md5(data.encode()).hexdigest()
    elif algorithm == "sha1":
        return hashlib.sha1(data.encode()).hexdigest()
    elif algorithm == "sha256":
        return hashlib.sha256(data.encode()).hexdigest()
    elif algorithm == "sha512":
        return hashlib.sha512(data.encode()).hexdigest()
    else:
        return None

def main():
    print("=== Hasher ===")
    print("Available algorithms: md5, sha1, sha256, sha512")
    while True:
        subMain()
        again = input("Again? (y/n): ")
        if again.lower() != "y":
            break

def subMain():
    data = input("Enter a string: ")
    algorithm = input("Select Algorithm: ")

    result = get_hash(data, algorithm)

    if result:
        print(f"Hash ({algorithm}): {result}")
    else:
        print("Unknown algorithm")

if __name__ == "__main__":
    main()
