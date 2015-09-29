from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Make, Base, Model, Specs
import json

engine = create_engine('sqlite:///Car.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

car_1 = Make(company="BMW",
             logo="""http://blog.logomyway.com/wp-content/uploads/2013/05/bmw-logo.jpg""")
session.add(car_1)
session.commit()

car_2 = Make(company="Tesla",
             logo="""http://www.autoblog.com/img/logos/makes/tesla.png""")
session.add(car_2)
session.commit()

car_3 = Make(company="Nissan",
             logo="""http://vignette4.wikia.nocookie.net/worldofcarsdrivein/images/9/90/Nissan-logo-loan.gif/revision/latest?cb=20120320145453""")
session.add(car_3)
session.commit()

car_4 = Make(company="Lexus",
             logo="""http://www.car-brand-names.com/wp-content/uploads/2015/05/Lexus-logo-3.png""")
session.add(car_4)
session.commit()

car_5 = Make(company="Mercedes-Benz",
             logo="""http://www.logodesignlove.com/images/evolution/mercedes-benz-logo-design.jpg""")
session.add(car_5)
session.commit()

car_6 = Make(company="Toyota",
             logo="""http://d1r57ja1amoclf.cloudfront.net/wp-content/uploads/2014/04/Toyota-Logo.jpg""")
session.add(car_6)
session.commit()

bmw_string = {"results": [
    {
        "make": "bmw",
        "image": "https://s.yimg.com/bt/api/res/1.2/HlQxKZO9MHWQghiDHWI_Yw--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/YLH9MBmAqhRZUG7F4l7FCg--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/7d09afdba0d8553e596ce2832ab4525a",
        "mpg": "23 CITY / 36 HWY",
        "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/HlQxKZO9MHWQghiDHWI_Yw--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/YLH9MBmAqhRZUG7F4l7FCg--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/7d09afdba0d8553e596ce2832ab4525a\" width=\"100%\" alt=\"2016 BMW 2 Series\" data-reactid=\".22a0847x24g.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-0.1.$=11:0.$=10:0.0.$li-carouselItem-0.$carouselItem-0.0.0\" />",
        "price": "$32,850",
        "hp": "240 HP",
        "model": "2 Series",
        "image/_alt": "2016 BMW 2 Series"
    },
    {
        "make": "bmw",
        "image": "https://s.yimg.com/bt/api/res/1.2/BIbs5uGc6o7Hulini1dU4w--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/z4uEWCkCndyygM.VlRtJAQ--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/ed077713bf534e79d4d6d11531da6d0d",
        "mpg": "20 CITY / 31 HWY",
        "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/BIbs5uGc6o7Hulini1dU4w--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/z4uEWCkCndyygM.VlRtJAQ--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/ed077713bf534e79d4d6d11531da6d0d\" width=\"100%\" alt=\"2016 BMW 6 Series\" data-reactid=\".22a0847x24g.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-0.1.$=11:0.$=10:0.0.$li-carouselItem-1.$carouselItem-1.0.0\" />",
        "price": "$76,600",
        "hp": "315 HP",
        "model": "6 Series",
        "image/_alt": "BMW 6 Series"
    },
    {
        "make": "bmw",
        "image": "https://s.yimg.com/bt/api/res/1.2/D2vheiRQyStJfEiSNlWRSg--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/nRCtrhTK.QR6k7F9MIakLw--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/483afa406ddbbffcc3072a2f3fccf9eb",
        "mpg": "24 CITY / 36 HWY",
        "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/D2vheiRQyStJfEiSNlWRSg--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/nRCtrhTK.QR6k7F9MIakLw--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/483afa406ddbbffcc3072a2f3fccf9eb\" width=\"100%\" alt=\"2016 BMW 3 Series\" data-reactid=\".22a0847x24g.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-1.1.$=11:0.$=10:0.0.$li-carouselItem-0.$carouselItem-0.0.0\" />",
        "price": "$33,150",
        "hp": "180 HP",
        "model": "3 Series",
        "image/_alt": "2016 BMW 3 Series"
    },
    {
        "make": "bmw",
        "image": "https://s.yimg.com/bt/api/res/1.2/e.dO83HS66WgjSORkG.byQ--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/Yxp5sISHL2yPK6NYp1PIeA--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/c6077721acab695e6bdb5b8ffcaad957",
        "mpg": "23 CITY / 34 HWY",
        "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/e.dO83HS66WgjSORkG.byQ--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/Yxp5sISHL2yPK6NYp1PIeA--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/c6077721acab695e6bdb5b8ffcaad957\" width=\"100%\" alt=\"2016 BMW 4 Series\" data-reactid=\".22a0847x24g.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-1.1.$=11:0.$=10:0.0.$li-carouselItem-1.$carouselItem-1.0.0\" />",
        "price": "$41,650",
        "hp": "240 HP",
        "model": "4 Series",
        "image/_alt": "2016 BMW 4 Series"
    },
    {
        "make": "bmw",
        "image": "https://s.yimg.com/bt/api/res/1.2/sSuX6SC92zKLzI7Z7nV5Zg--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/LeCT1pZmPk_BQkIb6GonPg--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/cf3cbdbd0a6d4ef3ab3704e1a882c400",
        "mpg": "23 CITY / 34 HWY",
        "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/sSuX6SC92zKLzI7Z7nV5Zg--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/LeCT1pZmPk_BQkIb6GonPg--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/cf3cbdbd0a6d4ef3ab3704e1a882c400\" width=\"100%\" alt=\"2016 BMW 5 Series\" data-reactid=\".22a0847x24g.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-1.1.$=11:0.$=10:0.0.$li-carouselItem-2.$carouselItem-2.0.0\" />",
        "price": "$50,200",
        "hp": "240 HP",
        "model": "5 Series",
        "image/_alt": "2016 BMW 5 Series"
    },
    {
        "make": "bmw",
        "image": "https://s.yimg.com/bt/api/res/1.2/CN9uzG35nKJdqzejjl_eCA--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/U8AeYBuZ1W_eSjBo6nvx5w--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/b54d089feb08cc42c370d6ca2d153a2b",
        "mpg": "22 CITY / 34 HWY",
        "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/CN9uzG35nKJdqzejjl_eCA--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/U8AeYBuZ1W_eSjBo6nvx5w--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/b54d089feb08cc42c370d6ca2d153a2b\" width=\"100%\" alt=\"2016 BMW 3 Series Gran Turismo\" data-reactid=\".22a0847x24g.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-2.1.$=11:0.$=10:0.0.$li-carouselItem-0.$carouselItem-0.0.0\" />",
        "price": "$43,000",
        "hp": "240 HP",
        "model": "3 Series Gran Turismo",
        "image/_alt": "2016 BMW 3 Series Gran Turismo"
    },
    {
        "make": "bmw",
        "image": "https://s.yimg.com/bt/api/res/1.2/QJTn6ans0P_N0EOFA2hB3A--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/v3yjLKP3uUwCLRsMkZ9pRw--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/12b1ae72476f97e79a29d0a9efd13897",
        "mpg": "19 CITY / 28 HWY",
        "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/QJTn6ans0P_N0EOFA2hB3A--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/v3yjLKP3uUwCLRsMkZ9pRw--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/12b1ae72476f97e79a29d0a9efd13897\" width=\"100%\" alt=\"2016 BMW 5 Series Gran Turismo\" data-reactid=\".22a0847x24g.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-2.1.$=11:0.$=10:0.0.$li-carouselItem-1.$carouselItem-1.0.0\" />",
        "price": "$60,900",
        "hp": "300 HP",
        "model": "5 Series Gran Turismo",
        "image/_alt": "2016 BMW 5 Series Gran Turismo"
    }
]}

tesla_string = {"results": [
                {
                    "make": "tesla",
                    "image": "https://s.yimg.com/bt/api/res/1.2/IUB.WumJv1U8q_yvq1e9Cw--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/4N.1DyNaKU5E1Uy7YmemOA--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/2f17703231f068441bde149009de104d",
                    "mpg": "N/A CITY / N/A HWY",
                    "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/IUB.WumJv1U8q_yvq1e9Cw--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/4N.1DyNaKU5E1Uy7YmemOA--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/2f17703231f068441bde149009de104d\" width=\"100%\" alt=\"2015 Tesla Model S\" data-reactid=\".5z9x6enxmo.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-0.1.$=11:0.$=10:0.0.$li-carouselItem-0.$carouselItem-0.0.0\" />",
                    "price": "$69,900",
                    "hp": "380 HP",
                    "model": "Model S",
                    "image/_alt": "2015 Tesla Model S"
                }
                ]}

nissan_string = {"results": [
                {
                    "make": "nissan",
                    "image": "https://s.yimg.com/bt/api/res/1.2/wlIU0m.xvS4Cyfcu77iAHA--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/4ORg71ZVid3kp2gX8MJPxw--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/024cd7ffbc94369e96c9176e8a7a2cf1",
                    "mpg": "18 CITY / 26 HWY",
                    "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/wlIU0m.xvS4Cyfcu77iAHA--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/4ORg71ZVid3kp2gX8MJPxw--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/024cd7ffbc94369e96c9176e8a7a2cf1\" width=\"100%\" alt=\"2016 Nissan 370Z\" data-reactid=\".rudjuxophc.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-0.1.$=11:0.$=10:0.0.$li-carouselItem-0.$carouselItem-0.0.0\" />",
                    "price": "$29,990",
                    "hp": "332 HP",
                    "model": "2016 370Z",
                    "image/_alt": "2016 Nissan 370Z"
                },
    {
                    "make": "nissan",
                    "image": "https://s.yimg.com/bt/api/res/1.2/__XXCOcax8wdqJc8mudDHw--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/s0MFrDwFqF36chLTxr2OoA--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/1d5ee3654f438965605a6d163caee111",
                    "mpg": "16 CITY / 22 HWY",
                    "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/__XXCOcax8wdqJc8mudDHw--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/s0MFrDwFqF36chLTxr2OoA--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/1d5ee3654f438965605a6d163caee111\" width=\"100%\" alt=\"2016 Nissan GT-R\" data-reactid=\".rudjuxophc.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-0.1.$=11:0.$=10:0.0.$li-carouselItem-1.$carouselItem-1.0.0\" />",
                    "price": "$101,770",
                    "hp": "545 HP",
                    "model": "2016 GT-R",
                    "image/_alt": "2016 Nissan GT-R"
                },
    {
                    "make": "nissan",
                    "image": "https://s.yimg.com/bt/api/res/1.2/7saE040d2cupGZGwIo1ycA--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/G56040IuUjlb0xmlWoEIxQ--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/cacb7127c41e4fcdab87693f48ac875d",
                    "mpg": "27 CITY / 38 HWY",
                    "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/7saE040d2cupGZGwIo1ycA--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/G56040IuUjlb0xmlWoEIxQ--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/cacb7127c41e4fcdab87693f48ac875d\" width=\"100%\" alt=\"2015 Nissan Altima\" data-reactid=\".rudjuxophc.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-1.1.$=11:0.$=10:0.0.$li-carouselItem-0.$carouselItem-0.0.0\" />",
                    "price": "$22,300",
                    "hp": "182 HP",
                    "model": "Altima",
                    "image/_alt": "2015 Nissan Altima"
                },
    {
                    "make": "nissan",
                    "image": "https://s.yimg.com/bt/api/res/1.2/MTRsuwIHho.fAE4gBv6FIA--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/p08ALnE5OlU7SP7DvOx_Fg--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/47314fd558650483ab257f71510d3936",
                    "mpg": "27 CITY / 36 HWY",
                    "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/MTRsuwIHho.fAE4gBv6FIA--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/p08ALnE5OlU7SP7DvOx_Fg--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/47314fd558650483ab257f71510d3936\" width=\"100%\" alt=\"2016 Nissan Sentra\" data-reactid=\".rudjuxophc.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-1.1.$=11:0.$=10:0.0.$li-carouselItem-2.$carouselItem-2.0.0\" />",
                    "price": "N/A",
                    "hp": "130 HP",
                    "model": "2016 Sentra",
                    "image/_alt": "2016 Nissan Sentra"
                },
    {
                    "make": "nissan",
                    "image": "https://s.yimg.com/bt/api/res/1.2/GtPnVxiA6yx94Mvl792GCw--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/q5HWSjxgUBd6LTGk9gWTig--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/f9e77c446279d65d5729cf8d99819c7d",
                    "mpg": "13 CITY / 19 HWY",
                    "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/GtPnVxiA6yx94Mvl792GCw--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/q5HWSjxgUBd6LTGk9gWTig--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/f9e77c446279d65d5729cf8d99819c7d\" width=\"100%\" alt=\"2015 Nissan Armada\" data-reactid=\".rudjuxophc.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-2.1.$=11:0.$=10:0.0.$li-carouselItem-0.$carouselItem-0.0.0\" />",
                    "price": "$38,410",
                    "hp": "317 HP",
                    "model": "Armada",
                    "image/_alt": "2015 Nissan Armada"
                },
    {
                    "make": "nissan",
                    "image": "https://s.yimg.com/bt/api/res/1.2/aNDe7TdIfAkVMteg5aS0hQ--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/VDZ1nWTDfc43WcREQDCeNg--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/ace40f021fca06d11c23022276ef7721",
                    "mpg": "25 CITY / 31 HWY",
                    "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/aNDe7TdIfAkVMteg5aS0hQ--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/VDZ1nWTDfc43WcREQDCeNg--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/ace40f021fca06d11c23022276ef7721\" width=\"100%\" alt=\"2016 Nissan JUKE\" data-reactid=\".rudjuxophc.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-2.1.$=11:0.$=10:0.0.$li-carouselItem-1.$carouselItem-1.0.0\" />",
                    "price": "N/A",
                    "hp": "215 HP",
                    "model": "2016 JUKE",
                    "image/_alt": "2016 Nissan JUKE"
                },
    {
                    "make": "nissan",
                    "image": "https://s.yimg.com/bt/api/res/1.2/mjs7KJaSWnBimil0GorDQQ--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/XXPBpi_fKNwQuM1mo2ScqQ--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/6789ce56534237d1ed8c711ac45c8390",
                    "mpg": "21 CITY / 28 HWY",
                    "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/mjs7KJaSWnBimil0GorDQQ--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/XXPBpi_fKNwQuM1mo2ScqQ--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/6789ce56534237d1ed8c711ac45c8390\" width=\"100%\" alt=\"2016 Nissan Murano\" data-reactid=\".rudjuxophc.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-2.1.$=11:0.$=10:0.0.$li-carouselItem-2.$carouselItem-2.0.0\" />",
                    "price": "N/A",
                    "hp": "260 HP",
                    "model": "2016 Murano",
                    "image/_alt": "2016 Nissan Murano"
                }
]}

lexus_string = {"results":
                [
                    {
                        "make": "lexus",
                        "image": "https://s.yimg.com/bt/api/res/1.2/nYHGZtCM5qV8r2MkY7Irig--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/72e2InDX0pLICz4.ZhNP.Q--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/72ee64d52d8de7fb83d4d8a494e96e81",
                        "mpg": "43 CITY / 40 HWY",
                        "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/nYHGZtCM5qV8r2MkY7Irig--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/72e2InDX0pLICz4.ZhNP.Q--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/72ee64d52d8de7fb83d4d8a494e96e81\" width=\"100%\" alt=\"2015 Lexus CT 200h\" data-reactid=\".26bmkpotp1c.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-0.1.$=11:0.$=10:0.0.$li-carouselItem-0.$carouselItem-0.0.0\" />",
                        "price": "$32,200",
                        "hp": "134 HP",
                        "model": "CT 200h",
                        "image/_alt": "2015 Lexus CT 200h"
                    },
                    {
                        "make": "lexus",
                        "image": "https://s.yimg.com/bt/api/res/1.2/Ql.HDM2ajkPVJfYi6G29oQ--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/W_ubIgfFxLV4TXJJdnFhtQ--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/53fd7c8b531b576a4dfca4d5159be48f",
                        "mpg": "40 CITY / 39 HWY",
                        "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/Ql.HDM2ajkPVJfYi6G29oQ--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/W_ubIgfFxLV4TXJJdnFhtQ--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/53fd7c8b531b576a4dfca4d5159be48f\" width=\"100%\" alt=\"2016 Lexus ES 300h\" data-reactid=\".26bmkpotp1c.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-1.1.$=11:0.$=10:0.0.$li-carouselItem-0.$carouselItem-0.0.0\" />",
                        "price": "$40,920",
                        "hp": "200 HP",
                        "model": "2016 ES 300h",
                        "image/_alt": "2016 Lexus ES 300h"
                    },
                    {
                        "make": "lexus",
                        "image": "https://s.yimg.com/bt/api/res/1.2/Abo9gbXdr0AO0mZtsxdYfA--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/BIXGNgiyDQCVKDdRr_ZLGg--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/3814fdbd66ef2e4abeb40b827d8b66d5",
                        "mpg": "21 CITY / 31 HWY",
                        "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/Abo9gbXdr0AO0mZtsxdYfA--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/BIXGNgiyDQCVKDdRr_ZLGg--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/3814fdbd66ef2e4abeb40b827d8b66d5\" width=\"100%\" alt=\"2016 Lexus ES 350\" data-reactid=\".26bmkpotp1c.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-1.1.$=11:0.$=10:0.0.$li-carouselItem-1.$carouselItem-1.0.0\" />",
                        "price": "$38,000",
                        "hp": "268 HP",
                        "model": "2016 ES 350",
                        "image/_alt": "2016 Lexus ES 350"
                    },
                    {
                        "make": "lexus",
                        "image": "https://s.yimg.com/bt/api/res/1.2/APOvBd..HiHzm3LtLNI3YQ--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/cZlAD6KGWkFPWLjLR2LVdA--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/842e7b8ff4a4a04099e6f19122378950",
                        "mpg": "19 CITY / 29 HWY",
                        "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/APOvBd..HiHzm3LtLNI3YQ--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/cZlAD6KGWkFPWLjLR2LVdA--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/842e7b8ff4a4a04099e6f19122378950\" width=\"100%\" alt=\"2015 Lexus GS 350\" data-reactid=\".26bmkpotp1c.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-1.1.$=11:0.$=10:0.0.$li-carouselItem-2.$carouselItem-2.0.0\" />",
                        "price": "$48,600",
                        "hp": "306 HP",
                        "model": "GS 350",
                        "image/_alt": "2015 Lexus GS 350"
                    },
                    {
                        "make": "lexus",
                        "image": "https://s.yimg.com/bt/api/res/1.2/yWPQybXxbSq1Ocpf41FG1w--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/36AmF8r_TZAevzklLS7AwQ--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/78aebe11be464ac4aad41834c3ab06ae",
                        "mpg": "15 CITY / 20 HWY",
                        "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/yWPQybXxbSq1Ocpf41FG1w--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/36AmF8r_TZAevzklLS7AwQ--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/78aebe11be464ac4aad41834c3ab06ae\" width=\"100%\" alt=\"2015 Lexus GX 460\" data-reactid=\".26bmkpotp1c.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-2.1.$=11:0.$=10:0.0.$li-carouselItem-0.$carouselItem-0.0.0\" />",
                        "price": "$49,485",
                        "hp": "301 HP",
                        "model": "GX 460",
                        "image/_alt": "2015 Lexus GX 460"
                    },
                    {
                        "make": "lexus",
                        "image": "https://s.yimg.com/bt/api/res/1.2/vhW_jXEvNKf9LkYgHi4Tsw--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/FIRq1SVSo3oAXB4DrhTofg--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/a787801b2ef12feed0bf42e7580f9913",
                        "mpg": "12 CITY / 17 HWY",
                        "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/vhW_jXEvNKf9LkYgHi4Tsw--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/FIRq1SVSo3oAXB4DrhTofg--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/a787801b2ef12feed0bf42e7580f9913\" width=\"100%\" alt=\"2015 Lexus LX 570\" data-reactid=\".26bmkpotp1c.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-2.1.$=11:0.$=10:0.0.$li-carouselItem-1.$carouselItem-1.0.0\" />",
                        "price": "$83,180",
                        "hp": "383 HP",
                        "model": "LX 570",
                        "image/_alt": "2015 Lexus LX 570"
                    },
                    {
                        "make": "lexus",
                        "image": "https://s.yimg.com/bt/api/res/1.2/zy.WqnMK1FLmb06Gci9zaA--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/E4LuRAkDk2rBBdbgxhkCgQ--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/42cb358593040410672c44878668aa48",
                        "mpg": "22 CITY / 28 HWY",
                        "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/zy.WqnMK1FLmb06Gci9zaA--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/E4LuRAkDk2rBBdbgxhkCgQ--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/42cb358593040410672c44878668aa48\" width=\"100%\" alt=\"2015 Lexus NX 200t\" data-reactid=\".26bmkpotp1c.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-2.1.$=11:0.$=10:0.0.$li-carouselItem-2.$carouselItem-2.0.0\" />",
                        "price": "$34,480",
                        "hp": "235 HP",
                        "model": "NX 200t",
                        "image/_alt": "2015 Lexus NX 200t"
                    }
                ]}

mercedes_string = {"results": [
    {
        "make": "mercedes-benz",
        "image": "https://s.yimg.com/bt/api/res/1.2/_9BAPiPQON5tVK98NO1bSA--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/t0B09Zm6sO8O23cLSBHpQQ--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/https://s.yimg.com/dh/ap/default/150316/no_image_car.jpg",
        "mpg": "16 CITY / 22 HWY",
        "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/_9BAPiPQON5tVK98NO1bSA--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/t0B09Zm6sO8O23cLSBHpQQ--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/https://s.yimg.com/dh/ap/default/150316/no_image_car.jpg\" width=\"100%\" alt=\"2016 Mercedes-Benz AMG GT\" data-reactid=\".1snyc6jckxs.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-0.1.$=11:0.$=10:0.0.$li-carouselItem-0.$carouselItem-0.0.0\" />",
        "price": "$129,900",
        "hp": "503 HP",
        "model": "2016 AMG GT",
        "image/_alt": "2016 Mercedes-Benz AMG GT"
    },
    {
        "make": "mercedes-benz",
        "image": "https://s.yimg.com/bt/api/res/1.2/pDuDbe_c4o18lpnzGyzOiA--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/WSmMw39HHW3bie8_QT_Jjw--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/e37ea51f4acf7a4eb519f3fda7fc88e8",
        "mpg": "N/A CITY / N/A HWY",
        "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/pDuDbe_c4o18lpnzGyzOiA--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/WSmMw39HHW3bie8_QT_Jjw--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/e37ea51f4acf7a4eb519f3fda7fc88e8\" width=\"100%\" alt=\"2016 Mercedes-Benz SLK-Class\" data-reactid=\".1snyc6jckxs.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-0.1.$=11:0.$=10:0.0.$li-carouselItem-1.$carouselItem-1.0.0\" />",
        "price": "$47,000",
        "hp": "241 HP",
        "model": "2016 SLK-Class",
        "image/_alt": "2016 Mercedes-Benz SLK-Class"
    },
    {
        "make": "mercedes-benz",
        "image": "https://s.yimg.com/bt/api/res/1.2/_9BAPiPQON5tVK98NO1bSA--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/t0B09Zm6sO8O23cLSBHpQQ--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/https://s.yimg.com/dh/ap/default/150316/no_image_car.jpg",
        "mpg": "13 CITY / 19 HWY",
        "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/_9BAPiPQON5tVK98NO1bSA--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/t0B09Zm6sO8O23cLSBHpQQ--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/https://s.yimg.com/dh/ap/default/150316/no_image_car.jpg\" width=\"100%\" alt=\"2015 Mercedes-Benz SLS AMG GT\" data-reactid=\".1snyc6jckxs.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-0.1.$=11:0.$=10:0.0.$li-carouselItem-2.$carouselItem-2.0.0\" />",
        "price": "$221,580",
        "hp": "583 HP",
        "model": "SLS AMG GT",
        "image/_alt": "2015 Mercedes-Benz SLS AMG GT"
    },
    {
        "make": "mercedes-benz",
        "image": "https://s.yimg.com/bt/api/res/1.2/_9BAPiPQON5tVK98NO1bSA--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/t0B09Zm6sO8O23cLSBHpQQ--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/https://s.yimg.com/dh/ap/default/150316/no_image_car.jpg",
        "mpg": "N/A CITY / N/A HWY",
        "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/_9BAPiPQON5tVK98NO1bSA--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/t0B09Zm6sO8O23cLSBHpQQ--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/https://s.yimg.com/dh/ap/default/150316/no_image_car.jpg\" width=\"100%\" alt=\"2015 Mercedes-Benz B-Class\" data-reactid=\".1snyc6jckxs.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-1.1.$=11:0.$=10:0.0.$li-carouselItem-0.$carouselItem-0.0.0\" />",
        "price": "$41,450",
        "hp": "177 HP",
        "model": "B-Class",
        "image/_alt": "2015 Mercedes-Benz B-Class"
    },
    {
        "make": "mercedes-benz",
        "image": "https://s.yimg.com/bt/api/res/1.2/WcqghBhJFYIfGSOW6fuXeQ--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/RslJGIltBmq0jf5p2PvTxQ--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/896241681846d37d9903bdec4ff676bd",
        "mpg": "25 CITY / 34 HWY",
        "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/WcqghBhJFYIfGSOW6fuXeQ--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/RslJGIltBmq0jf5p2PvTxQ--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/896241681846d37d9903bdec4ff676bd\" width=\"100%\" alt=\"2015 Mercedes-Benz C-Class\" data-reactid=\".1snyc6jckxs.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-1.1.$=11:0.$=10:0.0.$li-carouselItem-1.$carouselItem-1.0.0\" />",
        "price": "$38,400",
        "hp": "241 HP",
        "model": "C-Class",
        "image/_alt": "2015 Mercedes-Benz C-Class"
    },
    {
        "make": "mercedes-benz",
        "image": "https://s.yimg.com/bt/api/res/1.2/WHU1sQwR61xIp_lBMrj2qw--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/NcV0lF_tyQLcrzdsHQwbpg--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/d52e8387cc27597998588cb69bfc375c",
        "mpg": "26 CITY / 38 HWY",
        "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/WHU1sQwR61xIp_lBMrj2qw--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/NcV0lF_tyQLcrzdsHQwbpg--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/d52e8387cc27597998588cb69bfc375c\" width=\"100%\" alt=\"2015 Mercedes-Benz CLA-Class\" data-reactid=\".1snyc6jckxs.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-1.1.$=11:0.$=10:0.0.$li-carouselItem-2.$carouselItem-2.0.0\" />",
        "price": "$31,500",
        "hp": "208 HP",
        "model": "CLA-Class",
        "image/_alt": "2015 Mercedes-Benz CLA-Class"
    },
    {
        "make": "mercedes-benz",
        "image": "https://s.yimg.com/bt/api/res/1.2/osvMwQfqfmeIq3wIV8IU6w--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/rbN4M9aejnY54MNQgy6BMg--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/b5e583d96a4328cb807e2fb2e7de29bd",
        "mpg": "12 CITY / 15 HWY",
        "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/osvMwQfqfmeIq3wIV8IU6w--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/rbN4M9aejnY54MNQgy6BMg--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/b5e583d96a4328cb807e2fb2e7de29bd\" width=\"100%\" alt=\"2015 Mercedes-Benz G-Class\" data-reactid=\".1snyc6jckxs.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-2.1.$=11:0.$=10:0.0.$li-carouselItem-0.$carouselItem-0.0.0\" />",
        "price": "$115,400",
        "hp": "382 HP",
        "model": "G-Class",
        "image/_alt": "2015 Mercedes-Benz G-Class"
    },
    {
        "make": "mercedes-benz",
        "image": "https://s.yimg.com/bt/api/res/1.2/4sXuqDP33tugtPWFWRTj8w--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/dfyZB4F8c3GD5x6QvUDvBw--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/b41172165fd7fd1e3dfbecc60d0e8ab4",
        "mpg": "19 CITY / 26 HWY",
        "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/4sXuqDP33tugtPWFWRTj8w--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/dfyZB4F8c3GD5x6QvUDvBw--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/b41172165fd7fd1e3dfbecc60d0e8ab4\" width=\"100%\" alt=\"2015 Mercedes-Benz GL-Class\" data-reactid=\".1snyc6jckxs.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-2.1.$=11:0.$=10:0.0.$li-carouselItem-1.$carouselItem-1.0.0\" />",
        "price": "$63,600",
        "hp": "240 HP",
        "model": "GL-Class",
        "image/_alt": "2015 Mercedes-Benz GL-Class"
    },
    {
        "make": "mercedes-benz",
        "image": "https://s.yimg.com/bt/api/res/1.2/7FL0LEjh1Oh9rSiC1t8e1Q--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/XPYjCqUS3JeB1c5UKH0lAQ--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/e4952d2cf739f61820754e4f0dc763de",
        "mpg": "25 CITY / 35 HWY",
        "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/7FL0LEjh1Oh9rSiC1t8e1Q--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/XPYjCqUS3JeB1c5UKH0lAQ--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/e4952d2cf739f61820754e4f0dc763de\" width=\"100%\" alt=\"2015 Mercedes-Benz GLA-Class\" data-reactid=\".1snyc6jckxs.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-2.1.$=11:0.$=10:0.0.$li-carouselItem-2.$carouselItem-2.0.0\" />",
        "price": "$31,300",
        "hp": "208 HP",
        "model": "GLA-Class",
        "image/_alt": "2015 Mercedes-Benz GLA-Class"
    }
]}

toyota_string = {"results": [
                {
                    "make": "toyota",
                    "image": "https://s.yimg.com/bt/api/res/1.2/.WeCjBNKWplMR419Au7Vhw--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/fkONMOGFq530nYBiA9vSOQ--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/6d19c990d4cf7a436952801907621947",
                    "mpg": "17 CITY / 22 HWY",
                    "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/.WeCjBNKWplMR419Au7Vhw--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/fkONMOGFq530nYBiA9vSOQ--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/6d19c990d4cf7a436952801907621947\" width=\"100%\" alt=\"2015 Toyota 4Runner\" data-reactid=\".9b3qvna96o.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-0.1.$=11:0.$=10:0.0.$li-carouselItem-0.$carouselItem-0.0.0\" />",
                    "price": "$33,210",
                    "hp": "270 HP",
                    "model": "4Runner",
                    "image/_alt": "2015 Toyota 4Runner"
                },
    {
                    "make": "toyota",
                    "image": "https://s.yimg.com/bt/api/res/1.2/drmEvHNpXo.CZ4wECVbXiw--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/BNBIDsmexArOLueqWq1llQ--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/e8bb3ed6fc4f28331065337fbf24a04e",
                    "mpg": "19 CITY / 25 HWY",
                    "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/drmEvHNpXo.CZ4wECVbXiw--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/BNBIDsmexArOLueqWq1llQ--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/e8bb3ed6fc4f28331065337fbf24a04e\" width=\"100%\" alt=\"2016 Toyota Highlander\" data-reactid=\".9b3qvna96o.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-0.1.$=11:0.$=10:0.0.$li-carouselItem-1.$carouselItem-1.0.0\" />",
                    "price": "N/A",
                    "hp": "270 HP",
                    "model": "2016 Highlander",
                    "image/_alt": "2016 Toyota Highlander"
                },
    {
                    "make": "toyota",
                    "image": "https://s.yimg.com/bt/api/res/1.2/e79Pm3Ge8pvSM49Bd8.zQQ--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/k9Ci.AUJEkQCYsZcR81Uvg--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/d01b575e9cfa052819e5cd229e70d79f",
                    "mpg": "27 CITY / 28 HWY",
                    "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/e79Pm3Ge8pvSM49Bd8.zQQ--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/k9Ci.AUJEkQCYsZcR81Uvg--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/d01b575e9cfa052819e5cd229e70d79f\" width=\"100%\" alt=\"2015 Toyota Highlander Hybrid\" data-reactid=\".9b3qvna96o.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-0.1.$=11:0.$=10:0.0.$li-carouselItem-2.$carouselItem-2.0.0\" />",
                    "price": "$47,850",
                    "hp": "280 HP",
                    "model": "Highlander Hybrid",
                    "image/_alt": "2015 Toyota Highlander Hybrid"
                },
    {
                    "make": "toyota",
                    "image": "https://s.yimg.com/bt/api/res/1.2/5_0y7F_HU8OK.Xdllgt1pA--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/UeCP.MheSJsUDdmHWpDjFg--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/891512b1bb5cdd003fb3a0b8936c40c1",
                    "mpg": "21 CITY / 31 HWY",
                    "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/5_0y7F_HU8OK.Xdllgt1pA--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/UeCP.MheSJsUDdmHWpDjFg--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/891512b1bb5cdd003fb3a0b8936c40c1\" width=\"100%\" alt=\"2015 Toyota Avalon\" data-reactid=\".9b3qvna96o.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-1.1.$=11:0.$=10:0.0.$li-carouselItem-0.$carouselItem-0.0.0\" />",
                    "price": "$32,285",
                    "hp": "268 HP",
                    "model": "Avalon",
                    "image/_alt": "2015 Toyota Avalon"
                },
    {
                    "make": "toyota",
                    "image": "https://s.yimg.com/bt/api/res/1.2/xBUKHiOnNu9hIJAJte0HfA--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/Oi7p48UL.z4la5gWGo5xhA--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/2e9c18a46c7fece81deae958a0ed7275",
                    "mpg": "40 CITY / 39 HWY",
                    "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/xBUKHiOnNu9hIJAJte0HfA--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/Oi7p48UL.z4la5gWGo5xhA--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/2e9c18a46c7fece81deae958a0ed7275\" width=\"100%\" alt=\"2015 Toyota Avalon Hybrid\" data-reactid=\".9b3qvna96o.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-1.1.$=11:0.$=10:0.0.$li-carouselItem-1.$carouselItem-1.0.0\" />",
                    "price": "$37,800",
                    "hp": "200 HP",
                    "model": "Avalon Hybrid",
                    "image/_alt": "2015 Toyota Avalon Hybrid"
                },
    {
                    "make": "toyota",
                    "image": "https://s.yimg.com/bt/api/res/1.2/n1clV8waJiwHjwDLyxy74Q--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/gevu6iyW3__pUJOQ0WPizQ--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/4ffc29b6b846be2dc342e884e8e82da0",
                    "mpg": "25 CITY / 35 HWY",
                    "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/n1clV8waJiwHjwDLyxy74Q--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/gevu6iyW3__pUJOQ0WPizQ--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/4ffc29b6b846be2dc342e884e8e82da0\" width=\"100%\" alt=\"2015 Toyota Camry\" data-reactid=\".9b3qvna96o.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-1.1.$=11:0.$=10:0.0.$li-carouselItem-2.$carouselItem-2.0.0\" />",
                    "price": "$22,970",
                    "hp": "178 HP",
                    "model": "Camry",
                    "image/_alt": "2015 Toyota Camry"
                },
    {
                    "make": "toyota",
                    "image": "https://s.yimg.com/bt/api/res/1.2/_J3DjH0v94R_o2umq_DIkQ--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/BNPOeKhY4qYZsY4eYXmKtA--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/5ff4cae7357b1c1f53e923f3385cc7f6",
                    "mpg": "51 CITY / 48 HWY",
                    "img_url": "<img src=\"https://s.yimg.com/bt/api/res/1.2/_J3DjH0v94R_o2umq_DIkQ--/YXBwaWQ9eW5ld3M7dz01MDA-/https://s.yimg.com/bt/api/res/1.2/BNPOeKhY4qYZsY4eYXmKtA--/YXBwaWQ9eW5ld3M7Zmk9ZmlsbDt3PTEyODA7aD01ODY-/http://media.zenfs.com/en-US/us.autos.evox.com/5ff4cae7357b1c1f53e923f3385cc7f6\" width=\"100%\" alt=\"2015 Toyota Prius\" data-reactid=\".9b3qvna96o.1.3.0.1:2.0.$main-4-AutoCarousel.1.0.0:$carousel-2.1.$=11:0.$=10:0.0.$li-carouselItem-0.$carouselItem-0.0.0\" />",
                    "price": "$24,200",
                    "hp": "134 HP",
                    "model": "Prius",
                    "image/_alt": "2015 Toyota Prius"
                }
]}

load_list = [bmw_string, tesla_string, nissan_string,
             lexus_string, mercedes_string, toyota_string]


def load_bmw():
    for i in range(0, 7):
        model = json.dumps(load_list[0]["results"][i]["model"])
        image_url = json.dumps(load_list[0]["results"][i]["image"])
        image_url = image_url[1:-1]
        model = model[1:-1]
        make_id = 1
        model_input = Model(name=model, picture_url=image_url, make_id=make_id)
        session.add(model_input)
        session.commit()
        make_id = 1
        price = json.dumps(load_list[0]["results"][i]["price"])
        hp = json.dumps(load_list[0]["results"][i]["hp"])
        mpg = json.dumps(load_list[0]["results"][i]["mpg"])
        price = price[1:-1]
        hp = hp[1:-1]
        mpg = mpg[1:-1]
        car_id = i + 1
        spec_input = Specs(
            price=price, hp=hp, mpg=mpg, make_id=make_id, car_id=car_id)
        session.add(spec_input)
        session.commit()


def load_tesla():
    for i in range(0, 1):
        model = json.dumps(load_list[1]["results"][i]["model"])
        image_url = json.dumps(load_list[1]["results"][i]["image"])
        image_url = image_url[1:-1]
        model = model[1:-1]
        make_id = 2
        model_input = Model(name=model, picture_url=image_url, make_id=make_id)
        session.add(model_input)
        session.commit()
        new_car_id = 8
        price = json.dumps(load_list[1]["results"][i]["price"])
        hp = json.dumps(load_list[1]["results"][i]["hp"])
        mpg = json.dumps(load_list[1]["results"][i]["mpg"])
        price = price[1:-1]
        hp = hp[1:-1]
        mpg = mpg[1:-1]
        car_id = i + new_car_id
        spec_input = Specs(
            price=price, hp=hp, mpg=mpg, make_id=make_id, car_id=car_id)
        session.add(spec_input)
        session.commit()


def load_nissan():
    for i in range(0, 7):
        model = json.dumps(load_list[2]["results"][i]["model"])
        image_url = json.dumps(load_list[2]["results"][i]["image"])
        image_url = image_url[1:-1]
        model = model[1:-1]
        make_id = 3
        model_input = Model(name=model, picture_url=image_url, make_id=make_id)
        session.add(model_input)
        session.commit()
        new_car_id = 9
        price = json.dumps(load_list[2]["results"][i]["price"])
        hp = json.dumps(load_list[2]["results"][i]["hp"])
        mpg = json.dumps(load_list[2]["results"][i]["mpg"])
        price = price[1:-1]
        hp = hp[1:-1]
        mpg = mpg[1:-1]
        car_id = i + new_car_id
        spec_input = Specs(
            price=price, hp=hp, mpg=mpg, make_id=make_id, car_id=car_id)
        session.add(spec_input)
        session.commit()


def load_lexus():
    for i in range(0, 7):
        model = json.dumps(load_list[3]["results"][i]["model"])
        image_url = json.dumps(load_list[3]["results"][i]["image"])
        image_url = image_url[1:-1]
        model = model[1:-1]
        make_id = 4
        model_input = Model(name=model, picture_url=image_url, make_id=make_id)
        session.add(model_input)
        session.commit()
        new_car_id = 16
        price = json.dumps(load_list[3]["results"][i]["price"])
        hp = json.dumps(load_list[3]["results"][i]["hp"])
        mpg = json.dumps(load_list[3]["results"][i]["mpg"])
        price = price[1:-1]
        hp = hp[1:-1]
        mpg = mpg[1:-1]
        car_id = i + new_car_id
        spec_input = Specs(
            price=price, hp=hp, mpg=mpg, make_id=make_id, car_id=car_id)
        session.add(spec_input)
        session.commit()


def load_mercedes():
    for i in range(0, 9):
        model = json.dumps(load_list[4]["results"][i]["model"])
        image_url = json.dumps(load_list[4]["results"][i]["image"])
        image_url = image_url[1:-1]
        model = model[1:-1]
        make_id = 5
        model_input = Model(name=model, picture_url=image_url, make_id=make_id)
        session.add(model_input)
        session.commit()
        new_car_id = 23
        price = json.dumps(load_list[4]["results"][i]["price"])
        hp = json.dumps(load_list[4]["results"][i]["hp"])
        mpg = json.dumps(load_list[4]["results"][i]["mpg"])
        price = price[1:-1]
        hp = hp[1:-1]
        mpg = mpg[1:-1]
        car_id = i + new_car_id
        spec_input = Specs(
            price=price, hp=hp, mpg=mpg, make_id=make_id, car_id=car_id)
        session.add(spec_input)
        session.commit()


def load_toyota():
    for i in range(0, 7):
        model = json.dumps(load_list[5]["results"][i]["model"])
        image_url = json.dumps(load_list[5]["results"][i]["image"])
        image_url = image_url[1:-1]
        model = model[1:-1]
        make_id = 6
        model_input = Model(name=model, picture_url=image_url, make_id=make_id)
        session.add(model_input)
        session.commit()
        new_car_id = 32
        price = json.dumps(load_list[5]["results"][i]["price"])
        hp = json.dumps(load_list[5]["results"][i]["hp"])
        mpg = json.dumps(load_list[5]["results"][i]["mpg"])
        price = price[1:-1]
        hp = hp[1:-1]
        mpg = mpg[1:-1]
        car_id = i + new_car_id
        spec_input = Specs(
            price=price, hp=hp, mpg=mpg, make_id=make_id, car_id=car_id)
        session.add(spec_input)
        session.commit()


# Loads data models to database when excuted from command line

load_bmw()
load_tesla()
load_nissan()
load_lexus()
load_mercedes()
load_toyota()
