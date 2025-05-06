import gdown

url="https://drive.google.com/uc?id=1BEf7YBAgjJKNNccwhECap6o5RXSKaSXk"
output= "modsS.zip"

if __name__ == "__main__":
  gdown.download(url, output=output)
