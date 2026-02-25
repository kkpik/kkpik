# 英文チェッカー（初心者向け / Windows版）

英文を入力すると、以下を表示するシンプルな Web アプリです。

- 文法チェック
- 修正例
- 解説（指摘内容）
- 点数（100点満点）

---

## まず最初に：Windowsでの最短手順（このままコピペOK）

> ここだけ実行すれば、とりあえず起動できます。  
> **PowerShell** を開いて、1行ずつ実行してください。

```powershell
cd C:\Users\あなたのユーザー名\Desktop\kkpik
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

起動できたらブラウザで次を開きます：

- `http://127.0.0.1:5000`

終了するときは、PowerShell で `Ctrl + C` を押してください。

---

## 1. 事前準備（Windows）

### 1-1. Python をインストール

1. 公式サイト（https://www.python.org/downloads/windows/）からインストール
2. インストール画面で **Add Python to PATH** にチェック
3. インストール完了後、PowerShell を開いて確認

```powershell
python --version
```

または：

```powershell
py --version
```

バージョン（例: `Python 3.11.x`）が表示されればOKです。

---

## 2. プロジェクトを開く

`kkpik` フォルダに移動します（場所は自分の保存先に合わせて変更）。

```powershell
cd C:\Users\あなたのユーザー名\Desktop\kkpik
```

`README.md` や `app.py` が見えれば正しい場所です。

```powershell
dir
```

---

## 3. 仮想環境を作成して有効化

### 3-1. 仮想環境の作成

```powershell
py -m venv .venv
```

### 3-2. 仮想環境の有効化

```powershell
.\.venv\Scripts\Activate.ps1
```

成功すると、行の先頭に `(.venv)` が表示されます。

---

## 4. ライブラリをインストール

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## 5. アプリを起動

```powershell
python app.py
```

次の表示が出れば成功です：

```text
 * Running on http://127.0.0.1:5000
```

ブラウザで `http://127.0.0.1:5000` を開いてください。

---

## 6. 使い方

1. テキスト欄に英文を入力
2. 「チェックする」を押す
3. 点数・修正例・解説を確認

---

## 7. よくあるエラー（Windows）

### A. `'.\\.venv\\Scripts\\Activate.ps1' は実行できません` と出る

PowerShell の実行ポリシーが原因です。次を実行してから、再度有効化してください。

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

その後：

```powershell
.\.venv\Scripts\Activate.ps1
```

---

### B. `No module named flask` または `No module named language_tool_python`

仮想環境が有効でない可能性があります。以下をやり直してください。

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

---

### C. `Address already in use`（ポート競合）

`app.py` の最後を次のように変更します。

```python
app.run(debug=True, port=5001)
```

起動後は `http://127.0.0.1:5001` を開いてください。

---

## 8. 授業で使うときのコツ

- まず「わざとミスした例文」を入力して、生徒に修正理由を考えさせる
- 次に正しい文を入力して、スコアの違いを比較する
- 「なぜその候補になるか」を日本語で説明させる

---

## 9. ファイル構成

```text
kkpik/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```
