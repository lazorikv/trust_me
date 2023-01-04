import {useEffect, useState} from "react";
import "../../styles/home/article.css"

const Article = () => {
    return (
        <>
            <div className="title">
                <h1>
                    The Negative Effects of Using Real Estate Agents:
                </h1>
                <h1>
                    Why It Pays to Be Informed
                </h1>
            </div>
            <div className="articleText">
                Whether you're a potential homebuyer or an experienced real estate investor, it's important to be aware
                of the potential pitfalls associated with using real estate agents. While most agents are honest and
                provide valuable assistance, there are some negative effects to consider before engaging a real estate
                agent. In this article, we'll discuss the potential drawbacks of relying on a real estate agent for your
                next transaction.

                <div className="articleItem">
                    <span>
                        1. Lack of Professionalism: Not all real estate agents are alike and professionalism can vary
                significantly from one to the next. This can be problematic as inexperienced agents may not possess the
                same level of expertise and knowledge as another. Additionally, they may not know the local market well
                enough to offer sound advice or strategies.
                    </span>
                    <img src="homepage/1.jpg" alt="First Image"/>
                </div>
                <div className="articleItem">
                    2. Lack of Transparency: Many real estate agents may not be open and honest about their commission
                    or
                    fees. This can lead to hidden charges that can significantly increase the cost of a transaction.
                    It's
                    also possible that an agent will act in their own self-interest rather than in yours, pushing deals
                    that
                    may benefit them more than you.
                </div>
                <div className="articleItem">
                    3. Conflict of Interest: Real estate agents may be tempted to try and gain a higher commission by
                    pushing deals that may not be the best fit for their client. This can be especially true when
                    dealing
                    with real estate agents that are employed by a company or individual who stands to benefit from the
                    sale
                    of the property.
                </div>
                <div className="articleItem">
                    <img src="homepage/2.png" alt="Real Estate Agency"/>
                    4. Multiple Listings: Real estate agents often represent multiple clients, which can lead to
                    conflicts
                    of interest between the client and the agent. This can lead to problems like multiple listings of
                    the
                    same home, increased competition between buyers, and inaccurate pricing information.

                </div>
                <div className="articleItem">
                    5. Limited Flexibility: Most real estate agents work on a commission basis and have little
                    flexibility
                    when it comes to negotiating terms or deals. This can mean that a buyer or seller may not get the
                    best
                    deal for their money or have the most control over the negotiation process.
                </div>
                <div className="articleItem">
                    Before engaging a real estate agent for your next transaction, it pays to be aware of the potential
                    risks associated with using a real estate agent. Knowing these potential pitfalls can help you to
                    make
                    an informed decision and ensure that you get the best deal possible.
                </div>
            </div>
        </>
    )
}

export default Article