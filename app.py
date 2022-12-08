import openai
from flask import Flask

app = Flask(__name__)

# URLとメソッドの指定
@app.route("/", methods=["GET"])
def get_articles():
    # APIキーを設定
    openai.api_key = "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"

    # GPT-3を使用するためのエンドポイントを指定
    prompt = "女子大学生のインターン生がしてそうなことを20個教えて"
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=2,
        temperature=0.5,
    )

    # 生成された文章を表示
    print(completions.choices[0].text)

if __name__ == '__main__':
    app.debug = True
    app.run(debug=False, host='0.0.0.0', port=8080)


