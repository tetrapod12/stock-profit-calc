# stock-profit-calc

株の売買利益を自動で計算するシンプルなCLIツールです。

## 特長

* CSV形式の取引履歴ファイルを読み込み、FIFO方式で銘柄別・合計損益を計算
* ドル（\$）表記による結果表示
* 依存パッケージなしで動作可能

## 前提条件

* Python 3.10 以上がインストールされていること
* （推奨）仮想環境（venv）を利用すること

## インストール手順

1. リポジトリをクローンまたはダウンロード

   ```bash
   git clone https://github.com/<YOUR_GITHUB_USERNAME>/stock-profit-calc.git
   cd stock-profit-calc
   ```
2. 仮想環境を作成・有効化

   * macOS/Linux

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   * Windows PowerShell

     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
3. 依存パッケージのインストール（不要であればスキップ）

   ```bash
   pip install -r requirements.txt
   ```

## 使い方

1. 取引履歴を `transactions.csv` としてプロジェクトルートに配置
2. 以下コマンドを実行

   ```bash
   python calc.py transactions.csv
   ```
3. 銘柄別と合計の損益がターミナルに表示されます

## CSVフォーマット例

```csv
# date,symbol,type,quantity,price,fee
2025-06-01,SOXL,buy,10,15.70,0.5
2025-06-05,SOXL,sell,5,17.50,0.5
```

（必須カラム：`date,symbol,type,quantity,price,fee`）

## 拡張アイデア

* 複数銘柄フィルタリングオプション
* 期間指定、レポート出力（CSV/JSON）
* 平均原価法やLIFOへの対応
* Web UI化（Streamlit/Flask）

## ライセンス

MIT License
