from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == "POST":
        file_html_data = open('./data_html.txt', "w")
        # file_simple_data = open('./simple_data.txt', "w")
        data_html = request.form.get('data_html')
        # data_simple = request.form.get('data_simple')
        file_html_data.write(data_html)
        # file_simple_data.write(data_simple)
        file_html_data.close()
        # file_simple_data.close()
        print("Updated!")
        return("Updated!")
    
    if request.method == 'GET':
        return Fat Bitches


if __name__ == "__main__":
    app.run()

