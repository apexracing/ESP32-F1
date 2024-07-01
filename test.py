import requests

if __name__ == "__main__":
    response=requests.get("https://gitee.com/apexracing/f1livetime/raw/master//f1_2024.json")
    data=response.json()
    response.close()
    for key in data.keys():
        print(key)

