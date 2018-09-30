# dl4us_final
dl4usの最終レポート生成物

- 実施したこと
  - アイマスSSまとめサイトからスクレイピングしたデータを元にチャットボットを作成

- scrape_txt.py
  - まとめサイトからSSをスクレイピング

- preprocess.py
  - スクレイピングした本文データからseq2seqに入力できるよう発話文と回答文を生成

- chatbot.ipynb
  - seq2seqモデルの学習、出力結果の確認
