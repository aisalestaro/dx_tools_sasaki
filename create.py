from db_config import User, DXTool

"""
# Userにデータを追加
users_data = [
    {"id": 1, "Company_Name": "株式会社マツリカ", "Department": "営業", "name": "佐々木　優希", "email_address": "yuki.sasaki@mazrica.com", "telephone_number": "09012345678"},
    {"id": 2, "Company_Name": "株式会社リモライフ", "Department": "営業", "name": "佐々木　千代子", "email_address": "zituyuu777@gmail.com", "telephone_number": "09012345679"},
    {"id": 3, "Company_Name": "株式会社ABC", "Department": "営業", "name": "佐藤　千鶴", "email_address": "tiduru@gmail.com", "telephone_number": "09012345670"}
]

for data in users_data:
    User.get_or_create(id=data['id'], defaults=data)  # 既存のデータがあれば更新、なければ作成
"""


"""    
tools_data = [
    {"tool_id":1, "tool_name": "Tableau", "tool_attribute": "経営企画", "tool_url": "https://www.tableau.com/ja-jp"},
    {"tool_id":2, "tool_name": "Microsoft Power BI", "tool_attribute": "経営企画", "tool_url": "https://powerbi.microsoft.com/ja-jp/"},
    {"tool_id":3, "tool_name": "Looker Studio", "tool_attribute": "経営企画", "tool_url": "https://cloud.google.com/looker-studio?hl=ja"},
    {"tool_id":4, "tool_name": "HubSpot", "tool_attribute": "マーケティング", "tool_url": "https://www.hubspot.jp/"},
    {"tool_id":5, "tool_name": "Marketo", "tool_attribute": "マーケティング", "tool_url": "https://business.adobe.com/jp/products/marketo/adobe-marketo.html"},
    {"tool_id":6, "tool_name": "Marketing Cloud Account Engagement", "tool_attribute": "マーケティング", "tool_url": "https://www.salesforce.com/jp/products/marketing-cloud/marketing-automation/"},
    {"tool_id":7, "tool_name": "Sales Cloud", "tool_attribute": "営業", "tool_url": "https://www.salesforce.com/jp/products/sales-cloud/overview/"},
    {"tool_id":8, "tool_name": "Mazrica Sales", "tool_attribute": "営業", "tool_url": "https://product-senses.mazrica.com/"},
    {"tool_id":9, "tool_name": "Zoho CRM", "tool_attribute": "営業", "tool_url": "https://www.zoho.com/jp/crm/"},
    {"tool_id":10,"tool_name": "楽楽販売", "tool_attribute": "販売", "tool_url": "https://www.rakurakuhanbai.jp/"},
    {"tool_id":11,"tool_name": "board", "tool_attribute": "販売", "tool_url": "https://the-board.jp/"},
    {"tool_id":12,"tool_name": "アラジン・オフィス", "tool_attribute": "販売", "tool_url": "https://aladdin-office.com/"},
    {"tool_id":13,"tool_name": "カオナビ", "tool_attribute": "人事", "tool_url": "https://www.kaonavi.jp/"},
    {"tool_id":14,"tool_name": "あしたのチーム", "tool_attribute": "人事", "tool_url": "https://www.ashita-team.com/"},
    {"tool_id":15,"tool_name": "Sharin", "tool_attribute": "人事", "tool_url": "https://sharin.co.jp/"},
    {"tool_id":16,"tool_name": "freee", "tool_attribute": "経理", "tool_url": "https://www.freee.co.jp/"},
    {"tool_id":17,"tool_name": "Money Forward", "tool_attribute": "経理", "tool_url": "https://biz.moneyforward.com/expense/"},
    {"tool_id":18,"tool_name": "楽楽精算", "tool_attribute": "経理", "tool_url": "https://www.rakurakuseisan.jp/"},
    {"tool_id":19,"tool_name": "クラウドサイン", "tool_attribute": "事務", "tool_url": "https://www.cloudsign.jp/"},
    {"tool_id":20,"tool_name": "ドキュサイン", "tool_attribute": "事務", "tool_url": "https://www.docusign.jp/products/electronic-signature"},
    {"tool_id":21,"tool_name": "NINJA SIGN", "tool_attribute": "事務", "tool_url": "https://ninja-sign.com/"},
    {"tool_id":22,"tool_name": "ToDoist", "tool_attribute": "開発・情報システム", "tool_url": "https://todoist.com/ja/home"},
    {"tool_id":23,"tool_name": "Jira", "tool_attribute": "開発・情報システム", "tool_url": "https://www.atlassian.com/ja/software/jira"},
    {"tool_id":24,"tool_name": "Trello", "tool_attribute": "開発・情報システム", "tool_url": "https://trello.com/"},
    {"tool_id":25,"tool_name": "Google Workspace", "tool_attribute": "その他", "tool_url": "https://gsuite.google.co.jp/intl/ja/features/"},
    {"tool_id":26,"tool_name": "Microsoft 365", "tool_attribute": "その他", "tool_url": "https://www.microsoft.com/ja-jp/microsoft-365/business"},
    {"tool_id":27,"tool_name": "サイボウズ ガルーン", "tool_attribute": "その他", "tool_url": "https://garoon.cybozu.co.jp/"}
]

for data in tools_data:
    DXTool.get_or_create(tool_id=data['tool_id'], defaults=data)  # 既存のデータがあれば更新、なければ作成
"""
