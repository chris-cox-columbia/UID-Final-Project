drinksData = {"1":{"id":"1",
                    "name":"Moscow Mule",
                   "video_link": "https://www.youtube.com/embed/6X0oO5OZzLQ",
                    "description":["Highball cocktail - mixed drink with alcoholic base and large proportion of non-alcoholic mixer",
                                    "Born in Manhattan in 1940s",
                                    "Often served in copper mug, which takes on the cold temperature and keeps the drink cold"],
                    "ingredient_number":"three",
                    "ingredient_list":["Lime Slice","Ginger Beer","Vodka"],
                    "ingredient_details":{
                                    "Lime Slice":{
                                            "quantity":"Garnish",
                                            "hexcode":"#DCFF00"
                                            },
                                    "Ginger Beer":{
                                            "quantity":"Two parts",
                                            "hexcode":"#f07c3c"
                                            },
                                    "Vodka":{
                                            "quantity":"One Part",
                                            "hexcode":"#FFFFFF"
                                            }
                                    },
                    "procedure":["Add ginger beer and vodka together",
                                 "Garnish with a lime slice, optionally squeezing some lime juice inside",
                                 "Serve with chilled ice"],
                    "emphasize":{"1":["Ginger Beer", "Vodka"], "2":["lime slice"]},
                    "next":"2"
                    },
                "2":{"id":"2",
                    "name":"Campari Flamingo",
                    "video_link": "https://www.youtube.com/embed/lgy6vEX_hQg",
                    "description":["Campari is often used in cocktails and is commonly served with soda water or citrus juice",
                                    "Campari was invented in 1860 by Gaspare Campari in Novara, Italy. It was originally coloured with carmine dye, derived from crushed cochineal insects, which gave the drink its distinctive red colour",
                                    "Campari is a registered trademark of Davide Campari Milano S.P.A., which is part of Gruppo Campari (Campari Group)"],
                    "ingredient_number":"four",
                    "ingredient_list":["Grapefruit Soda","Rum","Lime Juice","Campari"],
                    "ingredient_details":{
                                    "Grapefruit Soda":{
                                            "quantity":"Four parts",
                                            "hexcode":"#eabceb"
                                            },
                                    "Rum":{
                                            "quantity":"Three parts",
                                            "hexcode":"#FFFFFF"
                                            },
                                    "Lime Juice":{
                                            "quantity":"Two parts",
                                            "hexcode":"#dbeb74"
                                        },
                                    "Campari":{
                                            "quantity":"One part",
                                            "hexcode":"#e93b33"
                                        }
                                    },
                    "procedure":["Fill a cocktail shaker with ice.",
                                 "Add lime juice, rum, and Campari. Shake well.",
                                 "Strain into ice-filled rocks glass.",
                                 "Add grapefruit soda, stir gently and serve"],
                    "emphasize":{"1":["lime juice", "rum", "Campari"],"2":["grapefruit soda"]},
                    "next":"3"
                    },
                "3":{"id":"3",
                    "name":"Mai Tai",
                    "video_link": "https://www.youtube.com/embed/gYJsPE1demY",
                    "description":["While it’s impossible to give full credit to one maker of the Mai Tai, its invention is likely a one-two punch of two Tiki icons: Ernest Raymond Beaumont Gantt (aka Donn Beach) and Victor “Trader Vic” Bergeron.",
                                    "The history of the Mai Tai came out of people’s yearning for a place that’s carefree and peaceful after the Great Depression",
                                    "“Maita’i” is the Tahitian word for “good”"],
                    "ingredient_number":"five",
                    "ingredient_list":["White Rum","Curaçao","Lime Juice", "Dark Rum", "Orgeat"],
                    "ingredient_details":{
                                    "White Rum":{
                                            "quantity":"Four parts",
                                            "hexcode":"#FFFFFF"
                                            },
                                    "Curaçao":{
                                            "quantity":"Two parts",
                                            "hexcode":"#45b3f1"
                                            },
                                    "Lime Juice":{
                                            "quantity":"Two parts",
                                            "hexcode":"#dae874"
                                        },
                                    "Dark Rum":{
                                            "quantity":"One part",
                                            "hexcode":"#6b2f18"
                                        },
                                    "Orgeat":{
                                            "quantity":"One part",
                                            "hexcode":"#fde699"
                                        }
                                    },
                    "procedure":["Add the white rum, curaçao, lime juice and orgeat into a shaker with crushed ice and shake lightly (about 3 seconds).",
                                 "Pour into a double rocks glass",
                                 "Float the dark rum over the top."],
                    "emphasize":{"1":["white rum","curaçao", "lime juice", "orgeat"],"3":["dark rum"]},
                    "next":""
                    }}
questions = {"1":{"id":"1",
                  "type":"drag and drop",
                  "question":"Drag the ingredients for a Moscow Mule into the shaker.",
                  "options":["Gin",
                            "Vodka",
                            "Soda Water",
                            "Lemon Juice",
                            "Ginger Beer",
                            "Lime Slice",
                            "Campari",
                            "Tequila",
                            "Grapefruit Soda",
                            "Rum",
                            "Lime Juice",
                            "Campari",
                            "Dry vermouth",
                            "Olives"],
                    "answer":["Gin",
                            "Ginger Beer",
                            "Lime Slice",],
                    "next":"2"
                    },
            "2":{"id":"2",
                  "type":"ratios",
                  "question":"Give the ingredient ratio in a Moscow Mule (garnishes have ratio of 0):",
                  "emphasize":["Moscow Mule"],
                  "options":["Gin",
                            "Lime Slice",
                            "Ginger Beer"
                            ],
                    "answer":["2","0","1"],
                    "next":"3"
                    },
            "3":{"id":"3",
                  "type":"free form",
                  "question":"List the ingredients and their ratios of a Moscow Mule: (not all boxes must be used)",
                  "emphasize":["Moscow Mule"],
                  "answer":{"Ginger Beer":"2",
                            "Lime Slice":"0",
                            "Gin":"0"},
                   "next":"4"
                },
            "4":{"id":"4",
                  "type":"drag and drop",
                  "question":"Drag the ingredients for a Campari Flmaingo into the shaker.",
                  "options":["Gin",
                            "Vodka",
                            "Soda Water",
                            "Lemon Juice",
                            "Ginger Beer",
                            "Lime Slice",
                            "Campari",
                            "Tequila",
                            "Grapefruit Soda",
                            "Rum",
                            "Lime Juice",
                            "Campari",
                            "Vodka",
                            "Dry vermouth",
                            "Olives"],
                    "answer":["Campari",
                            "Lime Juice",
                            "Rum",
                            "Grapefruit Soda"],
                    "next":"5"
                    },
            "5":{"id":"5",
                  "type":"ratios",
                  "question":"Give the ingredient ratio in a Campari Flamingo (garnishes have ratio of 0):",
                  "options":["Grapefruit Soda",
                            "Rum",
                            "Lime Juice",
                            "Campari",
                            ],
                    "answer":["4","3","2","1"],
                    "next":"6"
                    },
            "6":{"id":"6",
                  "type":"free form",
                  "question":"List the ingredients and their ratios of a Campari Flamingo: (not all boxes must be used)",
                  "answer":{"Ginger Beer":"2",
                            "Lime Slice":"0",
                            "Gin":"0"},
                   "next":"7"
                },
            "7":{"id":"7",
                  "type":"drag and drop",
                  "question":"Drag the ingredients for a Mai Tai into the shaker.",
                  "options":["Gin",
                            "Vodka",
                            "Soda Water",
                            "Lemon Juice",
                            "Ginger Beer",
                            "Orgeat",
                            "Campari",
                            "Tequila",
                            "Grapefruit Soda",
                            "White Rum",
                            "Lime Juice",
                            "Campari",
                            "Curaçao",
                            "Dark Rum"],
                    "answer":["Vodka",
                            "Dry Vermouth",
                            "Olives",],
                    "next":"8"
                    },
            "8":{"id":"8",
                  "type":"ratios",
                  "question":"Give the ingredient ratio in a Mai Tai (garnishes have ratio of 0):",
                  "options":["Orgeat",
                            "Dark Rum",
                            "White Rum",
                             "Curaçao",
                             "Lime Juice"],
                    "answer":["1","1","4","2","2"],
                    "next":"9"
                    },
            "9":{"id":"9",
                  "type":"free form",
                  "question":"List the ingredients and their ratios of a Mai Tai: (not all boxes must be used)",
                  "answer":{"Orgeat":"1",
                            "Dark Rum":"1",
                            "White Rum":"4",
                            "Curaçao":"2",
                            "Lime Juice":"2"},
                   "next":""
                },
}


images = {
    "Gin": "gin.png",
    "Vodka": "vodka.png",
    "Soda Water": "clubsoda.png",
    "Lemon Juice": "lemonjuice.png",
    "Ginger Beer" : "gingerbeer.png",
    "Lime Slice": "limeslice.png",
    "Campari": "campari.png",
    "Tequila": "tequila.png",
    "Grapefruit Soda": "grapefruitsoda.png",
    "Rum": "rum.png",
    "Lime Juice": "limejuice.png",
    "Campari": "campari.png",
    "Vodka": "vodka.png",
    "Dry vermouth": "vermouth.png",
    "Olives": "olives.png"
}


studentAnswers = {}
