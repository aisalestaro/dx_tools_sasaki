
from db_config import User, DXTool

# 質問リストと選択肢
questions = [
    {
        "question": "DX化に関心のある業務範囲は？（１つのみ選択）",
        "choices": ["経営企画", "マーケティング", "営業", "販売", "人事", "経理", "事務", "開発・情報システム", "その他"],
        "multiple": False
    },
    {
        "question": "業界は？（１つのみ選択）",
        "choices": ["建設・工事", "不動産", "医療・福祉", "小売・卸売", "サービス", "製造", "農林水産", "IT・インターネット", "飲食", "運輸・物流", "コンサルティング", "士業", "人材紹介・人材派遣", "金融", "広告・メディア", "美容・サロン", "旅行・レジャー", "教育・学習支援", "公務員", "その他・近いものはない"],
        "multiple": False
    },
    {
        "question": "すでに実現完了していること（複数選択可能）",
        "choices": ["メール/カレンダーツールの導入", "エクセル/スプレッドシートの導入", "HP作成", "WEB会議ツールの導入", "チャットツールの導入", "基幹システムの構築・導入", "ワークフローのデジタル化", "RPA/マクロなどによる業務自動化", "経理・会計システムの導入", "人事・労務システムの導入", "ペーパーレス化", "顧客データの一元管理", "マーケティングツールの導入", "営業支援ツールの導入", "データ経営の実現", "リモートワークの導入", "BIツールの導入", "AIの導入"],
        "multiple": True
    },
    {
        "question": "優先順位高く、実現したいこと（複数選択可能）",
        "choices": ["メール/カレンダーツールの導入", "エクセル/スプレッドシートの導入", "HP作成", "WEB会議ツールの導入", "社内チャットツールの導入", "基幹システムの構築・導入", "ワークフローのデジタル化", "RPA/マクロなどによる業務自動化", "経理・会計システムの導入", "人事・労務システムの導入", "ペーパーレス化", "顧客データの一元管理", "マーケティングツールの導入", "営業支援ツールの導入", "データ経営の実現", "リモートワークの導入", "BIツールの導入", "AIの導入"],
        "multiple": True
    },
    {
        "question": "従業員数（１つのみ選択）",
        "choices": ["1", "2-4", "5-10", "11-30", "31-50", "51-100", "101-200", "201-300", "300-500", "500-1,000", "1001-2,000", "2,001-3,000", "3,001〜"],
        "multiple": False
    },
{
        "question": "役職（１つのみ選択）",
        "choices": ["代表取締役", "取締役", "執行役員相当", "部長相当", "課長相当", "一般社員・その他"],
        "multiple": False
    },
    {
        "question": "御社の受注スタイルは？（１つのみ選択）",
        "choices": ["既存顧客からの受注が多い", "新規開拓からの受注が多い"],
        "multiple": False
    },
    {
        "question": "御社の顧客は？（１つのみ選択）",
        "choices": ["B to B（法人顧客）が多い", "B to C（一般消費者）が多い"],
        "multiple": False
    }
]

# ユーザーの回答を保存する辞書
user_answers = {}

# 質問を出題して回答を保存
for q in questions:
    print(q["question"])
    for i, choice in enumerate(q["choices"]):
        print(f"{i + 1}. {choice}")
    answer_index = int(input("回答: ")) - 1  # 1から始まる選択肢を0から始まるインデックスに変換
    user_answers[q["question"]] = q["choices"][answer_index]  # 選択肢のテキストを保存

# ユーザー情報を登録
user_info = {}
# IDは自動採番されるので入力は不要
user_info["Company_Name"] = input("会社名: ")
user_info["Department"] = input("部署: ")
user_info["name"] = input("名前: ")
user_info["email_address"] = input("メールアドレス: ")
user_info["telephone_number"] = input("電話番号: ")

# データベースにユーザー情報を保存
user_record = User.create(**user_info)

# DX指標を計算（仮に質問3の回答が5だとする）
# ここでは質問3の回答を取得して計算
dx_score = len(user_answers.get("すでに実現完了していること（複数選択可能）", "").split(',')) * 5
print(f"御社のDX指標：{dx_score}点 / 100点")

# おすすめのDXツールを提示
# ここでは質問1の回答を取得してマッチング
recommended_tools = DXTool.select().where(DXTool.tool_attribute == user_answers.get("DX化に関心のある業務範囲は？（１つのみ選択）"))
if recommended_tools.exists():
    print("御社におすすめのDXツールは以下の通りです。")
    for tool in recommended_tools:
        print(f"{tool.tool_name} - {tool.tool_url}")
else:
    print("マッチするDXツールは見つかりませんでした。")
