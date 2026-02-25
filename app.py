from flask import Flask, render_template, request

try:
    import language_tool_python
except ModuleNotFoundError:  # 初回セットアップ前でも原因がわかるようにする
    language_tool_python = None

app = Flask(__name__)


def score_sentence(issue_count: int) -> int:
    """Start from 100 and subtract 7 points per issue."""
    return max(0, 100 - issue_count * 7)


def score_label(score: int) -> str:
    if score >= 90:
        return "Excellent"
    if score >= 75:
        return "Good"
    if score >= 60:
        return "Keep going"
    return "Needs review"


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error_message = None

    if language_tool_python is None:
        error_message = (
            "必要ライブラリが未インストールです。READMEの手順どおりに "
            "`pip install -r requirements.txt` を実行してください。"
        )
        return render_template('index.html', result=result, error_message=error_message)

    if request.method == 'POST':
        text = request.form.get('english_text', '').strip()

        if not text:
            error_message = '英文を入力してから「チェックする」を押してください。'
            return render_template('index.html', result=result, error_message=error_message)

        try:
            tool = language_tool_python.LanguageTool('en-US')
            matches = tool.check(text)
            corrected = language_tool_python.utils.correct(text, matches)
        except Exception:
            error_message = (
                '文法チェックエンジンの起動に失敗しました。'
                'ネットワーク接続を確認して再実行してください。'
            )
            return render_template('index.html', result=result, error_message=error_message)

        issues = []
        for match in matches:
            issues.append(
                {
                    'message': match.message,
                    'rule': match.ruleIssueType,
                    'context': match.context,
                    'suggestions': match.replacements[:3],
                }
            )

        score = score_sentence(len(matches))
        result = {
            'original': text,
            'corrected': corrected,
            'issues': issues,
            'score': score,
            'label': score_label(score),
        }

    return render_template('index.html', result=result, error_message=error_message)


if __name__ == '__main__':
    app.run(debug=True)
