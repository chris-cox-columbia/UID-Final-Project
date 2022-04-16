drinksData = {"1":{"id":"1",
                    "name":"Moscow Mule",
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
                                                    "hexcode":"#FFB200"
                                                    },
                                    "Vodka":{
                                            "quantity":"One Part",
                                            "hexcode":"#FFFFFF"
                                        }
                                    },
                    "procedure":["Add Ginger Beer and Vodka together at a ratio of 2:1",
                                 "Garnish with a lime slice optionally squeezing some lime juice inside",
                                 "Serve with chilled ice"],
                    "emphasize":{"procedure_1":["Ginger Beer","Vodka"],"procedure_2":["lime slice"]},
                    "next":"2"
                    },
                "2":{"id":"2",
                    "name":"Campari Flamingo",
                    "description":["Campari is often used in cocktails and is commonly served with soda water or citrus juice",
                                    "Campari was invented in 1860 by Gaspare Campari in Novara, Italy. It was originally coloured with carmine dye, derived from crushed cochineal insects, which gave the drink its distinctive red colour",
                                    "Campari is a registered trademark of Davide Campari Milano S.P.A.,[2][3] which is part of Gruppo Campari (Campari Group)"],
                    "ingredient_number":"four",
                    "ingrdient_list":["Grapefruit Soda","Rum","Lime Juice","Campari"],
                    "ingredient_details":{
                                    "Grapefruit Soda":{
                                                    "quantity":"Four parts",
                                                    "hexcode":"#EE84FE"
                                                    },
                                    "Rum":{
                                            "quantity":"Three parts",
                                            "hexcode":"#D2801F"
                                            },
                                    "Lime Juice":{
                                            "quantity":"Two parts",
                                            "hexcode":"#92FF0D"
                                        },
                                    "Campari":{
                                            "quantity":"One part",
                                            "hexcode":"#FF000"
                                        }
                                    },
                    "procedure":["Fill a cocktail shaker with ice. Add lime juice, rum, and Campari. Shake well.",
                                 "Strain into ice-filled rocks glass. Add grapefruit soda, stir gently and serve"],
                    "next":"3"
                    },
                "3":{"id":"3",
                    "name":"Vodka Martini",
                    "description":["Before its silver screen appearance, the Martini Cocktail was featured in the 1958 book Dr. No by Ian Fleming.",
                                    "The original martini cocktails were made with Old Tom gin, sweet vermouth, bitters and a little bit of maraschino liqueur.",
                                    "In the 80s and 90s flavor was king. This is where we saw the birth of some phenomenal classic cocktails such as the iconic Espresso Martini Cocktail, the Cosmopolitan and more. "],
                    "ingredient_number":"three",
                    "ingrdient_list":["Vodka","Dry vermouth","Olives"],
                    "ingredient_details":{
                                    "Vodka":{
                                            "quantity":"Three parts",
                                            "hexcode":"#FFFFFF"
                                            },
                                    "Dry vermouth":{
                                            "quantity":"One part",
                                            "hexcode":"#EAE8B6"
                                            },
                                    "Olives":{
                                            "quantity":"Garnish",
                                            "hexcode":"#92FF0D"
                                        }
                                    },
                    "procedure":["Freeze martini glass 15 minutes before making the drink.",
                                 "Pour the vodka and vermouth into a  mixing glass or cocktail shaker filled with ice. Stir vigorously, about 20 seconds, until well chilled.",
                                 "Strain into a martini glass, garnish with olive or lemon peel and serve."],
                    "next":""
                    }
            }
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
                            "Vodka",
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
                  "emphasize":{"Moscow Mule"},
                  "options":["Gin",
                            "Lime Slice",
                            "Ginger Beer"
                            ],
                    "answer":[2,0,1],
                    "next":"3"
                    }, 
            "3":{"id":"3",
                  "type":"free form",
                  "question":"List the ingredients and their ratios of a Moscow Mule: (not all boxes must be used)",
                  "emphasize":{"Moscow Mule"},
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
                  "emphasize":{"Campari Flamingo"},
                  "options":["Grapefruit Soda",
                            "Rum",
                            "Lime Juice",
                            "Campari",
                            ],
                    "answer":[4,3,2,1],
                    "next":"6"
                    }, 
            "6":{"id":"6",
                  "type":"free form",
                  "question":"List the ingredients and their ratios of a Campari Flamingo: (not all boxes must be used)",
                  "emphasize":{"Campari Flamingo"},
                  "answer":{"Ginger Beer":"2",
                            "Lime Slice":"0",
                            "Gin":"0"},
                   "next":"4"
                }, 
            "7":{"id":"7",
                  "type":"drag and drop",
                  "question":"Drag the ingredients for a Vodka Martini into the shaker.",
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
                    "answer":["Vodka",
                            "Dry Vermouth",
                            "Olives",],
                    "next":"8"
                    },   
            "8":{"id":"8",
                  "type":"ratios",
                  "question":"Give the ingredient ratio in a Vodka Martini (garnishes have ratio of 0):",
                  "emphasize":{"Vodka Martini"},
                  "options":["Vodka",
                            "Dry Vermouth",
                            "Olives",],
                    "answer":[3,1,0],
                    "next":"9"
                    }, 
            "9":{"id":"9",
                  "type":"free form",
                  "question":"List the ingredients and their ratios of a Vodka Martini: (not all boxes must be used)",
                  "emphasize":{"Vodka Martini"},
                  "answer":{"Vodka":"3",
                            "Dry Vermouth":"1",
                            "Olives":"0"},
                   "next":"4"
                }, 
}