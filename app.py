from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == "POST":
        url = request.form.get('url')
        prv = request.form.get('prov')
        res = f'Received {prv} data from {url}...'
        with open('data_html.txt', "w") as data_file:
            data_file.write(res)
        with open('data_html.txt', "w") as data_file:
            res2 = data_file.read()
        print(res2)
        return res2
#         file_html_data = open('./data_html.txt', "w")
#         # file_simple_data = open('./simple_data.txt', "w")
#         data_html = request.form.get('data_html')
#         # data_simple = request.form.get('data_simple')
#         file_html_data.write(data_html)
#         # file_simple_data.write(data_simple)
#         file_html_data.close()
#         # file_simple_data.close()
#         print("Updated!")
#         return("Updated!")
    
    if request.method == 'GET':
        return 'Receiving end'


if __name__ == "__main__":
    app.run()

