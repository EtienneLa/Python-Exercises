from urllib import request

samp_url = "http://insight.dev.schoolwires.com/HelpAssets/C2Assets/C2Files/C2ImportCalEventSample.csv"

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r"samp.csv"
    fw = open(dest_url, "w")
    for line in lines:
        fw.write(line + "\n")
    fw.close()


download_stock_data(samp_url)
