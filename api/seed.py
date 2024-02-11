from sqlalchemy.orm import sessionmaker
import api.models.models as models


def insert_seed_data(session):
    """Insert seed data into the database."""

    # plans
    plan1 = models.Plan(
        title="気になってた女の子とうまく行ったプランです！",
        description="お店の雰囲気や立地、料理の美味しさなど、全てが最高でした！彼女へのサプライズにも協力してくれてとても良いお店でした。帰り道のイルミネーションも良かったです！",
        budget=15000,
        situation="告白するつもりで臨んだデート！",
        with_whom="意中の女の子",
    )
    plan2 = models.Plan(
        title="マンネリ化していたデートプランも、ここで新しい発見がありました！",
        description="いつも居酒屋とバーばかりでしたが、ここで新しい発見がありました！創作料理やお酒の紹介もあり、とても楽しい時間を過ごせました！",
        budget=10000,
        situation="彼氏とのデート",
        with_whom="彼ピッピ",
    )
    plan3 = models.Plan(
        title="後輩女子に大好評",
        description="大学の後輩の女の子と行きました。美味しい焼肉とお酒で盛り上がりました！",
        budget=13000,
        situation="後輩女子との飲み会",
        with_whom="後輩",
    )
    plan4 = models.Plan(
        title="自然を満喫！癒しのピクニックデート",
        description="都会の喧騒を離れ、自然豊かな公園でピクニックをしました。手作りのサンドイッチとフルーツ、そして緑に囲まれた静かな時間は最高でした。彼女もとても喜んでくれて、記憶に残る一日になりました。",
        budget=5000,
        situation="休日のリラックスしたデート",
        with_whom="彼女",
    )
    plan5 = models.Plan(
        title="アドベンチャー好きにおすすめ！スリリングなアクティビティデート",
        description="この日はアドベンチャーパークで過ごしました。ツリークライミングやジップラインなど、スリル満点のアクティビティを楽しみました。二人の絆も深まり、アクティブなデートを求めるカップルにぴったりです。",
        budget=20000,
        situation="アクティブなデート",
        with_whom="冒険好きな彼氏",
    )
    plan6 = models.Plan(
        title="文化的な一日を過ごすアート鑑賞デート",
        description="",
        budget=10000,
        situation="静かで落ち着いたデート",
        with_whom="アートが好きな彼女",
    )
    # places
    place1_1 = models.Place(url="https://www.hotpepper.jp/strJ000717028/", plan_id=1)
    place1_2 = models.Place(url="https://www.hotpepper.jp/strJ001249521/", plan_id=1)
    place2_1 = models.Place(url="https://www.hotpepper.jp/strJ003341342/", plan_id=2)
    place3_1 = models.Place(url="https://www.hotpepper.jp/strJ000717028/", plan_id=3)
    place4_1 = models.Place(url="https://www.hotpepper.jp/strJ000717028/", plan_id=4)
    place5_1 = models.Place(url="https://www.hotpepper.jp/strJ000717028/", plan_id=5)
    place6_1 = models.Place(url="https://www.hotpepper.jp/strJ000717028/", plan_id=6)
    place6_2 = models.Place(url="https://www.hotpepper.jp/strJ001249521/", plan_id=6)
    place6_3 = models.Place(url="https://www.hotpepper.jp/strJ003341342/", plan_id=6)
    place6_4 = models.Place(url="https://www.hotpepper.jp/strJ000717028/", plan_id=6)

    # comments
    comment1_1 = models.Comment(
        comment="参考になりました！自分も真似してみます！",
        stars=5,
        plan_id=1,
    )
    comment1_2 = models.Comment(
        comment="自分にはない視点でした！",
        stars=3,
        plan_id=1,
    )
    comment2_1 = models.Comment(
        comment="え〜こんな店あるんですね!彼氏といっってみます！",
        stars=3,
        plan_id=2,
    )
    comment3_1 = models.Comment(
        comment="参考になりました！自分も真似してみます！",
        stars=5,
        plan_id=3,
    )
    comment4_1 = models.Comment(
        comment="彼女ができました！",
        stars=4,
        plan_id=4,
    )
    comment5_1 = models.Comment(
        comment="彼氏ができました！",
        stars=3,
        plan_id=5,
    )
    comment5_2 = models.Comment(
        comment="マンネリ解消！",
        stars=5,
        plan_id=5,
    )

    session.add(plan1)
    session.add(plan2)
    session.add(plan3)
    session.add(plan4)
    session.add(plan5)
    session.add(plan6)
    session.add(place1_1)
    session.add(place1_2)
    session.add(place2_1)
    session.add(place3_1)
    session.add(place4_1)
    session.add(place5_1)
    session.add(place6_1)
    session.add(place6_2)
    session.add(place6_3)
    session.add(place6_4)
    session.add(comment1_1)
    session.add(comment1_2)
    session.add(comment2_1)
    session.add(comment3_1)
    session.add(comment4_1)
    session.add(comment5_1)
    session.add(comment5_2)

    session.commit()
    session.close()
